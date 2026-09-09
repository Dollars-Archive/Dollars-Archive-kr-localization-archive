# AGENTS.md Template

> 이 파일은 새 게임 한글화 프로젝트에 복사해서 사용하는 템플릿입니다.
> 공개 아카이브에는 개인 절대 경로, 토큰, 키, 비공개 원본 데이터 등을 넣지 않습니다.

## Project Identity

- Game: `<GAME_NAME>`
- Platform: `<PLATFORM>`
- Project root: `<PROJECT_ROOT>`
- Supported version/source baseline: `<VERSION_OR_BASELINE>`

## Scope Boundary

수정 허용 범위:

- `<ALLOWED_ROOT_OR_DIRS>`

수정 금지 범위:

- 다른 게임 프로젝트
- `<FORBIDDEN_NEIGHBOR_PROJECTS>`
- 원본 보존 영역
- 사용자 승인 없이 변경하면 안 되는 기존 성공 산출물

## Agent Model Policy

### Main Agent

```text
GPT-5.6 Sol / Medium
```

담당:

- 요구사항 해석
- 계획과 작업 분해
- 아키텍처/위험 판단
- Luna 위임
- 통합
- 최종 검증

### Subagents

```text
GPT-5.6 Luna / XHIGH
```

권장 역할:

- `luna_reader`: 읽기/조사 전용
- `luna_worker`: 범위가 확정된 구현/테스트

Terra는 기본 워크플로에서 사용하지 않습니다.

## Delegation Rules

- 독립 작업만 병렬 위임
- 같은 파일/같은 staging에 동시 쓰기 금지
- 새로운 아키텍처 판단이 필요하면 Luna가 Sol에게 반환
- 지정하지 않은 다른 프로젝트 탐색/수정 금지
- Luna 결과는 Sol이 diff와 테스트를 검토한 뒤 통합

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
