# Localization Bootstrap Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a standalone Codex localization bootstrap knowledge pack without merging it into the existing GPT/GitHub or Nintendo Switch guides.

**Architecture:** Keep the current guides unchanged. Add one new top-level bootstrap entry point that routes Codex to focused workflow, review, and template documents. The bootstrap instructs Codex to inspect the real target project first, then selectively read only the relevant archive guidance. README gains a new independent documentation section that links to the bootstrap entry point.

**Tech Stack:** Markdown, CSV templates, GitHub repository documentation

**Spec:** `docs/superpowers/specs/2026-09-09-localization-bootstrap-design.md`

## Global Constraints

- Existing `GPT-GITHUB-OPERATIONS.md` content must not be merged with or rewritten for this feature.
- Existing `switch/SWITCH-KOREAN-LOCALIZATION-GUIDE.md` content must not be merged with or rewritten for this feature.
- The new system must preserve the archive principle: `조사 → 단일 샘플 → 실기 검증 → 전체 적용 → 자동 검증 → 변경분만 배포`.
- One game equals one Codex localization project, one game-specific review program, and one game-specific Google Drive review workspace.
- Default model policy is GPT-5.6 Sol / Medium for planning and integration, GPT-5.6 Luna / XHIGH for bounded delegated work, and Terra excluded by default.
- Web ChatGPT performs the main staged linguistic review from Google Drive-hosted CSV data.
- Review Stage 1, Stage 2, and Stage 3 instructions must be physically separate and must not import each other's behavioral goals.
- Stage 1 targets foundation review in about 1,000-row units.
- Stage 2 targets natural Korean and character voice using Stage 1 decisions as baseline.
- Stage 3 targets strict final review in about 500-row units.
- User-confirmed playtest corrections outrank AI suggestions.
- Public repository documents must not include copyrighted original game data, complete original scripts, credentials, secrets, personal paths, keys, or restricted assets.
- Codex must treat archive documents as reusable guidance, never as a substitute for inspecting the target project's real files.

---

### Task 1: Add the standalone bootstrap entry point

**Files:**
- Create: `CODEX-LOCALIZATION-BOOTSTRAP.md`

**Interfaces:**
- Consumes: repository-level architecture from the approved spec
- Produces: single entry point that routes Codex to workflow, review, templates, and platform guides

- [ ] **Step 1: Create the bootstrap document with explicit operating order**

The document must tell Codex to:

1. identify the exact target project root and game;
2. read target-project `AGENTS.md` first when present;
3. inspect actual project files and current state before choosing techniques;
4. read `workflow/PROJECT-OPERATING-MODEL.md`;
5. read `workflow/SOL-LUNA-AGENT-POLICY.md`;
6. read review documents only when building or operating the review pipeline;
7. read only platform guides relevant to the actual project, such as the Switch guide for a Switch project;
8. preserve already proven project-specific methods and approved outputs;
9. begin risky changes with investigation or a single representative sample;
10. verify runtime behavior before scaling to bulk application;
11. keep one game's data and rules isolated from every other game;
12. never claim completion before re-reading or testing the produced result.

The document must include an explicit statement that this new bootstrap is a standalone document and does not replace the existing GPT/GitHub or Switch guides.

- [ ] **Step 2: Re-read the created file**

Verify that all referenced downstream paths use exact repository-relative names and that no non-existent file is referenced.

- [ ] **Step 3: Search the bootstrap for forbidden ambiguity**

Search for wording that could imply automatic cross-game reuse, automatic AI finalization, or platform assumptions without evidence. Rewrite any such wording before commit completion.

- [ ] **Step 4: Commit**

Commit message:

```text
docs: add Codex localization bootstrap entry point
```

---

### Task 2: Add standalone workflow policy documents

**Files:**
- Create: `workflow/PROJECT-OPERATING-MODEL.md`
- Create: `workflow/SOL-LUNA-AGENT-POLICY.md`
- Create: `workflow/PLAYTEST-FEEDBACK-POLICY.md`

**Interfaces:**
- Consumes: bootstrap routing rules
- Produces: project-isolation, model-delegation, and playtest-authority policies

- [ ] **Step 1: Create `PROJECT-OPERATING-MODEL.md`**

Required sections:

- one game = one project + one review program + one Drive workspace;
- Codex responsibilities versus web ChatGPT responsibilities;
- common-code reuse versus forbidden game-data reuse;
- target-project `AGENTS.md` authority;
- stage workflow and evidence recording;
- project-specific failures and successful samples as reusable local evidence;
- rule that archive knowledge never overrides real project files.

- [ ] **Step 2: Create `SOL-LUNA-AGENT-POLICY.md`**

Required sections:

