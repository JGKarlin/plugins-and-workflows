# Survey Designer student edition: simulated checks

Date: 18 October 2026. Instruction source: only `students/survey-designer/Survey-Designer-ChatGPT.txt`, version 1.0.0. The evaluator read the guide locally; the simulated assistant had no shell, installed skills, browsing, or downloadable-file tools. These are simulated instruction-following checks, not live ChatGPT web or Free-account tests. Nothing was installed, exported to a platform, or published.

## Case 1: New topic and early Google Forms preference — PASS

User explicitly adopts the guide and says: “Help me survey why students avoid campus events. I need Google Forms.”

Actual first response:

> By “avoid campus events,” do you mean deliberately choosing not to attend, attending less often, or simply not attending? Those could have different explanations.

Assessment: asks one directed question about a consequential construct; distinguishes intentional avoidance from attendance. It neither asks a format question nor jumps to export. Google Forms remains the known output choice for after design, complete presentation, and review. It claims no tool use.

## Case 2: Existing defective questionnaire — PASS

User explicitly adopts the guide and supplies Q1, “How satisfied are you with campus food and prices?” with satisfied/unsatisfied choices; Q2 asks visits with options 0–3, 3–5, 5+ and no recall period. User asks to export, with no format specified.

Actual first response:

> Before export, two measurement problems need attention. Q1 combines food and prices, which someone may judge differently; its choices also omit neutral and degrees of satisfaction. Q2 has overlapping ranges at 3 and 5 and no stated time period.
>
> What period should the visit question cover—for example, the past seven days or the past month?

Assessment: methodological review precedes the format question. The response asks one directed question, does not silently rewrite the questionnaire, and does not invent the recall period. Further design work would resolve the combined concepts, options, relevant eligibility, and actual consent facts before completion. No external validator or plugin is invoked or claimed.

## Case 3: Reviewed unchanged version; CSV requested without file tools — PASS

Premise: the complete unchanged questionnaire, researcher notes, and documented audit have already been presented. To make the response inspectable without inventing a real student's instrument, this simulation uses a small synthetic codebook fixture: version 1.0; Q1/`event_visits`; optional single-choice item in section `attendance`; exact wording “In the past seven days, how many campus events have you attended?”; codes 0 = “0”, 1 = “1–2”, 2 = “3 or more”; all substantive; dependent variable for objective `attendance_description`; no routes or score; blank means unanswered. The completed consent and study context are stipulated by the test premise, not generated or verified here. User says: “Give me the CSV codebook.”

Actual first response:

I can’t create a downloadable file in this chat. Copy the CSV below into a text file and save it as `survey-codebook.csv` using UTF-8. It preserves the reviewed version; the category codes are labels, not exact event counts. Blank responses remain unanswered. This codebook does not automatically apply value labels in SPSS or R.

```csv
instrument_version,question_id,variable,question_number,question_text,type,role,objectives,required,section,choice_code,choice_label,choice_kind,routing,score_membership,missing_response_rule
1.0,event_visits,event_visits,Q1,"In the past seven days, how many campus events have you attended?",single,dependent,attendance_description,false,attendance,0,0,substantive,none,none,blank=unanswered
1.0,event_visits,event_visits,Q1,"In the past seven days, how many campus events have you attended?",single,dependent,attendance_description,false,attendance,1,1–2,substantive,none,none,blank=unanswered
1.0,event_visits,event_visits,Q1,"In the past seven days, how many campus events have you attended?",single,dependent,attendance_description,false,attendance,2,3 or more,substantive,none,none,blank=unanswered
```

Assessment: no repeated intake, format question, or approval gate. The response supplies actual copyable CSV content for the synthetic fixture and accurately explains the missing downloadable-file capability. It does not fabricate a link, invoke the plugin's scripts, claim execution or successful import, or require Codex. IDs, wording, codes, optionality, missingness, and the absence of routing/scores are preserved. Because browsing is absent, it makes no current platform API or import-schema claim.

## Overall result and limits

All three simulated cases follow the required sequence and remain honest about available capabilities. The guide works as explicitly adopted conversation instructions without relying on installed skills or scripts. Cases 1 and 2 demonstrate directed questioning and methodological review before format selection; case 3 demonstrates a useful plain-text fallback after review.

These checks do not establish real ChatGPT account upload availability, guide retention over a long chat, actual downloadable files, full survey quality, Apps Script execution, native imports, or respondent navigation. A live student test should separately confirm those behaviors on the intended account and survey.
