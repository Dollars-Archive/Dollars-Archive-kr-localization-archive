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
├─ WORKLOG.md
├─ .gitignore
└─ AGENTS.md
```

`WORKLOG.md`는 실제 공개 한국어화 작업 시작을 선언한 프로젝트에서 사용합니다. 아직 후보 조사 단계라면 생성을 보류할 수 있습니다.

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

## Public Worklog

실제 공개 한국어화 작업 시작을 선언한 프로젝트에서는 아카이브의 `workflow/PUBLIC-WORKLOG-STANDARD.md`를 따릅니다.

- 게임 저장소 루트의 `WORKLOG.md` 단일 파일을 사용합니다.
- 새 날짜 기록은 항상 맨 위에 추가합니다.
- 실제로 의미 있는 작업이 있었던 날만 기록합니다.
- README 상단에는 `🚧 한국어화 작업 진행 중` 안내와 `WORKLOG.md` 링크를 둡니다.
- 작업 내용은 일반 사용자가 이해할 수 있는 성과·진행 상황 중심으로 한 단계 추상화합니다.
- 정확한 오프셋, 함수 주소, 바이너리 재현 정보, 내부 분석·자동화 스크립트, 검수 프로그램 핵심 구현, 우회·후킹·패치 포인트 등 내부 기술 레시피는 공개하지 않습니다.
- 첫 배포 후에도 `WORKLOG.md`를 삭제하지 않고 프로젝트 제작 역사로 유지합니다.
- 새 문서를 만들 때는 `templates/WORKLOG.template.md`를 기준으로 시작합니다.

핵심 원칙은 **“성과는 공개하고, 레시피는 공개하지 않는다.”** 입니다.

이미 최종 배포가 끝난 `Dollars-Archive/eve-rebirth-terror-kr-patch`와 `Dollars-Archive/eve-ghost-enemies-kr-patch`에는 이 규칙을 소급 적용하지 않습니다.

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

### 현장 조직도

```text
GPT-5.6 Sol / High
  → 소장 / 감독관: 작업 분해, 배차, 위험 판단, 결과 검증, 최종 통합

DevSpace Tunnel + Web GPT-5.6 Sol / XHIGH
  → 분야별 과장 / 기본 전문 실무 책임자: 일반~상당 난도의 분석·구현·설계·조사·검토

GPT-5.6 Luna / XHIGH
  → 기사 / 단순 작업자: 방법이 확정된 저위험 반복·검색·정리·테스트

GPT-6 Astra / Medium
  → 외주 전문업체: 고난도 구현·디버깅

DevSpace Tunnel + Web GPT-6 Pro
  → 최고급 외부 전문가: Astra급 접근으로도 풀기 어려운 최고난도 추론
```

Terra는 기본 워크플로에서 사용하지 않습니다.

### Sol High 운영 원칙

Sol은 기본 실무자가 아니라 감독관입니다.

- 요구사항 해석
- 프로젝트 문맥 유지
- 작업 분해
- 위험도·난이도 판정
- 작업자 배차
- 결과 취합과 충돌 해결
- 실제 diff·테스트·런타임 근거 검증
- 최종 통합

`Sol이 할 수 있다`, `이미 문맥을 안다`, `금방 끝낼 수 있다`만으로 전문 실무 위임을 생략하지 않습니다. **Sol 사용량 절감은 정당한 위임 이득입니다.**

상당한 프로젝트 실무를 Sol이 직접 수행할 때는 구체적인 예외 이유가 있어야 합니다.

### 기본 실무 배차

- 일반~상당 난도의 프로젝트 실무 → **DevSpace + Web GPT-5.6 Sol XHIGH 우선**
- 단순·반복·기계·저위험 작업 → **Luna XHIGH**
- 고난도 구현·디버깅 → **Astra Medium**
- 최고난도 난제 → **DevSpace + Web GPT-6 Pro**

Luna에는 새로운 아키텍처, 애매한 바이너리 추론, 불명확한 원인 분석, 캐릭터 관계·존대·말투의 애매한 최종 판정을 맡기지 않습니다.

처음부터 Astra급 또는 Pro급 문제임이 명백하면 하위 작업자를 일부러 실패시키지 않습니다.

### Delegation Rules

- 비자명한 작업은 Sol이 직접 실행하기 전에 먼저 하위 작업으로 분해
- Web Sol XHIGH에 맡길 전문 실무가 있는지 우선 확인
- Luna로 떼어낼 안전한 기계 작업이 있는지 확인
- 독립 작업이 2개 이상이면 병렬 배차 적극 검토
- 같은 파일/같은 staging의 동시 쓰기 금지, 필요하면 순차 위임
- 같은 파일을 다룬다는 이유만으로 전체 실무를 Sol이 독점하지 않음
- 다른 모델의 결과는 Sol이 실제 diff와 테스트를 검토한 뒤 통합
- Web GPT 실무를 맡길 때 DevSpace 연결 상태를 추측하지 말고 `open_workspace` 실제 호출 후 판정
- Web GPT 자동 전달이 불가능하면 완성된 manual handoff 프롬프트를 준비
- 상당한 작업을 Sol 혼자 수행했다면 결과 보고에 위임하지 않은 구체적 이유 기록

### Web GPT Worker Safety

Web GPT는 최종 작업 수행자로 호출합니다. 별도 지시 없이 Oracle/다른 GPT를 재호출하거나 호스트 완료를 기다리지 않습니다.

Web Sol XHIGH 파일 작업에는 아카이브의 `workflow/WEB-SOL-DEVSPACE-OPERATING-CONTRACT.md`를 적용합니다. `gpt-5.6-sol / extra-high / select`의 실제 웹 선택·DevSpace 읽기·생성·기존 파일 수정·재읽기 경로는 검증된 범위로 취급하되, 삭제·이동·이름 변경은 기본 금지합니다. Latest가 기본 예시라는 이유만으로 Sol 미지원이라고 추정하거나 로컬 Codex Sol XHIGH로 임의 대체하지 않습니다.

계정 로그인·MFA·계정 전환·계정 전역 메모리/개인화·앱/권한/OAuth 설정은 사용자만 처리합니다. 반면 Oracle이 소유한 **현재 임시채팅 탭의 맞춤화/개인화 상태 확인과, 정확한 비활성 제어 1개를 식별했을 때 그 임시채팅 안에서만 활성화하는 동작**은 계정 전역 설정 변경이 아니며 검증된 `ensureTemporaryChatPersonalization` 계열 helper가 자동 처리할 수 있습니다. `chatgpt-workspace-setup` 또는 다른 스킬의 `user handles account personalization` 문구를 이 임시채팅 토글까지 확대해석하여 사용자에게 매 run 수동 조작을 요구하지 않습니다. 정확한 제어가 없거나 모호하거나 로그인/MFA/계정 수준 변경이 필요할 때만 자동 조작을 중단하고 사용자에게 실제 막힌 지점을 요청합니다.

역할 혼동·자기 재호출·호스트 대기·중첩 락·무의미한 반환은 동일 미션 자동 위임을 1회에서 종료하고 manual handoff로 전환합니다.

DevSpace `502` / `network_error`는 별도 연결 장애 규칙에 따라 최소 1분 간격 최대 5회 재시도합니다.

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
