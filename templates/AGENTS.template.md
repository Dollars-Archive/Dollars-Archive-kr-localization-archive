# AGENTS.md Template

> 이 파일은 새 게임 한글화 프로젝트에 복사해서 사용하는 템플릿입니다.
> 새 작품은 기본적으로 `D:\Codex\한글화 프로젝트\<작품 폴더명>` 아래에 둡니다.
> 공개 아카이브에는 토큰, 키, 비공개 원본 데이터 등을 넣지 않습니다.

## Project Identity

- Game: `<GAME_NAME>`
- Platform: `<PLATFORM>`
- Project root: `D:\Codex\한글화 프로젝트\<PROJECT_FOLDER>`
- Supported version/source baseline: `<VERSION_OR_BASELINE>`

## Standard Project Layout

기본 구조는 `이상한 환상향 로터스 Lotus Labyrinth` 프로젝트를 기준으로 합니다.

```text
<PROJECT_ROOT>/
├─ .github/
├─ docs/
├─ source/
├─ staging/
├─ tests/
├─ tools/
├─ work/
├─ .gitignore
└─ AGENTS.md
```

PS3 및 그보다 이전 세대 작품은 다음 폴더를 추가로 준비합니다.

```text
05_HD Pack/
```

**HD Pack은 폴더만 준비합니다. 사용자가 명시적으로 HD Pack 제작을 요청하기 전에는 텍스처 덤프, 업스케일, 이미지 재가공 또는 교체 작업을 시작하지 않습니다.**

- HD Pack requested by user: `<YES_OR_NO>`
- HD Pack status: `<NOT_STARTED_OR_STATUS>`

## Scope Boundary

수정 허용 범위:

- `<ALLOWED_ROOT_OR_DIRS>`

수정 금지 범위:

- 다른 게임 프로젝트
- `<FORBIDDEN_NEIGHBOR_PROJECTS>`
- 원본 보존 영역
- 사용자 승인 없이 변경하면 안 되는 기존 성공 산출물
- 사용자가 요청하지 않은 `05_HD Pack` 실제 제작 작업

## Agent Model Policy

### Main Agent

```text
GPT-5.6 Sol / High
```

담당:

- 요구사항 해석
- 계획과 작업 분해
- 아키텍처/위험 판단
- 난이도 판정과 모델 배차
- 결과 통합
- 최종 검증

### Routed Workers

```text
GPT-6 Astra / Medium
  → 고난도 구현·디버깅

GPT-5.6 Luna / XHIGH
  → 단순·반복·범위가 확정된 구현/조사/테스트

Web GPT XHIGH
  → Luna에는 어렵고 Sol High에는 과한 독립 작업

DevSpace Tunnel + Web GPT 6 Pro
  → 매우 깊은 추론이 필요한 난제
```

Terra는 기본 워크플로에서 사용하지 않습니다.

## Delegation Rules

- 모델을 많이 쓰는 것 자체를 목표로 하지 않음
- Sol High가 바로 처리하는 편이 낫다면 위임하지 않음
- 처음부터 고난도이면 Luna를 억지로 먼저 실패시키지 않고 Astra를 고려
- 독립 작업만 병렬 위임
- 같은 파일/같은 staging에 동시 쓰기 금지
- 새로운 아키텍처 판단이 필요하면 Luna가 Sol에게 반환
- 지정하지 않은 다른 프로젝트 탐색/수정 금지
- 다른 모델의 결과는 Sol이 실제 diff와 테스트를 검토한 뒤 통합
- Web GPT가 필요하면 DevSpace 연결 상태를 추측하지 말고 `open_workspace` 실제 호출 후 판정
- Web GPT 자동 전달이 불가능하면 사용자가 그대로 보낼 수 있는 완성 의뢰문을 준비

## Existing Approved Assets / Decisions

보존해야 할 기존 성공 결과를 기록합니다.

- `<APPROVED_ITEM_1>`
- `<APPROVED_ITEM_2>`

## Stage Workflow

기본 흐름:

```text
조사 → 단일 샘플 → 런타임 검증 → 전체 적용 → 자동 검증 → 변경분만 배포
```

현재 프로젝트에 필요한 Stage를 아래에 정의합니다.

1. `<STAGE_1>`
2. `<STAGE_2>`
3. `<STAGE_3>`

HD Pack이 사용자에게 별도로 승인된 경우에도 번역/패치 Stage와 구분해서 관리합니다.

## Required Tests

- `<STATIC_TEST>`
- `<BUILD_TEST>`
- `<RUNTIME_TEST>`

## Runtime Verification

정적 검증만으로 완료 판정하지 않습니다.

확인 환경:

- `<RUNTIME_TARGET_1>`
- `<RUNTIME_TARGET_2>`

## Failure / Evidence Log

각 실패 또는 성공 샘플에는 가능하면 다음을 남깁니다.

- 대상 파일/기능
- 시도한 방법
- 결과
- 해시/크기/로그 등 재검증 근거
- 롤백 기준
- 다음 작업 입력값

## Translation Review Boundary

대량 언어 검수는 웹 ChatGPT + 게임별 Google Drive 작업공간을 기본으로 합니다.

Codex는 최종 검수 CSV의 반입, 구조 검증, 빌드 및 실제 패치 적용을 담당합니다.

HD Pack 제작은 번역 검수의 자동 후속 단계가 아닙니다. 사용자 요청이 있을 때만 별도 작업으로 시작합니다.
