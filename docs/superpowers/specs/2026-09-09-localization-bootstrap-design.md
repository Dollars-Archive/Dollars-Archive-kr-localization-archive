# Localization Bootstrap Architecture Design

Date: 2026-09-09
Status: Design approved in chat, awaiting repository-spec review before implementation planning

## 1. Purpose

This design turns `Dollars-Archive-kr-localization-archive` into a reusable knowledge base that Codex can consume when starting or restructuring a Korean localization project.

The target experience is intentionally simple:

1. The user gives Codex a game project and this archive.
2. Codex reads one bootstrap entry document.
3. The bootstrap document tells Codex which shared policies and platform-specific notes to read.
4. Codex inspects the actual target project before deciding what applies.
5. Codex designs the project, project-specific review program, extraction/build/validation flow, and web-GPT review data flow without mixing rules from other games.

The archive remains a reusable technical knowledge base. It must not become a storage location for copyrighted original game data, credentials, personal paths, complete original scripts, keys, or other restricted material.

## 2. Existing principles to preserve

The new system must preserve the archive's current technical philosophy:

```text
investigate -> single sample -> runtime verification -> full application -> automated verification -> distribute changed data only
```

It must also preserve these existing rules:

- keep clean originals separate from staging and generated output;
- prefer reproducible tools and builders over unreproducible manual edits;
- verify supported source versions and relevant hashes;
- preserve control codes and binary structure;
- test a single representative sample before bulk application;
- document both successful and failed approaches;
- verify on actual runtime targets, not static inspection alone;
- distribute only permitted changed/delta data, never original game data.

The bootstrap layer may extend these rules but must not weaken them.

## 3. Recommended repository architecture

Use a knowledge-pack architecture with one entry point.

```text
Dollars-Archive-kr-localization-archive/
|
|-- README.md
|-- CODEX-LOCALIZATION-BOOTSTRAP.md
|
|-- workflow/
|   |-- PROJECT-OPERATING-MODEL.md
|   |-- SOL-LUNA-AGENT-POLICY.md
|   `-- PLAYTEST-FEEDBACK-POLICY.md
|
|-- review/
|   |-- REVIEW-DATA-SCHEMA.md
|   |-- REVIEW-STAGE-1.md
|   |-- REVIEW-STAGE-2.md
|   `-- REVIEW-STAGE-3.md
|
|-- templates/
|   |-- AGENTS.template.md
|   |-- glossary.template.csv
|   |-- characters.template.csv
|   |-- relationships.template.csv
|   `-- speech-style.template.csv
|
|-- switch/
|   `-- SWITCH-KOREAN-LOCALIZATION-GUIDE.md
|
`-- docs/
    `-- superpowers/specs/
```

The user should normally need to point Codex only to `CODEX-LOCALIZATION-BOOTSTRAP.md` plus the target game project.

The bootstrap file must act as a router, not as a giant duplicate of every downstream document.

## 4. Isolation model: one game, one localization project, one review program

Each game is an independent localization domain.

Required separation:

```text
one game
  -> one Codex localization project
  -> one game-specific review program
  -> one game-specific Google Drive review workspace
```

Common code may be reused, but game data and game-specific rules must remain isolated.

The following must never be implicitly imported from another game:

- glossary entries;
- character identities;
- character personalities;
- speech styles;
- character relationships;
- honorific/informal-speech rules;
- review decisions;
- runtime offsets;
- binary format assumptions;
- approved translated strings;
- playtest conclusions.

Cross-project reuse requires explicit evidence that the reused implementation is format-compatible. Similar filenames, engines, publishers, series names, or previous success are not sufficient proof.

## 5. Codex responsibility boundary

Codex is responsible for localization engineering, not for doing the main bulk translation pass.

Codex responsibilities include:

- inspect the actual project and supported game version;
- analyze file formats and assets;
- build extraction, insertion, patching, validation, and packaging tools;
- build project-specific review software;
- generate repeatable staging/build flows;
- write and run tests;
- maintain manifests and hashes;
- produce test builds and release-oriented changed-data outputs;
- ingest reviewed CSV results back into the project;
- preserve user-approved playtest corrections.

