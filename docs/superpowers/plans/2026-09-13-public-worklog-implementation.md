# Public Localization Worklog Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 새로 시작하거나 현재 진행 중인 게임 한국어화 프로젝트에 공개용 `WORKLOG.md`를 표준 구성으로 추가할 수 있게 아카이브의 운영 문서·템플릿·Pages 안내를 연결한다.

**Architecture:** `workflow/PUBLIC-WORKLOG-STANDARD.md`를 공개 운영 규칙의 단일 기준으로 두고, `templates/WORKLOG.template.md`를 실제 복사용 템플릿으로 제공한다. `CODEX-LOCALIZATION-BOOTSTRAP.md`와 `templates/AGENTS.template.md`는 해당 표준을 참조하도록 연결하고, 아카이브 README와 Pages 문서 목록에서 사용자가 쉽게 찾을 수 있게 노출한다.

**Tech Stack:** Markdown, GitHub repository contents, GitHub Pages static viewer (`docs/assets/app.js`)

**Spec:** `docs/superpowers/specs/2026-09-13-public-worklog-design.md`

## Global Constraints

- 게임별 공개 작업일지는 루트의 `WORKLOG.md` **단일 파일**을 사용한다.
- 최신 날짜 항목을 항상 위에 추가한다.
- 실제로 의미 있는 작업이 있었던 날만 기록한다.
- 공개 내용은 사용자 관점의 성과·진행상황 중심으로 작성한다.
- 정확한 메모리 주소, 오프셋, 함수 주소, 바이너리 재현 정보, 내부 분석·자동화 스크립트, 검수 프로그램 핵심 구현, 우회·후킹·패치 포인트 등 제작 노하우는 공개하지 않는다.
- 원칙 문구는 **“성과는 공개하고, 레시피는 공개하지 않는다.”**로 유지한다.
- README에는 실제 작업이 시작된 프로젝트만 `🚧 한국어화 작업 진행 중` 안내와 `WORKLOG.md` 링크를 둔다.
- 첫 배포 후에도 `WORKLOG.md`는 프로젝트 제작 역사로 유지한다.
- 아직 실제 작업이 시작되지 않은 후보 저장소에는 진행 중 표시를 넣지 않는다.
- 기존 진행 프로젝트에 소급 적용할 때는 과거 기록을 억지로 복원하지 않고 적용 시점부터 기록한다.
- **`Dollars-Archive/eve-rebirth-terror-kr-patch`와 `Dollars-Archive/eve-ghost-enemies-kr-patch`는 이미 최종 패치가 배포된 프로젝트이므로 이 작업의 소급 적용 대상에서 명시적으로 제외한다. 두 저장소의 README/WORKLOG 구조를 변경하지 않는다.**
- 현재 저장소에 존재하지 않는 진행 중 게임 프로젝트는 임의로 새 GitHub 저장소를 만들지 않는다. 해당 게임 저장소가 준비되거나 사용자가 연결한 뒤 표준을 적용한다.

---

### Task 1: 공개 Worklog 운영 표준 작성

**Files:**
- Create: `workflow/PUBLIC-WORKLOG-STANDARD.md`
- Reference: `docs/superpowers/specs/2026-09-13-public-worklog-design.md`

**Interfaces:**
- Consumes: 승인된 설계문서의 공개/비공개 경계와 단일 `WORKLOG.md` 운영 원칙
- Produces: Bootstrap, AGENTS 템플릿, README, Pages가 참조할 공개 운영 규칙

- [ ] **Step 1: 설계문서의 핵심 요구사항을 다시 읽는다**

확인 항목:

```text
단일 WORKLOG.md
최신 날짜 우선
README 진행 중 선언
성과 공개 / 레시피 비공개
배포 후 역사 보존
기존 프로젝트는 적용 시점부터
EVE 두 저장소 소급 적용 제외
```

- [ ] **Step 2: `workflow/PUBLIC-WORKLOG-STANDARD.md`를 작성한다**

문서에는 최소 다음 섹션을 포함한다.

```text
목적
적용 대상 / 제외 대상
README 진행 중 선언 표준 문구
WORKLOG.md 기본 형식
공개 가능한 내용
공개 금지 내용
상태 표기
기존 프로젝트 적용 규칙
배포 후 운영
Pages 연동 원칙
```

EVE 예외는 저장소명까지 정확히 적는다.

- [ ] **Step 3: 공개 금지 목록을 설계문서와 대조한다**

아래 항목이 빠지지 않았는지 확인한다.

```text
오프셋 / 주소 / 함수 주소
재현 가능한 바이너리 구조
내부 스크립트
검수 프로그램 핵심 구현
우회 / 후킹 / 패치 포인트
비공개 툴 설정
개인정보 / 키 / 토큰 / 비공개 경로
저작권상 공개 불가 원본 데이터
```

- [ ] **Step 4: 파일을 재조회하여 기준 문구와 EVE 제외 규칙을 검증한다**