- Sol 5.6 / Medium as main planner, integrator, and final reviewer;
- Luna 5.6 / XHIGH as bounded worker and reader;
- Terra excluded from default workflow;
- recommended `luna_reader` and `luna_worker` roles;
- parallel delegation only for independent tasks;
- no simultaneous writes to the same files/shared state;
- Luna escalation rule when architecture or scope decisions are required;
- Sol review of evidence and diffs before integration.

- [ ] **Step 3: Create `PLAYTEST-FEEDBACK-POLICY.md`**

Required authority order:

1. user-confirmed correction observed during real gameplay;
2. actual in-game context and dialogue evidence;
3. registered glossary, character, relationship, and speech-style rules;
4. AI analysis or proposed translation.

Also define how playtest-confirmed changes update reusable rules without automatically rewriting unrelated lines.

- [ ] **Step 4: Re-read all three files and cross-check terminology**

Verify that the same terms are used consistently for Sol, Luna, review program, Google Drive workspace, playtest correction, and project isolation.

- [ ] **Step 5: Commit**

Commit message:

```text
docs: add localization operating policies
```

---

### Task 3: Add the three-stage review policy as separate articles

**Files:**
- Create: `review/REVIEW-DATA-SCHEMA.md`
- Create: `review/REVIEW-STAGE-1.md`
- Create: `review/REVIEW-STAGE-2.md`
- Create: `review/REVIEW-STAGE-3.md`

**Interfaces:**
- Consumes: workflow authority and Google Drive review concept
- Produces: strict stage boundaries and shared review-data contract

- [ ] **Step 1: Create `REVIEW-DATA-SCHEMA.md`**

Define the shared reference files:

- `glossary.csv`
- `characters.csv`
- `relationships.csv`
- `speech_style.csv`

Require directional relationship records so `A -> B` and `B -> A` can differ.

Define final reviewed CSV requirements:

- stable row identifier;
- source text field;
- current Korean text field;
- protected structural fields preserved;
- schema/version marker where applicable;
- deterministic import into the game-specific review program;
- malformed or unknown IDs must be rejected or quarantined instead of guessed.

- [ ] **Step 2: Create `REVIEW-STAGE-1.md` as an independent article**

Opening boundary must state:

```text
현재 작업은 1차 검수다.
1차 목적만 수행하고 2차·3차의 스타일 보정 목표를 임의로 가져오지 않는다.
```

Primary goals:

- about 1,000 rows per user-visible unit;
- RSC/string-size limit checks;
- missing fields;
- control/tag/placeholder/newline damage;
- speaker/listener identification when supported;
- directed relationship and speech-level compliance;
- address rules;
- glossary consistency;
- obvious severe mistranslation or semantic inversion;
- flag uncertain rows for deeper passes;
- avoid unnecessary stylistic rewriting.

- [ ] **Step 3: Create `REVIEW-STAGE-2.md` as an independent article**

Opening boundary must state that Stage 1 structural decisions are the baseline and should not be silently overturned.

Primary goals:

- natural Korean;
- removal of literal Japanese phrasing;
- character voice;
- emotional intensity;
- scene-appropriate wording;
- dialogue flow;
- awkward syntax and repetition;
- evidence-based flagging if a Stage 1 rule appears wrong.

- [ ] **Step 4: Create `REVIEW-STAGE-3.md` as an independent article**

Opening boundary must state that this is the strict final precision pass.

Primary goals:

- about 500 rows per unit;
- precise source meaning;
- nuance and subtle mistranslation;
- nearby dialogue context;
- emotional continuity;
- foreshadowing and ambiguity;
- jokes and wordplay;
- character consistency;
- particles, word order, rhythm, readability;
- final RSC constraints;
- final CSV validity suitable for import.

- [ ] **Step 5: Verify stage isolation**

Search all three stage files and confirm:

- Stage 1 does not instruct broad naturalization or final polish;
- Stage 2 does not redefine relationship/speech-level rules without evidence;
- Stage 3 does not tell the model to ignore established common-reference data;
- each stage references common files but not another stage's instruction file.

- [ ] **Step 6: Commit**

Commit message:

```text
docs: add staged web GPT review guides
```

---

### Task 4: Add reusable templates

**Files:**
- Create: `templates/AGENTS.template.md`
- Create: `templates/glossary.template.csv`
- Create: `templates/characters.template.csv`
- Create: `templates/relationships.template.csv`
- Create: `templates/speech-style.template.csv`

**Interfaces:**
- Consumes: workflow and review policy
- Produces: copyable project-local starting templates

- [ ] **Step 1: Create `AGENTS.template.md`**

Template must include fields/sections for:

- exact game/project identity;
- allowed project root;
- forbidden neighboring projects;
- supported version/source baseline;
- Sol/Luna model policy;
- read/write boundaries;
- existing approved assets/translations that must be preserved;
- stage plan;
- required tests;
- runtime verification requirements;
- Luna escalation conditions;
- failure/evidence logging.

Use clearly marked placeholders intended for copying into a private project, but do not include personal absolute paths or secrets in the archive template.

- [ ] **Step 2: Create `glossary.template.csv`**

Header:

```csv
source_term,approved_ko,category,notes,status
```

- [ ] **Step 3: Create `characters.template.csv`**

Header:

```csv
character_id,name,aliases,personality,traits,base_speech_style,verbal_habits,notes
```

- [ ] **Step 4: Create `relationships.template.csv`**

Header:

```csv
speaker_id,listener_id,relationship,speech_level,address_rule,effective_from,effective_to,exceptions,notes
```

- [ ] **Step 5: Create `speech-style.template.csv`**

Header:

```csv
character_id,base_style,sentence_length,vocabulary_tendency,emotional_expression,avoid,approved_examples,notes
```

- [ ] **Step 6: Verify CSV parseability**

Check that every template has exactly one header row, consistent comma-separated fields, and no accidental Markdown fencing inside the file contents.

- [ ] **Step 7: Commit**

Commit message:

```text
docs: add localization project templates
```

---

### Task 5: Add a new independent README section

**Files:**
- Modify: `README.md`

**Interfaces:**
- Consumes: completed bootstrap entry point
- Produces: visible navigation entry without changing existing article contents

- [ ] **Step 1: Read current `README.md` immediately before editing**

Preserve the existing document sections and wording.

- [ ] **Step 2: Add a new standalone documentation section**

Insert a section separate from `GPT / GitHub 운용` and `Nintendo Switch 한국어 패치`.

Recommended heading:

```markdown
### Codex 한글화 프로젝트 운영
```

Recommended entry:

```markdown
- [Codex 한글화 프로젝트 부트스트랩](CODEX-LOCALIZATION-BOOTSTRAP.md)
  - 게임별 프로젝트·검수 프로그램 분리
  - GPT-5.6 Sol / Luna 역할 분담
  - Google Drive 기반 1차·2차·3차 검수 구조
  - 용어집·캐릭터·관계도·말투 기준 자료 운영
  - 최종 CSV 반영과 실제 플레이 피드백 우선순위
```

Do not fold this bullet into either existing guide description.

- [ ] **Step 3: Re-read `README.md`**

Verify the new section is visible as its own heading and that the two existing sections remain intact.

- [ ] **Step 4: Commit**

Commit message:

```text
docs: link standalone Codex localization guide
```

---

### Task 6: Final repository verification

**Files:**
- Read-only verification across all newly added documentation

**Interfaces:**
- Consumes: Tasks 1-5
- Produces: verified standalone documentation pack

- [ ] **Step 1: Re-fetch every new file from the default branch**

Required files:

```text
CODEX-LOCALIZATION-BOOTSTRAP.md
workflow/PROJECT-OPERATING-MODEL.md
workflow/SOL-LUNA-AGENT-POLICY.md
workflow/PLAYTEST-FEEDBACK-POLICY.md
review/REVIEW-DATA-SCHEMA.md
review/REVIEW-STAGE-1.md
review/REVIEW-STAGE-2.md
review/REVIEW-STAGE-3.md
templates/AGENTS.template.md
templates/glossary.template.csv
templates/characters.template.csv
templates/relationships.template.csv
templates/speech-style.template.csv
README.md
```

- [ ] **Step 2: Verify internal links**

Confirm every repository-relative Markdown link points to an existing path.

- [ ] **Step 3: Verify separation from existing articles**

Confirm no content changes were made to:

```text
GPT-GITHUB-OPERATIONS.md
switch/SWITCH-KOREAN-LOCALIZATION-GUIDE.md
```

- [ ] **Step 4: Scan for public-repository hazards**

Search new documents for:

- personal absolute paths;
- tokens/secrets/passwords;
- keys;
- complete original script dumps;
- copyrighted original game assets;
- project-specific private data presented as generic examples.

Remove any accidental matches that are real sensitive content.

- [ ] **Step 5: Scan for unfinished markers**

Search for `TODO`, `TBD`, `FIXME`, and ambiguous references to files that do not exist.

- [ ] **Step 6: Verify acceptance criteria against the spec**

Confirm that a user can now point Codex to one standalone bootstrap file and that the bootstrap routes to all required project, agent, staged-review, template, and platform knowledge without requiring the user to merge existing articles manually.

- [ ] **Step 7: Record final commit SHAs and report verified paths**

Do not report completion until the default branch has been re-read and the visible README navigation entry is confirmed.