Bulk dialogue translation and staged linguistic review are performed primarily in web ChatGPT using Google Drive-hosted CSV data and game-specific reference files.

## 6. Agent operating model

### 6.1 Main agent

Default main agent:

```text
GPT-5.6 Sol
reasoning: Medium
```

Sol owns:

- requirement interpretation;
- architecture;
- planning;
- task decomposition;
- decisions that can affect data integrity or runtime behavior;
- subagent delegation;
- integration;
- conflict resolution;
- final verification.

### 6.2 Subagents

Default execution subagents:

```text
GPT-5.6 Luna
reasoning: XHIGH
```

Luna is used for bounded work such as:

- repetitive implementation;
- known-pattern file changes;
- read-only investigation;
- log analysis;
- test writing and execution;
- CSV/JSON/Markdown generation;
- static verification;
- result comparison;
- narrowly scoped bulk operations.

Luna must not independently redefine architecture, change project scope, or reinterpret already approved game-specific translation policy.

### 6.3 Terra

Terra is not part of the default workflow.

### 6.4 Recommended subagent roles

Projects may define at least two local subagents:

- `luna_reader`: read-only investigation and evidence gathering;
- `luna_worker`: bounded implementation and test execution.

Parallel work is allowed only when tasks are independent and do not write the same files or shared mutable state.

The main Sol agent reviews returned evidence and diffs before integration.

## 7. Project-local AGENTS policy

Every localization project should have an `AGENTS.md` derived from the archive template.

It must define at minimum:

- exact project scope and game identity;
- allowed project root;
- forbidden neighboring projects;
- supported game version and source baseline if known;
- agent model policy;
- read/write boundaries;
- stage workflow;
- required tests;
- preservation rules for approved assets and translations;
- conditions that require escalation from Luna to Sol;
- runtime verification requirements;
- rules for recording failures and evidence.

The project-local file overrides generic examples from the archive whenever a game-specific rule exists.

## 8. Google Drive review workspace

Each game gets a separate Google Drive review workspace.

Recommended layout:

```text
<Game>/
|
|-- 00_common-reference/
|   |-- glossary.csv
|   |-- characters.csv
|   |-- relationships.csv
|   `-- speech_style.csv
|
|-- 01_stage-1/
|   |-- INSTRUCTION_1ST.md
|   `-- batch CSV files
|
|-- 02_stage-2/
|   |-- INSTRUCTION_2ND.md
|   `-- batch CSV files
|
|-- 03_stage-3/
|   |-- INSTRUCTION_3RD.md
|   `-- batch CSV files
|
`-- 04_final/
    `-- final reviewed CSV
```

Only common reference data is shared across the three review stages.

Stage instructions must remain physically separated so that stage 1 does not accidentally execute stage-3 behavior and stage 3 does not reinterpret already fixed stage-1 policy without evidence.

## 9. Shared linguistic reference data

### 9.1 `glossary.csv`

Stores fixed terminology such as:

- names;
- places;
- organizations;
- items;
- UI/system terminology;
- recurring concepts;
- spelling and notation rules.

### 9.2 `characters.csv`

Stores character identity and stable characterization:

- canonical name;
- aliases;
- personality;
- behavioral traits;
- stable speech tendencies;
- notable verbal habits.

### 9.3 `relationships.csv`

Stores directed speaker-to-listener relationship rules.

A relation is directional. `A -> B` and `B -> A` must be separate records when speech level, address, status, or emotional stance differs.

Recommended data includes:

- speaker;
- listener;
- relationship type;
- speech level;
- default form of address;
- exceptions;
- effective story range or relationship-change point when relevant.

### 9.4 `speech_style.csv`

Stores how each character speaks independently from whom they are speaking to.

This must remain separate from relationship data because personality and honorific level are different dimensions.

Recommended data includes:

