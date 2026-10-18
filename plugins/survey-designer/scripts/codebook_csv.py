#!/usr/bin/env python3
"""Export exact labels/codes from the validated authoritative instrument."""
import csv
import json
import sys
from pathlib import Path
from validate_survey import validate


def main():
    if len(sys.argv) != 3:
        print("Usage: codebook_csv.py survey.json codebook.csv", file=sys.stderr)
        return 2
    try:
        data = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
        errors, _ = validate(data)
        if errors:
            raise ValueError("; ".join(errors))
        fields = ["survey_id", "version", "question_id", "number", "variable", "indicator_variable", "section", "question", "help", "type", "role", "objectives", "required", "choice_code", "choice_label", "choice_kind", "exclusive", "routes", "scores", "scoring_rules", "missing_policy"]
        destination = Path(sys.argv[2])
        destination.parent.mkdir(parents=True, exist_ok=True)
        with destination.open("w", encoding="utf-8-sig", newline="") as stream:
            writer = csv.DictWriter(stream, fieldnames=fields)
            writer.writeheader()
            for q in data["questions"]:
                memberships = [s for s in data["scores"] if q["id"] in s["items"]]
                for choice in q["choices"] or [{}]:
                    row = {key: q.get(key, "") for key in ("number", "variable", "section", "help", "type", "role", "required")}
                    code = choice.get("code", "")
                    row.update(survey_id=data["survey_id"], version=data["version"], question_id=q["id"], question=q["text"], objectives=json.dumps(q["objectives"], ensure_ascii=False), choice_code=code, choice_label=choice.get("label", ""), choice_kind=choice.get("kind", ""), exclusive=code in q.get("exclusive_choice_codes", []), routes=json.dumps(q["routes"], ensure_ascii=False), scores=json.dumps([s["id"] for s in memberships], ensure_ascii=False), scoring_rules=json.dumps(memberships, ensure_ascii=False), missing_policy=json.dumps(q.get("missing_policy", {}), ensure_ascii=False))
                    row["indicator_variable"] = f"{q['variable']}__{code}" if q["type"] == "multiple" else ""
                    writer.writerow(row)
        print(destination)
        return 0
    except (OSError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
