# 한글화 프로젝트 전체 라이프사이클 구현 계획

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 신규 게임 한글화의 실제 작업 순서를 `전용 6폴더 생성 → 기술 분석/한글 출력 → 진행 안전성 게이트 → 전체 원문 추출·row_key·카테고리화 → 게임 전용 검수 프로그램 → 번역 전 0단계 → Google Drive 검수 작업장 → 1·2·3차 검수 → 최종 누적 CSV 반입 → 모드/실기 검증`으로 일관되게 고정한다.

**Architecture:** `CODEX-LOCALIZATION-BOOTSTRAP.md`를 최상위 실행 순서로 두고, `workflow/PROJECT-OPERATING-MODEL.md`가 로컬 프로젝트/검수 프로그램/Google Drive의 역할을 세분화한다. `review/PRE-TRANSLATION-SETUP.md`는 0단계의 선행조건을 원문 원장·분류·검수 프로그램까지 확장하고, `templates/AGENTS.template.md`는 신규 프로젝트가 같은 폴더·단계·Drive 게이트를 기록하도록 한다.

**Tech Stack:** Markdown 정책 문서, GitHub Contents API, 정적 문자열/구조 검증

**Spec:** `docs/superpowers/specs/2026-09-13-localization-project-lifecycle-design.md`

## Global Constraints

- 신규 프로젝트 루트는 `D:\Codex\한글화 프로젝트\<게임명>`이다.
- 신규 프로젝트 공통 필수 폴더는 `01_프로젝트_문서`, `02_한글화_작업`, `03_검수_프로그램`, `04_최종_배포`, `05_HD Pack`, `버그 리포트` 여섯 개다.
- `05_HD Pack`은 폴더만 만들고 사용자 명시 요청 전 실제 제작을 시작하지 않는다.
- 기존 프로젝트는 이 변경을 이유로 강제 재배치하지 않는다.
- 최소 한글 출력 성공 후 `[n]`, 반각/전각, 가로폭, 최대 줄 수, RSC/인코딩, 다음 대사/장면 진행을 검증하기 전 대량 번역을 시작하지 않는다.
- 기술 게이트 통과 후 전체 일본어 원문을 추출하고 안정 `row_key`, `category`, `subcategory`를 가진 원장을 만든다.
- 용어집 최종화 전에 게임 전용 검수 프로그램을 준비한다. 기본 기능은 `D:\Codex\# 검수 프로그램\EVE 고스트 에너미즈`, 카테고리화 방식은 `D:\Codex\# 검수 프로그램\이상한 환상향 로터스 라비린스`를 참고하되 게임별 데이터는 섞지 않는다.
- 관계/존대는 `A → B`와 `B → A`를 독립 관리한다.
- Google Drive PC 동기화 루트는 `F:\내 드라이브\검수 프로그램`이며 게임별 실사용 구조는 `01_최신_용어집`, `02_검수_필수파일`, `03_검수_수정_CSV`다.
- Drive는 PC 없이 휴대폰/웹 ChatGPT에서 검수하기 위한 실사용 작업장이다. 로컬 초안만으로 0단계 완료나 1차 시작 가능을 선언하지 않는다.
- 검수 단계는 전체 데이터를 1차 1,000행 → 2차 1,000행 → 3차 500행으로 각각 다시 훑는다.
- 3차 완료 후 핵심 반입물은 `<게임약칭>_최종대사_수정_누적.csv` 하나이며 게임 전용 검수 프로그램 최신 원장에 적용해 모드/패치와 실기 검증으로 이어간다.

---

### Task 1: 최상위 부트스트랩 순서 재정의

**Files:**
- Modify: `CODEX-LOCALIZATION-BOOTSTRAP.md`

**Interfaces:**
- Consumes: 승인된 lifecycle spec
- Produces: 모든 신규/기존 프로젝트가 읽는 단일 최상위 실행 순서

- [ ] **Step 1:** 현재 신규 프로젝트/초기 런타임/Google Drive 섹션을 찾아 기존 규칙과 충돌 지점을 확인한다.
- [ ] **Step 2:** 신규 프로젝트 6폴더를 필수 베이스로 명시하고 추가 폴더는 필요 시 생성 대상으로 분리한다.
- [ ] **Step 3:** 최소 한글 출력 → 기술 안전성 게이트 → 전체 원문 추출 → row_key → category/subcategory → 게임 전용 검수 프로그램 → 0단계의 순서를 명시한다.
- [ ] **Step 4:** Google Drive 구조를 `F:\내 드라이브\검수 프로그램\<게임명>\01_최신_용어집|02_검수_필수파일|03_검수_수정_CSV`로 교체하고 Drive 등록/재조회 전 1차 시작 금지를 하드 게이트로 둔다.
- [ ] **Step 5:** 최종 누적 CSV 반입 → 모드/패치 → 실기 검증 흐름을 추가한다.

