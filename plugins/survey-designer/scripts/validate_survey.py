#!/usr/bin/env python3
"""Check structural survey fidelity; methodological review remains a skill task."""
import json
import sys
from pathlib import Path

TYPES = {"single", "multiple", "likert", "integer", "decimal", "text", "paragraph", "note"}
ROLES = {"dependent", "independent", "control", "screening", "administrative"}
KINDS = {"substantive", "unknown", "no_opinion", "not_applicable", "refusal", "none"}


def validate(data):
    errors, warnings = [], []
    if not isinstance(data, dict):
        return ["Survey must be an object."], []
    for key in ("schema_version", "survey_id", "version", "status", "title", "language", "study", "sections", "questions", "scores"):
        if key not in data:
            errors.append(f"Missing survey field: {key}")
    if data.get("schema_version") != 1:
        errors.append("schema_version must be 1.")
    if data.get("status") not in {"draft", "complete"}:
        errors.append("status must be draft or complete.")
    study = data.get("study", {})
    if not isinstance(study, dict):
        return errors + ["study must be an object."], warnings
    for key in ("research_question", "mode", "hypotheses", "population", "recruitment", "sample_limits", "target_minutes", "consent"):
        if key not in study:
            errors.append(f"Missing study field: {key}")
    if study.get("mode") not in {"hypothesis-led", "exploratory", "mixed"}:
        errors.append("Unknown study mode.")
    hypotheses = study.get("hypotheses", [])
    if not isinstance(hypotheses, list):
        errors.append("hypotheses must be an array.")
        hypotheses = []
    if study.get("mode") == "hypothesis-led" and not hypotheses:
        errors.append("A hypothesis-led study needs hypotheses.")
    sections, questions = data.get("sections", []), data.get("questions", [])
    if not isinstance(sections, list) or not isinstance(questions, list):
        return errors + ["sections and questions must be arrays."], warnings
    if not sections or not questions:
        errors.append("The instrument needs sections and questions.")
    if any(not isinstance(s, dict) for s in sections) or any(not isinstance(q, dict) for q in questions):
        return errors + ["Section/question entries must be objects."], warnings
    section_ids = [s.get("id") for s in sections]
    question_ids = [q.get("id") for q in questions]
    variables = [q.get("variable") for q in questions]
    for label, values in (("section IDs", section_ids), ("question IDs", question_ids), ("variables", variables)):
        if any(not isinstance(v, str) or not v for v in values):
            errors.append(f"All {label} must be nonempty strings.")
        elif len(set(values)) != len(values):
            errors.append(f"Duplicate {label}.")
    positions = {s: i for i, s in enumerate(section_ids) if isinstance(s, str)}
    numbers = [q.get("number") for q in questions]
    if numbers != [f"Q{i + 1}" for i in range(len(questions))]:
        errors.append("Question numbers must follow Q1, Q2, ... in instrument order.")
    last_position = -1
    for i, q in enumerate(questions):
        label = q.get("id", f"question {i + 1}")
        for key in ("id", "number", "variable", "section", "type", "text", "help", "required", "role", "objectives", "choices", "routes"):
            if key not in q:
                errors.append(f"{label}: missing {key}.")
        if q.get("type") not in TYPES or q.get("role") not in ROLES:
            errors.append(f"{label}: invalid type or role.")
        if not isinstance(q.get("required"), bool):
            errors.append(f"{label}: required must be boolean.")
        if not isinstance(q.get("text"), str) or not q["text"].strip():
            errors.append(f"{label}: missing respondent text.")
        position = positions.get(q.get("section"), -1)
        if position < 0:
            errors.append(f"{label}: unknown section.")
        elif position < last_position:
            errors.append(f"{label}: question order moves backward across sections.")
        last_position = max(last_position, position)
        if not q.get("objectives") and q.get("role") not in {"administrative", "screening"} and not q.get("reason_for_inclusion"):
            errors.append(f"{label}: no objective or justified inclusion.")
        choices, routes = q.get("choices", []), q.get("routes", [])
        if not isinstance(choices, list) or any(not isinstance(c, dict) for c in choices):
            errors.append(f"{label}: choices must be objects in an array.")
            continue
        codes = [c.get("code") for c in choices]
        code_keys = [json.dumps(c, sort_keys=True) for c in codes]
        if len(set(code_keys)) != len(code_keys) or any(c is None or isinstance(c, (list, dict, bool)) for c in codes):
            errors.append(f"{label}: invalid or duplicate choice codes.")
        if q.get("type") in {"single", "multiple", "likert"} and len(choices) < 2:
            errors.append(f"{label}: choice items need at least two choices.")
        for choice in choices:
            if not choice.get("label") or choice.get("kind") not in KINDS:
                errors.append(f"{label}: each choice needs a label and recognized kind.")
        for code in q.get("exclusive_choice_codes", []):
            if code not in codes:
                errors.append(f"{label}: exclusive code does not exist.")
        if not isinstance(routes, list) or any(not isinstance(r, dict) for r in routes):
            errors.append(f"{label}: invalid routes.")
            continue
        if routes and q.get("type") != "single":
            errors.append(f"{label}: portable choice routing requires single choice.")
        if routes and any(later.get("section") == q.get("section") and later.get("type") != "note" for later in questions[i + 1:]):
            errors.append(f"{label}: routing question must be last in its section.")
        seen = set()
        for route in routes:
            code, target = route.get("choice_code"), route.get("target")
            key = json.dumps(code, sort_keys=True)
            if code not in codes or key in seen:
                errors.append(f"{label}: unknown or duplicate route choice.")
            seen.add(key)
            if target != "END" and (target not in positions or positions[target] <= position):
                errors.append(f"{label}: route must target a later section or END.")
        if routes and len(seen) != len(codes):
            errors.append(f"{label}: every routing choice needs an explicit target.")
        if routes and not q.get("required"):
            section = next((s for s in sections if s.get("id") == q.get("section")), {})
            if not section.get("default_next"):
                errors.append(f"{label}: optional routing needs an explicit section default_next.")
        if q.get("advanced_conditions"):
            warnings.append(f"{label}: verify advanced conditions against the selected platform.")
        if q.get("randomization"):
            warnings.append(f"{label}: verify real per-respondent randomization and fixed choices.")
    for section in sections:
        target = section.get("default_next")
        if target and target != "END" and (target not in positions or positions[target] <= positions.get(section.get("id"), -1)):
            errors.append(f"{section.get('id')}: default_next must move forward or end.")
    scores = data.get("scores", [])
    if not isinstance(scores, list):
        errors.append("scores must be an array.")
        scores = []
    for score in scores:
        if not isinstance(score, dict):
            errors.append("Score must be an object.")
            continue
        for key in ("id", "items", "direction", "method", "minimum_answered", "reverse_items", "missing_rule"):
            if key not in score:
                errors.append(f"Score missing {key}.")
        items = score.get("items", [])
        if not isinstance(items, list) or not items or any(qid not in question_ids for qid in items):
            errors.append(f"{score.get('id')}: invalid score members.")
        elif not isinstance(score.get("minimum_answered"), int) or not 1 <= score["minimum_answered"] <= len(items):
            errors.append(f"{score.get('id')}: invalid minimum_answered.")
        if any(qid not in items for qid in score.get("reverse_items", [])):
            errors.append(f"{score.get('id')}: reverse item not a score member.")
    warnings.append("Structural checks do not establish wording quality, sampling validity, scale reliability, pilot completion or successful platform import.")
    return errors, warnings


def main():
    if len(sys.argv) != 2:
        print("Usage: validate_survey.py survey.json", file=sys.stderr)
        return 2
    try:
        data = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
        errors, warnings = validate(data)
    except (OSError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    for message in errors:
        print("ERROR: " + message)
    for message in warnings:
        print("WARNING: " + message)
    print(f"{len(errors)} errors; {len(warnings)} warnings.")
    return int(bool(errors))


if __name__ == "__main__":
    raise SystemExit(main())