- base speech style;
- sentence-length tendency;
- vocabulary tendency;
- verbal habits;
- emotional-expression tendency;
- expressions to avoid;
- approved representative examples where legally appropriate.

## 10. Three-stage web-GPT review pipeline

The stages intentionally optimize for different tasks.

### 10.1 Stage 1: foundation review

Typical user-visible batch size: about 1,000 rows.

Primary purpose: establish reliable foundations before spending model attention on polished translation.

Focus:

- RSC or project-specific string-size limits;
- missing original/translation fields;
- broken tags, control sequences, placeholders, and line breaks;
- speaker/listener identification where supported by evidence;
- directed relationship rules;
- informal/formal speech compliance;
- address rules;
- obvious character-style violations;
- glossary mismatches;
- severe mistranslation or semantic inversion;
- rows requiring later deeper review.

Stage 1 should avoid unnecessary stylistic rewriting. Its job is to reduce uncertainty for later stages.

If 1,000 rows are too large for reliable model handling, the web workflow may internally process smaller chunks while still tracking the user's stage unit as one 1,000-row batch.

### 10.2 Stage 2: naturalization and character voice

Typical batch size: about 1,000 rows, adjusted when context requires.

Stage 2 assumes that stage-1 structural decisions are the current baseline.

Focus:

- natural Korean;
- removal of literal Japanese phrasing;
- character voice;
- emotional intensity;
- scene-appropriate wording;
- dialogue flow;
- local contextual consistency;
- awkward syntax and repetition.

Stage 2 must not casually overturn established relationship, address, terminology, or speech-level rules. Suspected baseline errors should be flagged with evidence rather than silently replaced.

### 10.3 Stage 3: final precision review

Typical batch size: about 500 rows.

This is the strictest linguistic pass before import into the project review program.

Focus includes all relevant constraints plus:

- precise source meaning;
- subtle mistranslation;
- nuance;
- nearby dialogue context;
- emotional continuity;
- foreshadowing;
- ambiguity;
- jokes and wordplay;
- character consistency;
- particles, word order, rhythm, and readability;
- final RSC/string-size constraints;
- final CSV validity.

The output of stage 3 should be suitable for download as a final reviewed CSV for programmatic import.

## 11. Stage-instruction isolation

Each stage instruction document must begin with an explicit stage boundary.

Required behavior:

- execute only the current stage's goals;
- read common reference files;
- do not import the behavioral goals of another stage;
- do not silently redefine approved rules from an earlier stage;
- flag conflicts instead of inventing a new project rule;
- preserve CSV identifiers and non-translatable structural fields.

This boundary is necessary because the three stages intentionally use different notions of "good work".

## 12. Review program design principle

The project-specific review program is not an AI oracle and must not treat model suggestions as final truth.

It should help accumulate and apply evidence.

Recommended priority of authority:

1. user-confirmed correction observed during actual gameplay;
2. actual in-game context and dialogue evidence;
3. registered project glossary, relationship map, character profile, and speech-style rules;
4. AI analysis or proposed translation.

AI-only judgment must not automatically finalize sensitive relationship or speech-level decisions when stronger evidence is absent.

The program should preserve audit history so later passes can distinguish:

- AI suggestion;
- accepted review change;
- user-confirmed playtest change;
- superseded rule;
- unresolved candidate.

## 13. Final CSV import flow

The intended high-level data flow is:

```text
extract dialogue
  -> prepare review CSV
  -> upload to game-specific Google Drive workspace
  -> stage 1 review
  -> stage 2 review
  -> stage 3 review
  -> download final reviewed CSV
  -> import into game-specific review program
  -> validate identifiers and structural fields
  -> apply approved translation data
  -> build staging output
  -> automated verification
  -> runtime/playtest verification
  -> store user-confirmed corrections
```

Import must be deterministic. The review program should reject or quarantine malformed rows, unknown IDs, broken protected fields, and incompatible schema versions rather than guessing.

## 14. Feedback loop from actual gameplay

Runtime playtesting is the final authority layer and also feeds future review.

