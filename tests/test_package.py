"""Run with python3 -m unittest discover -s tests -v from the marketplace root."""
import copy
import csv
import importlib.util
import json
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / 'plugins' / 'survey-designer'
SCRIPTS = PLUGIN / 'scripts'
spec = importlib.util.spec_from_file_location('validate_survey', SCRIPTS / 'validate_survey.py')
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)


def fixture():
    def question(qid, section, text, choices, role='administrative', objectives=None, kind='single'):
        return dict(id=qid, number='', variable=qid, section=section, type=kind,
                    text=text, help='', required=True, role=role,
                    objectives=objectives or [], choices=choices, routes=[])
    def choice(code, label, kind='substantive'):
        return dict(code=code, label=label, kind=kind)
    consent = question('consent', 'intro', 'TEST ONLY: Do you agree?',
                       [choice(1, 'Yes'), choice(0, 'No')])
    consent['routes'] = [dict(choice_code=1, target='experience'), dict(choice_code=0, target='END')]
    rating = question('rating', 'experience', '食堂の料理にどの程度満足していますか？',
                      [choice(1, 'Dissatisfied'), choice(2, 'Neutral'), choice(3, 'Satisfied'),
                       choice(98, 'No opinion', 'no_opinion')], 'dependent', ['E1'], 'likert')
    reasons = question('reasons', 'experience', 'Select reasons, including any “other” reason.',
                       [choice('taste', 'Taste, quality'), choice('cost', 'Price'),
                        choice('none', 'None of these', 'none')], 'independent', ['E1'], 'multiple')
    reasons['exclusive_choice_codes'] = ['none']
    reasons['required'] = False
    questions = [consent, rating, reasons]
    for i, q in enumerate(questions, 1):
        q['number'] = f'Q{i}'
    return dict(schema_version=1, survey_id='test-only', version='1.0', status='draft',
                title='Synthetic test fixture — do not distribute', language='mixed',
                study=dict(research_question='Test serialization only', mode='exploratory', hypotheses=[],
                           population='Synthetic', recruitment='None', sample_limits='No real respondents',
                           target_minutes=1, consent={'note': 'Synthetic test only'}),
                sections=[dict(id='intro', title='Introduction', description='Test'),
                          dict(id='experience', title='Experience', description='Test')],
                questions=questions, scores=[])


class PackageTests(unittest.TestCase):
    def test_marketplace_resolves_manifest_and_both_skills(self):
        market = json.loads((ROOT / '.agents/plugins/marketplace.json').read_text())
        entry = market['plugins'][0]
        folder = (ROOT / entry['source']['path']).resolve()
        self.assertEqual(folder, PLUGIN)
        manifest = json.loads((folder / 'plugin.json').read_text())
        self.assertEqual(manifest['name'], entry['name'])
        self.assertEqual(manifest['extensions']['com.openai']['interface']['displayName'], 'Survey Designer')
        self.assertEqual({p.name for p in (folder / 'skills').iterdir()}, {'design-survey', 'export-survey'})

    def test_all_relative_markdown_resources_resolve_inside_plugin(self):
        for doc in PLUGIN.rglob('*.md'):
            for target in re.findall(r'\]\(([^)]+)\)', doc.read_text()):
                if '://' in target or target.startswith('#'):
                    continue
                path = (doc.parent / target.split('#')[0]).resolve()
                self.assertTrue(path.is_relative_to(PLUGIN), (doc, target))
                self.assertTrue(path.exists(), (doc, target))

    def test_valid_synthetic_instrument(self):
        errors, warnings = validator.validate(fixture())
        self.assertEqual(errors, [])
        self.assertTrue(any('Structural checks' in w for w in warnings))

    def test_rejects_backward_routing(self):
        data = fixture()
        data['questions'][0]['routes'][0]['target'] = 'intro'
        self.assertTrue(any('later section' in e for e in validator.validate(data)[0]))

    def test_rejects_duplicate_codes(self):
        data = fixture()
        data['questions'][1]['choices'][1]['code'] = 1
        self.assertTrue(any('duplicate choice codes' in e for e in validator.validate(data)[0]))

    def test_rejects_optional_route_without_default(self):
        data = fixture()
        data['questions'][0]['required'] = False
        self.assertTrue(any('default_next' in e for e in validator.validate(data)[0]))

    def test_rejects_unmapped_substantive_item(self):
        data = fixture()
        data['questions'][1]['objectives'] = []
        self.assertTrue(any('no objective' in e for e in validator.validate(data)[0]))

    def test_csv_fidelity_and_cli_validation(self):
        data = fixture()
        with tempfile.TemporaryDirectory() as temp:
            source, output = Path(temp) / 'survey.json', Path(temp) / 'codebook.csv'
            source.write_text(json.dumps(data, ensure_ascii=False), encoding='utf-8')
            check = subprocess.run([sys.executable, '-B', str(SCRIPTS / 'validate_survey.py'), str(source)], capture_output=True, text=True)
            self.assertEqual(check.returncode, 0, check.stdout + check.stderr)
            export = subprocess.run([sys.executable, '-B', str(SCRIPTS / 'codebook_csv.py'), str(source), str(output)], capture_output=True, text=True)
            self.assertEqual(export.returncode, 0, export.stdout + export.stderr)
            with output.open(encoding='utf-8-sig', newline='') as stream:
                rows = list(csv.DictReader(stream))
            self.assertEqual(len(rows), sum(len(q['choices']) for q in data['questions']))
            for q in data['questions']:
                actual = [r for r in rows if r['question_id'] == q['id']]
                self.assertEqual([r['choice_label'] for r in actual], [c['label'] for c in q['choices']])
                self.assertEqual([r['choice_code'] for r in actual], [str(c['code']) for c in q['choices']])
                self.assertTrue(all(r['question'] == q['text'] for r in actual))
                self.assertTrue(all(json.loads(r['routes']) == q['routes'] for r in actual))
            none = next(r for r in rows if r['choice_code'] == 'none')
            self.assertEqual(none['indicator_variable'], 'reasons__none')
            self.assertEqual(none['exclusive'], 'True')
            self.assertEqual(next(r for r in rows if r['choice_code'] == '98')['choice_kind'], 'no_opinion')

    def test_invalid_instrument_does_not_produce_csv(self):
        data = copy.deepcopy(fixture())
        data['questions'][0]['routes'][0]['target'] = 'MISSING'
        with tempfile.TemporaryDirectory() as temp:
            source, output = Path(temp) / 'bad.json', Path(temp) / 'bad.csv'
            source.write_text(json.dumps(data))
            result = subprocess.run([sys.executable, '-B', str(SCRIPTS / 'codebook_csv.py'), str(source), str(output)], capture_output=True, text=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertFalse(output.exists())


if __name__ == '__main__':
    unittest.main()
