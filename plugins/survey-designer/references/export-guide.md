# Export workflow and platform boundaries

Apply the lecture's fidelity principle (slide 58): the same instrument, identifiers, answer codes and codebook across tools. Generate actual files after format selection, not another prompt. Check current official documentation at export time and test actual import paths when access permits.

## Google Forms / Google Apps Script

Deliver a .gs file with one public createForm() entry point and no API-key requirement for FormApp. Keep helper functions inside it if the user wants one function. Use FormApp.create with a neutral respondent title; preserve exact respondent text and sections. Create items/pages in their correct physical order and store references, then set all navigation choices once destinations exist. Do not append all page breaks before their questions and accidentally place the items on the last page.

Use a topic per section. Put independent terminating screens on separate pages when necessary: consent refusal, age exclusion, geography exclusion, etc. All choices on a routing question must consistently carry navigation; apply SUBMIT to terminating choices. Native navigation takes effect at page completion, not instantly on clicking an answer. Avoid multiple routing questions on the same page, whose instructions can conflict.

Use single-choice routes; do not promise count comparison, multi-select branching, row-level conditional display or arbitrary Boolean routing in native Forms. Do not silently replace unsupported logic with visible optional questions. Explain the specific incompatibility and agree a substantive revision or documented manual step. Preserve the direct avoidance group in the Shibuya example.

Do not claim numeric answer-code export from labels alone. Supply a codebook/recoding map. Keep unknown and NA outside substantive scale scoring, even if Forms renders them as separate unnumbered grid columns. If that presentation is inadequate for the instrument, use separate items or another agreed display.

Preserve randomization and fixed terminal choices only if actually implemented. A one-time shuffle at script generation is not per-respondent randomization. Do not claim item-level shuffling from a method the API does not expose. Check the current Forms API/Forms REST schema before using any such feature; disclose manual configuration precisely.

SetCollectEmail(false), setAllowResponseEdits(false), setLimitOneResponsePerUser(false), setShuffleQuestions(false), setPublishingSummary(false), an appropriate confirmation message, and a progress bar. These do not override an organization's access policy; verify respondent access before claiming no sign-in. Do not promise complete anonymity from these settings alone. Log getEditUrl() and getPublishedUrl().

Tell the researcher to paste into a standalone project, save, choose createForm in the function dropdown and run. Explain that every run creates a new form unless a deliberately designed update mechanism is supplied. Do not require a fake myFunction wrapper. Distinguish script syntax checks, API mocks, live execution, actual respondent-path tests and publication.

Official starting points:
https://developers.google.com/apps-script/reference/forms/form
https://developers.google.com/apps-script/reference/forms/multiple-choice-item
https://developers.google.com/apps-script/reference/forms/page-navigation-type

## Word and PDF

Generate respondent-only or researcher versions as requested. Keep translation, variables and hypotheses only in the researcher version. Include all response options and legible instructions. Print skip instructions and optionality where appropriate. A printable questionnaire cannot automatically enforce routing. Use document/PDF skills, render and inspect every page, and include a version label without exposing the research hypothesis to respondents.

## Qualtrics

Use properly structured Advanced Format TXT for supported question/block features; a generic list of questions is not an advanced-format file. Do not assume TXT imports preserve display logic, quotas, all recode settings or randomization. Provide exact remaining configuration and validate the imported survey when access exists. Use a tested QSF-based route only when its schema and import have been verified; do not invent QSF fields.

https://www.qualtrics.com/support/survey-platform/survey-module/survey-tools/import-and-export-surveys/

## XLSForm for KoboToolbox / ODK

Use a genuine .xlsx with survey, choices and settings sheets and stable names/codes. Use label language columns for respondent translations, required and constraint columns as appropriate, and relevant conditions for skips. Numeric comparisons and multi-select relevance are possible in this platform; don't transfer Google Forms limitations here. Validate with the actual XLSForm converter/target platform when available; state if only workbook structure was checked.

https://support.kobotoolbox.org/getting_started_xlsform.html
https://support.kobotoolbox.org/skip_logic_xls.html
https://docs.getodk.org/xlsform/

## LimeSurvey

Use its defined Tab Separated Value survey-structure schema with UTF-8 and the supported .txt extension, not an arbitrary TSV table. Include group/question/subquestion/answer records and relevant settings according to current version documentation. Verify codes, conditions and actual import; document manual configuration rather than implying identical support across versions.

https://www.limesurvey.org/manual/Tab_Separated_Value_Survey_Structure

## Microsoft Forms when requested

Word/PDF Quick Import is a limited conversion path. Current documentation supports titles/subtitles, multiple-choice and open-text questions; do not promise a faithful import of Likert grids, all sections or branching. Produce a suitable import document and a precise list of configuration work, or agree another supported route. Do not claim the questionnaire is unchanged if scales must be restructured.

https://support.microsoft.com/en-gb/forms/convert-a-word-or-pdf-form-or-quiz-to-microsoft-forms

## CSV codebook

Include survey version, item/variable IDs, question numbers/text, type, role/objectives, answer codes/labels/kinds, requiredness, section, routing and score membership. For multi-select items document indicator variables and the distinction between unchecked and unanswered. A CSV codebook is documentation, not executable SPSS/R label syntax. Offer separate analysis syntax only when requested.

## Delivery and revisions

Generate only the selected format(s), with the same survey version. Keep the specification/codebook available for later exports. Validate textual and logical fidelity rather than only whether a file exists. State any untested import or necessary manual work. A new format does not restart the interview; a substantive questionnaire change updates the source version and affected outputs.
