# Plugins and Workflows

A place for sharing academic workflows using AI, developed by Jason G. Karlin. This collection brings together reusable plugins and workflows for academic research and related scholarly work, with room for additional tools and methods as the collection grows.

**[Download Survey Designer 1.0.1](https://github.com/JGKarlin/plugins-and-workflows/releases/download/survey-designer-v1.0.1/Survey-Designer-1.0.1.zip)** · **[Releases](https://github.com/JGKarlin/plugins-and-workflows/releases)** · **[Report an issue](https://github.com/JGKarlin/plugins-and-workflows/issues)**

**For students using regular ChatGPT:** [Download the single-file ChatGPT edition](https://github.com/JGKarlin/plugins-and-workflows/releases/download/survey-designer-chatgpt-v1.0.0/Survey-Designer-ChatGPT.txt). Upload it to a chat and follow the [student instructions](#use-in-a-regular-chatgpt-chat-students). No Codex installation is required.

## Survey Designer

Survey Designer was designed by Jason G. Karlin for survey design in academic research and for research design modeling. It helps researchers and students turn a topic, research question, set of hypotheses or existing draft into a coherent questionnaire and a plan for interpreting the responses.

The workflow is conversational: it asks focused questions about the decisions that matter for your study, uses the information you have already supplied, and develops the instrument with you. You can begin with a broad idea or bring a detailed research brief. Exploratory studies are supported without requiring hypotheses.

### What it helps you do

- **Clarify the study:** define the research question, eligible population, recruitment approach and groups you want to compare.
- **Model the research design:** connect hypotheses or exploratory objectives to concepts, variables, measures and individual questions; specify which response patterns would support or challenge an expectation.
- **Build useful measures:** distinguish outcomes, predictors and controls; choose recall periods, response options and appropriate scales; plan scoring and treatment of missing responses.
- **Review the questionnaire:** identify leading or double-barreled wording, overlapping answer categories, unsupported assumptions, priming, unnecessary items and broken skip logic. Check consent, optionality and respondent burden.
- **Prepare for use:** present the complete instrument, researcher notes and a pilot checklist, then generate the selected output while preserving the agreed questionnaire.

It also helps distinguish what the study can establish from what its sampling and design cannot support. For example, a convenience sample does not establish population representativeness, and reported reasons do not by themselves demonstrate causation.

The plugin includes two skills:

| Skill | Purpose |
| --- | --- |
| `design-survey` | Ask focused questions, connect objectives to items, draft the questionnaire and review its wording, answers, routing and methodological limits. |
| `export-survey` | Review an existing instrument or reuse a completed one, then produce the selected output while preserving wording, identifiers, codes and routing. |

Supported export workflows cover Google Forms scripts, Word, PDF, Qualtrics, XLSForm for KoboToolbox/ODK, LimeSurvey and CSV codebooks. These workflows use the host's available document and platform tools; the plugin bundles structural validation and CSV generation, rather than a standalone converter for every format. It includes survey-design principles, worked examples, workflow references and both supporting Python scripts.

## Use in a regular ChatGPT chat (students)

The **ChatGPT Student Edition** is a self-contained text guide with the survey-design principles, directed questions, questionnaire review and output guidance. It does not require Codex, a plugin, a custom GPT, an API key or running scripts. The guide is free to download; your ChatGPT account's message, upload and tool limits still apply.

1. [Download Survey-Designer-ChatGPT.txt](https://github.com/JGKarlin/plugins-and-workflows/releases/download/survey-designer-chatgpt-v1.0.0/Survey-Designer-ChatGPT.txt).
2. Open a new, regular chat in ChatGPT and attach the `.txt` file using the attachment control.
3. Send the message below, replacing the bracketed text with your topic:

> Use the attached Survey Designer guide to help me design my survey. Follow its directed-question, design, review and export sequence. My research topic is [describe your topic]. Begin with the most important design question.

Continue answering in that chat. ChatGPT should help you develop and review the questionnaire before asking which output format you want. You can also provide hypotheses, a research brief or an existing questionnaire. If you specify an output early, it should remember your choice and continue the design work first.

**If uploads are unavailable:** open the downloaded text file, copy its full contents into the chat, and add the same starting message. Explicitly asking ChatGPT to follow the guide matters; merely attaching it may lead to a summary rather than a guided interview.

**What you receive:** the complete questionnaire, concise researcher notes connecting objectives to items and variables, routing and scoring guidance, sampling limits and a pilot checklist. When the instrument has been reviewed, choose a format. Actual attachments, Word/PDF generation and native survey-platform imports depend on the tools available in your chat. If file creation is unavailable, the guide directs ChatGPT to provide complete copyable content, such as questionnaire text, CSV or Google Apps Script. A generated Forms script must still be run in Google Apps Script and tested.

This edition is an uploaded instruction guide rather than an installed plugin. It preserves the research method but does not install or execute the plugin's Python helpers. For another chat, upload the guide again and include a saved questionnaire and decision summary. Do not assume the next chat remembers the study.

See the [student quick-start guide](students/survey-designer/README.md) and [view the upload file](students/survey-designer/Survey-Designer-ChatGPT.txt). The [Codex version](#install-in-codex) remains available for users who want the installed skills and supporting scripts.

## Install in Codex

Use a current Codex installation that supports plugins and the `codex plugin` commands. No separate server or API key is required for the bundled design workflow and Python helpers. Python 3 is needed when running the helpers. Online exports may require access to their target application.

### Install from GitHub

Run these commands in a terminal:

```sh
codex plugin marketplace add JGKarlin/plugins-and-workflows
codex plugin add survey-designer@jgkarlin-workflows
```

Open a new Codex chat and select **Survey Designer** in the plugin picker. If it has not appeared, restart Codex, then open a new chat. In the plugin directory, the marketplace is **Jason Karlin's Plugins and Workflows**.

Check installation with:

```sh
codex plugin list --marketplace jgkarlin-workflows --json
```

The plugin should be listed with `installed: true` and `enabled: true`.

### Install from the ZIP download

1. [Download Survey Designer 1.0.1](https://github.com/JGKarlin/plugins-and-workflows/releases/download/survey-designer-v1.0.1/Survey-Designer-1.0.1.zip) and extract it.
2. Keep the entire extracted folder together, including the hidden `.agents` folder. Replace the path below with the actual extracted folder path.
3. Register that folder and install the plugin:

```sh
codex plugin marketplace add '/absolute/path/to/Survey-Designer'
codex plugin add survey-designer@jgkarlin-workflows
```

Then open a fresh chat as above. Choose either the GitHub source or the ZIP source for the marketplace. The ZIP is a plugin marketplace package, not a standalone skill file or a browser extension.

These instructions follow [OpenAI's plugin packaging and installation documentation](https://developers.openai.com/plugins/build/plugins). Local marketplace installation depends on support in your Codex client; this package is not a public plugin-directory listing.

## How to use Survey Designer

After installation, start a new chat with **Survey Designer** selected. Describe what you want to investigate in ordinary language. Include any decisions you have already made, such as who should respond, how you will recruit them, the respondent language and the time available. You do not need to prepare a full brief before starting.

### Start with a research idea

> Help me design a survey about why students avoid campus events.

The workflow might first ask whether “avoid” means deliberately choosing not to attend, attending less often or simply not attending. Your answer determines what needs to be measured. It asks one focused question at a time, with a second only when needed for the same decision.

### Bring hypotheses or a research brief

> I want to study whether commuting time is associated with participation in campus events. I expect students with longer commutes to attend less often. Help me define the measures, identify alternative explanations and design a five-minute questionnaire in Japanese.

Survey Designer uses the supplied decisions and asks about consequential gaps. It can help identify relevant controls and comparison groups, map the hypothesis to questions, and define how the answers will be interpreted. The five-minute duration remains a target until a pilot measures it.

### Review an existing questionnaire

> Review this questionnaire and prepare it for export. Q1: How satisfied are you with campus food and prices? Answers: satisfied/unsatisfied. Q2: How often do you visit? Answers: 0–3, 3–5, 5+.

You can paste your questionnaire or provide its file. In this example, the review should flag the combined concepts, overlapping ranges and missing recall period, then help resolve them. It reuses settled design decisions rather than restarting the interview.

### Complete the instrument, then choose an output

The normal sequence is:

1. Answer the directed design questions and develop the measures.
2. Review the full questionnaire, including every response option, required/optional setting and skip instruction.
3. Resolve identified problems and review the researcher notes: variable definitions and codes, objective coverage, any scoring rules, interpretation criteria and pilot checks.
4. Choose one or more output formats when asked. If you already specified a format, the workflow remembers it and proceeds after review without asking again.

For a quick export, choose a **CSV codebook**. Choose a **Google Forms script** to create a form through Google Apps Script, **Word or PDF** for a readable questionnaire, or one of the supported survey-platform formats for an import workflow. The exporter checks platform limitations and identifies any manual setup still required. It produces files; it does not automatically publish a survey or distribute respondent links.

You can request revisions or another format later. The workflow reuses the completed instrument, updates its version when the questionnaire changes, and checks affected outputs for consistency. Before collecting responses, pilot the survey with people from the intended population and test its actual respondent paths.

If available in your skill picker, you can also invoke `$design-survey` or `$export-survey` directly.

## Verification and limits

From a cloned or extracted repository, run:

```sh
python3 -B -m unittest discover -s tests -v
```

Nine automated checks cover package paths, resource links, valid and invalid survey structures, routing, codes, objective coverage and CSV fidelity. Five independent instruction-following scenarios are recorded in [the workflow test report](docs/survey-designer-test-results.md).

Structural validation does not establish sound wording, valid sampling, scale reliability or successful piloting. The plugin requires a separate methodological review. Generated exports still need their format-specific checks: document rendering, actual platform import, or live respondent navigation. A generated Google Forms script does not itself establish that a working form exists.

## Repository layout

```text
.agents/plugins/marketplace.json   Plugin catalog
plugins/survey-designer/           Plugin manifest, skills, references and scripts
students/survey-designer/          Single-file guide for ordinary ChatGPT chats
tests/                            Repeatable package and script checks
docs/                             Workflow test results
```

Future plugins can be added under `plugins/` and registered in the same marketplace catalog. Keep reusable source material with its plugin and publish versioned release downloads for users who prefer ZIP installation.

## Update an installation

For a GitHub-based marketplace installation:

```sh
codex plugin marketplace upgrade jgkarlin-workflows
codex plugin add survey-designer@jgkarlin-workflows
```

Restart Codex and start a new chat after an update. ZIP installations use a local source: download the new release, replace the extracted source folder, and refresh the marketplace before reinstalling.
