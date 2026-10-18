# Survey Designer for regular ChatGPT

Designed by Jason G. Karlin for survey design in academic research and for research design modeling.

This student edition puts the survey-design method in one text file you can upload to an ordinary ChatGPT chat. You do not need Codex, a plugin installation, a custom GPT, an API key or any scripts.

## Download and start

1. **[Download Survey-Designer-ChatGPT.txt](https://github.com/JGKarlin/plugins-and-workflows/releases/download/survey-designer-chatgpt-v1.0.0/Survey-Designer-ChatGPT.txt).** This is the file to upload; you do not need the repository ZIP.
2. Start a new chat in ChatGPT and attach the downloaded text file.
3. Send this message with your own topic:

> Use the attached Survey Designer guide to help me design my survey. Follow its directed-question, design, review and export sequence. My research topic is [describe your topic]. Begin with the most important design question.

If the download opens as text in your browser, save it as a `.txt` file or copy its contents. If attachments are unavailable, paste the entire file into the chat and add the starting message. You can [read the file here](Survey-Designer-ChatGPT.txt).

## What happens next

ChatGPT should ask a focused question about the most important missing design decision. Answer in ordinary language. It helps clarify the research question, population, hypotheses or exploratory objectives, measures, comparison groups and consent. You can start with a broad idea, supply hypotheses, or paste a questionnaire for review.

For example:

> Use the attached Survey Designer guide. I want to investigate whether commuting time is associated with participation in campus events. Help me design a five-minute survey in Japanese.

The workflow connects objectives to questions, reviews wording and answer options, checks routing and explains sampling and interpretation limits. It presents the complete questionnaire, concise researcher notes and a pilot checklist before asking for output format. A format you supplied earlier should be remembered.

You remain responsible for the study's substantive decisions. Read the questions and notes, resolve placeholders and pilot the actual instrument before collecting responses. A completion-time target is not a measured result, and a proposed scale has not automatically been validated.

## Outputs and account limits

The guide is free to download. Your ChatGPT account's message, upload and tool limits apply, including on Free accounts; the download does not unlock additional tools or guarantee that a whole study fits within an account's allowance.

Choose a questionnaire document, CSV codebook, Google Forms script or supported survey-platform format after review. ChatGPT should create downloadable files when its available tools support them. Otherwise it should provide the complete copyable text and explain what remains to be done. Do not treat a text specification as an import-ready native file or a generated script as a tested live form.

For Google Forms, paste the generated script into Google Apps Script, select `createForm`, run it with your authorization, and test the resulting form. Account and organization settings can affect access. The guide should explain the exact remaining steps when it generates the script.

## Continue or start over

Keep working in the same chat. For revisions, ask for changes to the current instrument rather than starting a separate study. Before moving to another chat, ask:

> Give me a handoff containing the current study brief, full questionnaire, version, variable and objective mapping, routing, consent facts, unresolved issues, review and pilot status, and chosen output format.

Save that handoff. In the new chat, upload the guide again, paste the handoff and ask to continue. The guide is not a permanent account setting.

## If the conversation goes off track

- If ChatGPT only summarizes the file, explicitly ask it to follow the guide and begin with a directed design question.
- If it asks for format too early, ask it to finish and review the questionnaire first.
- If it invents study details, correct them and ask it to mark unknown facts as placeholders.
- If it cannot create a file, ask for complete copyable content and save it yourself.

The guide's simulated workflow checks are recorded in [the student test report](../../docs/survey-designer-student-test-results.md). They do not establish a live ChatGPT or Free-account test.
