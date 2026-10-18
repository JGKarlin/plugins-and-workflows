# Google Form Script Prompt

```text
Write a Google Apps Script that creates a Google Form from the questionnaire you just wrote.
- One function, createForm(), that runs as is; create all pages before adding branches.
- Give the form a neutral Japanese title; do not reveal the hypotheses.
- Use the Japanese version: exact wording, options and section order.
- Start each question title with its number (Q1, Q2 …).
- Start a new page for each section; mark required questions.
- Send answers that end the survey (consent, screening) to the end.
- Branch only on single choice answers; Forms cannot branch on counts.
- Log the edit link and the respondent link; add a Japanese thank-you message and a progress bar.

Make the first page a Japanese information and consent page that states:
- Who: [your name], [course, university], contact [email].
- Purpose: the topic in neutral words; do not reveal the hypotheses.
- Data: list the topics asked; no names, emails or street addresses.
- Use: for [course] only; results reported only as group totals.
- Storage: who can see answers, where kept, deleted by [date].
- Voluntary: 18+ only; optional questions can be skipped; stop anytime.
- Withdrawal: anonymous answers cannot be removed once submitted.
- Time and risk: about 5 minutes; no payment and no known risks.
- End: "I agree to take part" Yes / No; "No" ends the survey.

Privacy in the questions:
- Ask for ward, city or town only; collect only what a hypothesis needs.
- Turn off email collection and response editing; no sign-in required.
```