When the user confirms a correction during gameplay, the project should be able to record:

- dialogue or asset identifier;
- previous value;
- confirmed value;
- reason/category;
- scene/context reference;
- whether the correction updates a reusable rule such as a relationship or speech-style rule.

Reusable confirmed corrections should improve subsequent review batches without retroactively rewriting unrelated text automatically.

## 15. Bootstrap entry-point behavior

`CODEX-LOCALIZATION-BOOTSTRAP.md` should instruct Codex to follow this order:

1. confirm the target project's exact root and game identity;
2. read the target project's existing `AGENTS.md` and policies first if present;
3. inspect the actual project files and current state;
4. read `PROJECT-OPERATING-MODEL.md` and `SOL-LUNA-AGENT-POLICY.md`;
5. select only platform/domain guides relevant to the actual project;
6. preserve already proven project-specific methods and outputs;
7. identify unknowns and risks;
8. create or update a staged plan;
9. begin with investigation or a single representative sample, not bulk replacement;
10. verify successful samples at runtime before scaling;
11. use Luna only for bounded delegated work;
12. keep translation/review data compatible with the game-specific review workflow;
13. produce repeatable tools, tests, manifests, and evidence;
14. never claim success until the relevant output is re-read, tested, or otherwise verified.

The bootstrap must explicitly say that repository documents are guidance, not substitutes for inspecting the target project's real files.

## 16. Platform guide routing

The bootstrap should route by evidence.

For example:

- Nintendo Switch project -> read `switch/SWITCH-KOREAN-LOCALIZATION-GUIDE.md`;
- future PSP/PS2/PC/Unity/other guides -> read only when they match the actual target.

Codex must not assume a platform-specific binary or packaging method merely because another project in the archive used it.

## 17. Updating the archive with new knowledge

The archive is meant to improve as projects are completed.

When a project discovers a reusable technique, it may be distilled into this archive only when:

- the technique is general enough to help another project;
- copyrighted original game data is excluded;
- personal/local absolute paths are removed;
- credentials and secrets are removed;
- project-specific assumptions are labeled as examples rather than universal rules;
- success conditions and known failure modes are documented.

The archive should capture reasoning-relevant evidence, not merely a final command with no explanation.

## 18. Implementation phases

Implementation should occur in small repository changes after this design is approved.

Recommended order:

1. add `CODEX-LOCALIZATION-BOOTSTRAP.md`;
2. add workflow policy documents;
3. add three stage-specific review policy documents plus review data schema;
4. add reusable templates;
5. update `README.md` to expose the new entry point;
6. verify links and internal consistency;
7. test the bootstrap against at least one existing localization project as a dry-run/document review before treating it as stable.

## 19. Acceptance criteria

The design is successfully implemented when:

- a user can give Codex the archive plus a target game project and point it to one bootstrap file;
- Codex is instructed to inspect the real project before choosing techniques;
- Sol/Luna responsibilities are explicit and Terra is excluded by default;
- project boundaries prevent accidental cross-game data reuse;
- each game gets a separate review program and Drive review workspace;
- common linguistic reference schemas are defined;
- stage 1, 2, and 3 have distinct goals and physically separate instructions;
- stage 1 supports roughly 1,000-row foundation review;
- stage 3 supports roughly 500-row strict final review;
- final reviewed CSV data has a deterministic import path;
- playtest-confirmed user corrections outrank AI suggestions;
- existing Switch localization engineering rules remain intact;
- archive updates remain safe for public GitHub publication;
- all repository links and templates are internally consistent.

## 20. Non-goals for the first implementation

The first version will not attempt to:

- build one universal review application for all games;
- automatically translate entire games inside Codex;
- automatically overwrite user-confirmed translations based only on AI judgment;
- infer relationships from character personality alone;
- merge all platform knowledge into one oversized document;
- create a full autonomous release pipeline without explicit project-specific verification;
- treat historical techniques as universally valid without checking the current project.

These exclusions keep the system predictable and make the archive more useful as it grows.
