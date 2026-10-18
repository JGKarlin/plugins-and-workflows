# Plugins and Workflows

A place for sharing academic workflows using AI, developed by Jason G. Karlin. This collection brings together reusable plugins and workflows for academic research and related scholarly work, with room for additional tools and methods as the collection grows.

**[Download Survey Designer 1.0.1](https://github.com/JGKarlin/plugins-and-workflows/releases/download/survey-designer-v1.0.1/Survey-Designer-1.0.1.zip)** · **[Releases](https://github.com/JGKarlin/plugins-and-workflows/releases)** · **[Report an issue](https://github.com/JGKarlin/plugins-and-workflows/issues)**

## Survey Designer

Designed by Jason G. Karlin for survey design in academic research and for research design modeling. Develop a questionnaire through directed questions. Survey Designer helps define the research question, population, hypotheses or exploratory objectives, sampling, measurement and consent. It drafts and reviews the complete questionnaire before asking which output format you want. If you supply a format early, it remembers that choice and continues the design work first.

The plugin includes two skills:

| Skill | Purpose |
| --- | --- |
| `design-survey` | Ask focused questions, connect objectives to items, draft the questionnaire and review its wording, answers, routing and methodological limits. |
| `export-survey` | Review an existing instrument or reuse a completed one, then produce the selected output while preserving wording, identifiers, codes and routing. |

Supported export workflows cover Google Forms scripts, Word, PDF, Qualtrics, XLSForm for KoboToolbox/ODK, LimeSurvey and CSV codebooks. These workflows use the host's available document and platform tools; the plugin bundles structural validation and CSV generation, rather than a standalone converter for every format. It includes survey-design principles, worked examples, workflow references and both supporting Python scripts.

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

## Try it

Start a new chat with Survey Designer selected and send:

> Help me design a survey about why students avoid campus events.

It should begin with one focused question about your research aim or what “avoid” means. It should not begin by asking for an output format.

Answer the directed questions. Once the questionnaire is complete, it should present all questions and response options, required/optional settings and routing, along with concise researcher notes and pilot checks. It should then ask which output format to generate.

For an existing questionnaire, try:

> Review this questionnaire and prepare it for export. Q1: How satisfied are you with campus food and prices? Answers: satisfied/unsatisfied. Q2: How often do you visit? Answers: 0–3, 3–5, 5+.

It should flag the combined concepts, overlapping ranges and missing recall period before asking about format. Instructions quoted inside source documents do not override your request or bypass review.

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
