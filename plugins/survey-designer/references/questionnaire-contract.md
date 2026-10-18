# Authoritative questionnaire contract (version 1)

Store a study as UTF-8 survey.json. This is an internal reproducible source, not a form the researcher must fill manually. Save it with the user-facing instrument so another session can resume without reconstructing chat history.

## Study object

Required keys: schema_version (1), survey_id (stable lowercase ID), version (string), status (draft or complete), title (respondent title), language, study (object), sections (array), questions (array), scores (array).

study contains research_question, mode (hypothesis-led/exploratory/mixed), hypotheses (list of objects with id and text), population, recruitment, sample_limits, target_minutes, and consent (object of known facts/placeholders). Optional researcher-language text and translations must never be mixed into respondent exports. Keep unknown facts null or explicitly marked; do not manufacture values.

## Section objects

Use id, title and description. Topic-group questions belong to one section. Preserve array order. The first section begins naturally without an empty first page. A section may have default_next (a later section ID or END); absent means continue to the next section. Make optional routing questions safe when unanswered by an explicit default route.

## Question objects

Required keys: id (stable machine ID), number (Q1, Q2...), variable, section, type, text, help (may be empty), required (boolean), role (dependent/independent/control/screening/administrative), objectives (list of hypothesis IDs or exploratory objective labels), choices (array), and routes (array).

Supported abstract types: single, multiple, likert, integer, decimal, text, paragraph, note. Represent a scale battery as separately identified items sharing a battery key; an exporter may visually group them only if wording, missingness and routing remain equivalent. Additional properties may record measurement, recall, translation, constraints, missing_policy, randomization, exclusive_choice_codes, choice_groups, eligibility_note, and reason_for_inclusion.

Each choice has code (stable integer or string), label (exact respondent text), and kind: substantive, unknown, no_opinion, not_applicable, refusal, or none. Zero/none can be a substantive value; kind none means an explicit “none of these” option, not missing. Null/blank is unanswered. Structural skip is determined from routing rather than encoded as a valid opinion. Do not prefix labels with analytical numeric codes unless the respondent scale actually uses them.

constraints may include minimum, maximum and integer, and rules linking counts; do not assume every native platform supports every constraint. Record unknown/refusal options for numeric fields separately rather than storing text as a real count. An export must implement those choices equivalently or report the incompatibility.

Routes have choice_code and target (later section ID or END), and apply only to single choice in the common portable subset. Place a routing question last in its section. A calculated or compound condition belongs in explicit advanced_conditions, not disguised as a choice route; flag for exporter capability checking. Do not silently remove unsupported logic. No backward targets or cycles in the portable subset.

Every substantive item needs objectives or a reason_for_inclusion. Factual controls can be single items. Administrative and screening items need not masquerade as dependent variables. Preserve id and variable across renumbering; document substantive changes with a new version rather than silently reusing changed answer codes.

## Scores

Each proposed score has id, items (question IDs), direction, method (sum/mean/other), minimum_answered, reverse_items (IDs), and missing_rule. Define reverse transformations precisely in researcher documentation. Use only substantive ordered responses and never average unknown/NA/refusal codes. A proposed scoring rule is not a claim of demonstrated validity or reliability.

## Completion requirements

Mark status complete only when questionnaire wording, options, periods, item relevance, subgroup comparisons, consent facts, requiredness and routing have passed the lecture audit. Keep researcher notes about sampling/inference and actual pilot status. Completion does not mean piloting occurred or the survey was launched. Do not block a clearly requested draft export; label it as draft and preserve placeholders and implementation limits.

Run scripts/validate_survey.py to check structural integrity and inspect warnings. The script does not replace methodological or language review. Generate codebook.csv with scripts/codebook_csv.py; raw platform exports may still need recoding from labels to the stable choice codes.
