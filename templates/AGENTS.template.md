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

사용자가 HD Pack 제작 또는 가능성 분석을 명시적으로 요청한 경우에는 작업 전에 아카이브의 `workflow/HD-PACK-PIPELINE.md`를 읽습니다.

기본 전략:

```text
ROM/ISO 내부 자산 우선 추출
→ 작은 샘플로 구조 검증
→ 베이스 자산 HD화
→ 에뮬레이터 texture dump/hash와 매칭
→ 이후 실제 플레이에서는 신규 dump만 증분 처리
```

PS2에서는 PCSX2 Texture Replacement를 대표 예로 사용하고, 다른 플랫폼에서는 해당 에뮬레이터의 덤프/교체 규칙을 직접 확인합니다.

HD Pack 분석 단계(Stage A)에서는 사용자의 별도 승인이 없는 한 대량 업스케일, 전체 팩 제작, FMV 재인코딩, 장시간 플레이/대량 dump 수집, 원본 ROM/ISO 수정 또는 실행 파일 패치를 하지 않습니다.

## Font Selection

새 한글 폰트를 선택하거나 기존 폰트를 교체해야 하면 아카이브의 `workflow/FONT-SELECTION-POLICY.md`를 읽습니다.

기본 후보 검색처:

```text
https://font.emulog.app/#fonts
```

먼저 게임의 실제 폰트 규격을 확인합니다.

- 셀/타일 폭과 높이
- 실제 표시 픽셀 크기
- BPP / 팔레트 / 알파
- 고정폭/가변폭
- 글리프 수와 인코딩
- 아틀라스/텍스처 배치 방식
- 줄 높이, 자간, 베이스라인
- 용량/VRAM/바이너리 제약

그 뒤 기술적으로 맞는 폰트 후보를 가능하면 약 3개 추립니다.

각 후보는 같은 문구, 같은 픽셀 크기, 같은 화면 조건으로 소량 샘플을 만들어 사용자에게 비교 제시합니다.
사용자가 직접 최종 폰트를 선택하기 전에는 전체 폰트 교체나 대량 반영을 하지 않습니다.

- Font candidate A: `<FONT_A>`
- Font candidate B: `<FONT_B>`
- Font candidate C: `<FONT_C>`
- User-approved font: `<APPROVED_FONT_OR_NONE>`
- Approved font spec: `<CELL_SIZE_BPP_ENCODING_ETC>`

기술적으로 유효한 후보가 3개 미만이면 억지로 수를 채우지 않습니다.
사용자가 확정한 폰트는 이후 AI가 취향 판단만으로 임의 변경하지 않습니다.

## Pre-Translation Baseline Gate

대량 대사 번역 또는 검수 프로그램의 본 번역 기준자료 등록 전에 `review/PRE-TRANSLATION-SETUP.md`를 읽습니다.

**용어집·캐릭터·관계·말투를 먼저 세팅하고 번역을 시작합니다.**

- Pre-translation baseline status: `<NOT_STARTED / IN_PROGRESS / READY>`
- Glossary readiness: `<STATUS>`
- Character names/personality readiness: `<STATUS>`
- Speech-style readiness: `<STATUS>`
- Relationship/honorific readiness: `<STATUS>`
- Unresolved/HOLD count or reference: `<VALUE_OR_PATH>`

최소 준비 항목:

- 주요 캐릭터 이름·별칭·칭호
- 주요 반복 용어
- 캐릭터 성격과 기본 말투
- 화자 → 청자 방향 관계
- 반말/존댓말
- 호칭
- 근거 출처와 확정 상태

캐릭터 이름은 사용자 확정값과 공식 자료를 우선합니다. 공식 자료가 일본어뿐이고 한국어 표기가 애매하면 나무위키를 참고하고, 부족하면 일본 위키·팬 위키·사전·작품 자료를 교차 확인합니다. 그래도 불명확하면 HOLD합니다.

캐릭터 성격·말투는 실제 일본어 대사와 공식 소개, 매뉴얼·설정집·당시 연재 기사·인터뷰·특집 자료를 우선하고 나무위키와 일본 위키를 보조 자료로 사용합니다.

일본어판과 영어판이 함께 있으면 일본어 원문을 대사·용어·말투·존대·호칭의 기준으로 사용합니다. 영어판은 보조자료입니다.

검수 패스의 기본 작업 단위는 고정합니다.

```text
1차: 전체 대사집을 1,000행 단위로 기초 검수
2차: 1차 결과 전체를 다시 1,000행 단위로 자연화·말투 검수
3차: 2차 결과 전체를 다시 500행 단위로 최종 정밀검수
```

각 차수는 서로 다른 행 구간이 아니라 전체 대사집을 다시 검수하는 별도 패스입니다.

## Scope Boundary

수정 허용 범위:

- `<ALLOWED_ROOT_OR_DIRS>`

수정 금지 범위:

- 다른 게임 프로젝트
- `<FORBIDDEN_NEIGHBOR_PROJECTS>`
- 원본 보존 영역
- 사용자 승인 없이 변경하면 안 되는 기존 성공 산출물
- 사용자가 승인하지 않은 최종 폰트 대량 적용
- 사용자가 요청하지 않은 `05_HD Pack` 실제 제작 작업
- 0단계 핵심 기준자료가 비어 있는데 대량 번역을 완료 상태로 진행하는 것

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
- `<APPROVED_FONT_IF_ANY>`

## Stage Workflow

기본 흐름:

```text
조사 → 단일 샘플 → 런타임 검증 → 전체 적용 → 자동 검증 → 변경분만 배포
```

번역·검수 파이프라인은 별도로 다음 고정 단위를 사용합니다.

```text
0단계 기준자료 구축
→ 1차 1,000행 단위
→ 2차 1,000행 단위
→ 3차 500행 정밀검수
```

현재 프로젝트에 필요한 엔지니어링 Stage를 아래에 정의합니다.

1. `<STAGE_1>`
2. `<STAGE_2>`
3. `<STAGE_3>`

HD Pack이 사용자에게 별도로 승인된 경우에도 번역/패치 Stage와 구분해서 관리합니다.
HD Pack 자체의 Stage와 증분 처리 규칙은 `workflow/HD-PACK-PIPELINE.md`를 따릅니다.

폰트 작업은 `규격 조사 → 후보 약 3개 → 동일 조건 샘플 → 사용자 선택 → 전체 반영` 순서로 진행합니다.

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

본 번역 전에 용어집·캐릭터·관계·말투 기준을 먼저 구축하고, 이후 전체 데이터에 대해 1차 1,000행 → 2차 1,000행 → 3차 500행 정밀검수를 진행합니다.

Codex는 기준자료의 프로젝트 등록/스키마 검증, 최종 검수 CSV의 반입, 구조 검증, 빌드 및 실제 패치 적용을 담당합니다.

폰트 최종 선택은 사용자가 승인하며, HD Pack 제작은 번역 검수의 자동 후속 단계가 아닙니다. 사용자 요청이 있을 때만 별도 작업으로 시작합니다.