Expected:

```text
“성과는 공개하고, 레시피는 공개하지 않는다.” 존재
두 EVE 저장소명이 제외 대상으로 존재
WORKLOG.md 단일 파일 원칙 존재
```

- [ ] **Step 5: 커밋한다**

```bash
git add workflow/PUBLIC-WORKLOG-STANDARD.md
git commit -m "docs: add public localization worklog standard"
```

### Task 2: 실제 복사용 WORKLOG 템플릿 추가

**Files:**
- Create: `templates/WORKLOG.template.md`
- Reference: `workflow/PUBLIC-WORKLOG-STANDARD.md`

**Interfaces:**
- Consumes: 공개 Worklog 표준
- Produces: 새 게임 프로젝트 루트에 복사할 `WORKLOG.md` 초안

- [ ] **Step 1: 최소 템플릿을 작성한다**

템플릿은 아래 구조를 사용한다.

```md
# 작업일지

> 이 문서는 한국어 패치 제작 진행 상황을 기록합니다.
> 세부 분석 방법 및 내부 제작 노하우는 공개하지 않습니다.

---

## YYYY-MM-DD

### 오늘 한 작업
- 한국어화 작업 시작

### 진행 상황
🟡 작업 진행 중

### 다음 목표
- 다음 공개 목표를 기록
```

- [ ] **Step 2: 템플릿에 비공개 정보 입력을 유도하는 필드가 없는지 검사한다**

금지 예:

```text
Offset:
Function address:
Hook point:
Internal script:
Private path:
```

Expected: 없음.

- [ ] **Step 3: 템플릿을 재조회해 제목·날짜·상태·다음 목표 섹션을 확인한다**

- [ ] **Step 4: 커밋한다**

```bash
git add templates/WORKLOG.template.md
git commit -m "docs: add public worklog template"
```

### Task 3: Codex 부트스트랩에 Worklog 적용 규칙 연결

**Files:**
- Modify: `CODEX-LOCALIZATION-BOOTSTRAP.md`
- Reference: `workflow/PUBLIC-WORKLOG-STANDARD.md`

**Interfaces:**
- Consumes: 공개 Worklog 표준과 템플릿
- Produces: 새 한글화 프로젝트 착수 시 Worklog 적용 여부를 판단하는 부트스트랩 규칙

- [ ] **Step 1: `CODEX-LOCALIZATION-BOOTSTRAP.md` 최신본을 다시 가져온다**

동시 수정을 보호하기 위해 현재 blob SHA를 새로 확인한다.

- [ ] **Step 2: `Codex 작업 시작 순서`에 Worklog 표준 확인 단계를 추가한다**

추가 의미:

```text
실제 공개 작업 시작을 선언하는 프로젝트라면 workflow/PUBLIC-WORKLOG-STANDARD.md를 읽고 WORKLOG.md/README 진행 중 표시를 준비한다.
후보 조사 단계라면 생성하지 않는다.
최종 배포 완료된 EVE rebirth terror / EVE ghost enemies에는 소급 적용하지 않는다.
```

- [ ] **Step 3: 프로젝트 분리/운영 설명에 공개 제작일지 항목을 추가한다**

게임별 독립 관리 항목에 `공개 작업일지(WORKLOG.md)`를 추가하되, 기술 내부기록과 동일시하지 않는다고 명시한다.

- [ ] **Step 4: 수정 파일을 재조회하여 기존 모델 라우팅·검수 규칙이 훼손되지 않았는지 확인한다**

Expected:

```text
기존 1차 1,000행 / 2차 1,000행 / 3차 500행 유지
기존 모델 라우팅 정책 유지
Worklog 표준 링크 추가
EVE 두 프로젝트 제외 문구 존재
```

- [ ] **Step 5: 커밋한다**

```bash
git add CODEX-LOCALIZATION-BOOTSTRAP.md
git commit -m "docs: connect public worklog to localization bootstrap"
```

### Task 4: AGENTS 템플릿에 프로젝트별 Worklog 운영 규칙 추가

**Files:**
- Modify: `templates/AGENTS.template.md`
- Reference: `workflow/PUBLIC-WORKLOG-STANDARD.md`
- Reference: `templates/WORKLOG.template.md`

**Interfaces:**
- Consumes: Worklog 공개 표준
- Produces: 각 새 게임 프로젝트의 로컬 작업 규칙에 포함될 Worklog 지침

- [ ] **Step 1: `templates/AGENTS.template.md` 최신본을 다시 가져온다**

- [ ] **Step 2: Standard Project Layout에 `WORKLOG.md`를 추가한다**

예상 구조:

```text
<PROJECT_ROOT>/
├─ .github/
├─ docs/
├─ source/
├─ staging/
├─ tests/
├─ tools/
├─ work/
├─ WORKLOG.md
├─ .gitignore
└─ AGENTS.md
```