### Task 2: 프로젝트 운영 모델 정합화

**Files:**
- Modify: `workflow/PROJECT-OPERATING-MODEL.md`

**Interfaces:**
- Consumes: Task 1의 상위 순서
- Produces: 로컬 6폴더 역할, 검수 프로그램 선행 구축, Drive 역할 구분

- [ ] **Step 1:** 기존 `.github/docs/source/staging/tests/tools/work` 기본 구조를 공통 필수 구조로 취급하지 않도록 바꾼다.
- [ ] **Step 2:** 6개 필수 폴더의 역할을 명시하고 추가 폴더는 프로젝트별 선택사항으로 둔다.
- [ ] **Step 3:** 전체 원문·안정 원장·카테고리화·검수 프로그램이 0단계 언어 기준자료보다 선행한다는 점을 추가한다.
- [ ] **Step 4:** EVE 검수 프로그램과 로터스 카테고리화 참고 경계를 명시한다.
- [ ] **Step 5:** 로컬 엔지니어링/검수 프로그램과 Google Drive 휴대폰 검수 작업장의 역할을 분리한다.

### Task 3: 번역 전 0단계의 선행조건 교정

**Files:**
- Modify: `review/PRE-TRANSLATION-SETUP.md`

**Interfaces:**
- Consumes: 기술 게이트 결과, 전체 원문 원장, category/subcategory, 게임 전용 검수 프로그램
- Produces: 0단계 언어 기준자료와 Drive 등록 전 합격 게이트

- [ ] **Step 1:** `용어집부터 만든다`로 오해할 수 있는 흐름을 `기술 게이트 + 원장/분류/검수 프로그램 이후 언어 기준자료`로 교정한다.
- [ ] **Step 2:** 관계는 방향별 비대칭 반말/존댓말·호칭을 정상 케이스로 명시한다.
- [ ] **Step 3:** Drive 세 폴더 등록, 동기화, 재조회까지 끝나야 1차 검수가 가능하도록 완료 조건을 추가한다.
- [ ] **Step 4:** Drive 미등록 상태는 `LOCAL_DRAFT_ONLY` 또는 `DRIVE_REGISTRATION_PENDING`으로 남기고 완료 처리 금지를 명시한다.

### Task 4: 신규 AGENTS 템플릿 정합화

**Files:**
- Modify: `templates/AGENTS.template.md`

**Interfaces:**
- Consumes: Tasks 1-3의 정책
- Produces: 새 게임 프로젝트마다 실제 단계/루트/Drive 준비 상태를 기록하는 프로젝트 규칙

- [ ] **Step 1:** Standard Project Layout을 6개 필수 폴더로 교체한다.
- [ ] **Step 2:** lifecycle 상태 필드에 기술 게이트, 원장 추출, row_key, 분류, 검수 프로그램, 0단계, Drive readiness를 추가한다.
- [ ] **Step 3:** Drive 루트와 3개 폴더 역할, 최종 누적 CSV 반입 규칙을 추가한다.
- [ ] **Step 4:** 기존 프로젝트에는 강제 재배치하지 않는 경계를 유지한다.

### Task 5: 전체 문서 정합성 검증

**Files:**
- Verify: `CODEX-LOCALIZATION-BOOTSTRAP.md`
- Verify: `workflow/PROJECT-OPERATING-MODEL.md`
- Verify: `review/PRE-TRANSLATION-SETUP.md`
- Verify: `templates/AGENTS.template.md`

**Interfaces:**
- Produces: 서로 모순되지 않는 canonical lifecycle

- [ ] **Step 1:** 네 문서에 6폴더 구조가 동일하게 표현되는지 확인한다.
- [ ] **Step 2:** `기술 게이트 → 전체 원문/row_key/분류 → 검수 프로그램 → 0단계 → Drive` 순서가 모두 보존되는지 확인한다.
- [ ] **Step 3:** `F:\내 드라이브\검수 프로그램`, 세 Drive 폴더, 1000/1000/500, 최종 누적 CSV 규칙을 검색 검증한다.
- [ ] **Step 4:** 예전 `.github/docs/source/staging/tests/tools/work` 구조가 신규 공통 필수 구조로 남아 있지 않은지 확인한다.
- [ ] **Step 5:** `git diff --check` 또는 동등한 whitespace 검사를 통과시키고 변경 파일을 재조회한다.
- [ ] **Step 6:** 임시 적용 스크립트/워크플로를 사용했다면 최종 main에서 제거됐는지 확인한다.