단, 실제 프로젝트가 공개 작업 시작 전 후보 단계라면 `WORKLOG.md` 생성을 보류할 수 있다는 설명을 바로 덧붙인다.

- [ ] **Step 3: `Public Worklog` 섹션을 추가한다**

반드시 포함할 규칙:

```text
workflow/PUBLIC-WORKLOG-STANDARD.md 준수
최신 날짜가 위
의미 있는 작업일만 기록
README에 진행 중 선언 + WORKLOG 링크
성과 중심으로 추상화
내부 기술 레시피 금지
배포 후 삭제 금지
```

- [ ] **Step 4: 템플릿을 재조회해 기존 Scope Boundary와 HD Pack 규칙이 보존됐는지 확인한다**

- [ ] **Step 5: 커밋한다**

```bash
git add templates/AGENTS.template.md
git commit -m "docs: add public worklog rules to project template"
```

### Task 5: 아카이브 README와 Pages 문서 목록에 Worklog 표준 노출

**Files:**
- Modify: `README.md`
- Modify: `docs/assets/app.js`
- Reference: `workflow/PUBLIC-WORKLOG-STANDARD.md`

**Interfaces:**
- Consumes: 공개 Worklog 표준 문서
- Produces: GitHub README와 Pages 허브에서 접근 가능한 사용자 링크

- [ ] **Step 1: `README.md`와 `docs/assets/app.js` 최신본을 다시 가져온다**

- [ ] **Step 2: README 문서 목록에 `공개 작업일지 운영 표준` 항목을 추가한다**

설명에는 아래 세 가지를 강조한다.

```text
게임별 WORKLOG.md 단일 파일
README의 작업 진행 중 선언
성과 공개 / 제작 노하우 비공개
```

링크는 Pages viewer를 사용한다.

```text
https://dollars-archive.github.io/Dollars-Archive-kr-localization-archive/doc.html?file=workflow%2FPUBLIC-WORKLOG-STANDARD.md
```

- [ ] **Step 3: Pages `docs` 배열에 Worklog 표준 카드 하나를 추가한다**

권장 메타데이터:

```js
{
  group: 'PROJECT / WORKLOG',
  title: '공개 작업일지 운영 표준',
  file: 'workflow/PUBLIC-WORKLOG-STANDARD.md',
  description: '진행 중 프로젝트의 공개 제작일지와 노하우 비공개 경계를 관리하는 표준.',
}
```

- [ ] **Step 4: 파일을 재조회해 링크·경로 오타를 확인한다**

Expected:

```text
README Pages URL 정상
app.js file 경로가 workflow/PUBLIC-WORKLOG-STANDARD.md와 정확히 일치
기존 문서 카드 4개가 그대로 유지되고 새 카드만 추가
```

- [ ] **Step 5: 커밋한다**

```bash
git add README.md docs/assets/app.js
git commit -m "docs: expose public worklog standard"
```

### Task 6: 최종 검증과 적용 범위 확인

**Files:**
- Verify: `workflow/PUBLIC-WORKLOG-STANDARD.md`
- Verify: `templates/WORKLOG.template.md`
- Verify: `CODEX-LOCALIZATION-BOOTSTRAP.md`
- Verify: `templates/AGENTS.template.md`
- Verify: `README.md`
- Verify: `docs/assets/app.js`
- Must NOT modify: `Dollars-Archive/eve-rebirth-terror-kr-patch/*`
- Must NOT modify: `Dollars-Archive/eve-ghost-enemies-kr-patch/*`

**Interfaces:**
- Consumes: Tasks 1-5의 최종 결과
- Produces: 새/진행 중 프로젝트에만 적용 가능한 검증된 Worklog 표준

- [ ] **Step 1: 여섯 대상 파일을 모두 재조회한다**

모든 파일이 main 최신본에 존재하는지 확인한다.

- [ ] **Step 2: 아카이브 전체에서 Worklog 표준 연결을 점검한다**

확인 문자열:

```text
PUBLIC-WORKLOG-STANDARD.md
WORKLOG.template.md
WORKLOG.md
성과는 공개하고, 레시피는 공개하지 않는다.
```

- [ ] **Step 3: EVE 두 저장소가 이번 구현에서 변경되지 않았는지 확인한다**

구현 시작 직전의 두 EVE 저장소 main SHA를 기록하고, 최종 검증 시 동일한지 확인한다.

Expected: 두 SHA 모두 변경 없음.

- [ ] **Step 4: 아카이브 Pages 배포를 확인한다**

`pages build and deployment`에서 최종 구현 커밋의 build / report-build-status / deploy가 모두 `success`인지 확인한다.

- [ ] **Step 5: 최종 결과를 보고한다**

보고 내용:

```text
새 표준 문서 경로
새 WORKLOG 템플릿 경로
Bootstrap / AGENTS 연결 여부
README / Pages 노출 여부
Pages 배포 성공 여부
EVE 두 저장소 미변경 확인
최종 커밋 SHA
```
