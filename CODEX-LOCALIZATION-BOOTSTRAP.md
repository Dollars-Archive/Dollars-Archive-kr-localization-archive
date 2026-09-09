# Codex 한글화 프로젝트 부트스트랩

이 문서는 새 게임 한글화 프로젝트를 시작하거나 기존 프로젝트를 재정비할 때 Codex가 가장 먼저 읽는 **상위 진입점**입니다.

기존 `GPT-GITHUB-OPERATIONS.md` 또는 `switch/SWITCH-KOREAN-LOCALIZATION-GUIDE.md`를 대체하지 않습니다. 이 문서는 프로젝트 운영 규칙과 검수 구조를 연결하고, 실제 플랫폼과 작업 대상에 맞는 세부 문서를 선택해서 읽도록 안내합니다.

## 핵심 원칙

```text
조사 → 단일 샘플 → 실기 검증 → 전체 적용 → 자동 검증 → 변경분만 배포
```

아카이브의 문서는 범용 노하우입니다. 실제 대상 프로젝트의 파일, 현재 구현, 성공 샘플, 해시, 런타임 결과보다 우선하지 않습니다.

## Codex 작업 시작 순서

1. 현재 작업 대상 게임과 정확한 프로젝트 루트를 확인합니다.
2. 대상 프로젝트에 `AGENTS.md`가 있으면 가장 먼저 읽고 그 프로젝트의 규칙을 우선합니다.
3. 실제 프로젝트 파일과 현재 상태를 조사합니다. 다른 게임에서 성공한 방식만 보고 구조를 추정하지 않습니다.
4. `workflow/PROJECT-OPERATING-MODEL.md`를 읽습니다.
5. `workflow/SOL-LUNA-AGENT-POLICY.md`를 읽습니다.
6. 실제 플레이 기반 수정과 검수 프로그램 정책이 필요하면 `workflow/PLAYTEST-FEEDBACK-POLICY.md`를 읽습니다.
7. 번역 검수 파이프라인을 만들거나 운영할 때만 `review/` 문서를 읽습니다.
8. 플랫폼별 기술 노트는 실제 대상과 일치할 때만 선택해서 읽습니다.
   - Nintendo Switch: `switch/SWITCH-KOREAN-LOCALIZATION-GUIDE.md`
9. 이미 프로젝트에서 성공한 빌더, 샘플, 패치 방식, 승인된 번역 자산은 근거 없이 다시 설계하지 않습니다.
10. 위험한 변경은 전체 적용 전에 조사 또는 단일 대표 샘플부터 수행합니다.
11. 단일 샘플이 정적 검증뿐 아니라 실제 런타임에서 성공한 뒤에 전체로 확장합니다.
12. 게임별 데이터, 관계도, 말투, 용어집, 오프셋, 패치 규칙은 다른 게임에서 자동으로 가져오지 않습니다.
13. 산출물은 재현 가능한 도구, 테스트, manifest, 해시, 검증 기록을 남기는 방향으로 만듭니다.
14. 실제 결과를 다시 읽거나 테스트하기 전에는 완료했다고 판단하지 않습니다.

## 프로젝트 분리 원칙

기본 단위는 다음과 같습니다.

```text
게임 1개
  → Codex 한글화 프로젝트 1개
  → 게임 전용 검수 프로그램 1개
  → 게임 전용 Google Drive 검수 작업공간 1개
```

공통 코드는 재사용할 수 있지만 다음 항목은 게임별로 독립 관리합니다.

- 대사 데이터
- 용어집
- 캐릭터 이름과 성격
- 캐릭터 말투
- 화자 → 청자 관계도
- 반말/존댓말과 호칭 규칙
- 검수 이력
- 실제 플레이 확정값
- 바이너리 포맷 가정과 오프셋
- 승인된 번역과 UI 자산

## 역할 분담

Codex는 주로 **한글화 엔지니어링**을 담당합니다.

- 게임 파일/자산 분석
- 텍스트 추출·재삽입
- 폰트/UI/영상/바이너리 작업
- 빌더·패처·검증 도구 제작
- 게임별 검수 프로그램 제작
- 테스트와 정적 검증
- staging·build·release 산출물 생성
- 최종 검수 CSV 반입

대량 번역과 단계별 언어 검수는 주로 **웹 ChatGPT + Google Drive CSV**에서 수행합니다.

## 모델 운영 기본값

기본 정책은 다음과 같습니다.

- 메인: GPT-5.6 Sol / Medium
- 서브에이전트: GPT-5.6 Luna / XHIGH
- Terra: 기본 워크플로에서 사용하지 않음

세부 위임 규칙은 `workflow/SOL-LUNA-AGENT-POLICY.md`를 따릅니다.

## Google Drive 검수 구조

게임별 Drive 작업공간의 권장 구조:

```text
게임명/
├─ 00_공통기준/
│  ├─ glossary.csv
│  ├─ characters.csv
│  ├─ relationships.csv
│  └─ speech_style.csv
├─ 01_1차검수/
│  └─ INSTRUCTION_1ST.md
├─ 02_2차검수/
│  └─ INSTRUCTION_2ND.md
├─ 03_3차검수/
│  └─ INSTRUCTION_3RD.md
└─ 04_최종/
   └─ final reviewed CSV
```

각 단계는 목적이 다르므로 지시문도 물리적으로 분리합니다.

- 1차: 약 1,000행 단위의 기초공사
- 2차: 자연스러운 한국어와 캐릭터 말투 보정
- 3차: 약 500행 단위의 엄격한 최종 정밀검수

세부 규칙은 다음 문서를 사용합니다.

- `review/REVIEW-DATA-SCHEMA.md`
- `review/REVIEW-STAGE-1.md`
- `review/REVIEW-STAGE-2.md`
- `review/REVIEW-STAGE-3.md`

## 실제 플레이 피드백

AI 제안은 최종 진실로 취급하지 않습니다.

기본 우선순위:

1. 실제 게임 플레이 중 사용자가 직접 확인하고 확정한 수정
2. 게임 내 실제 문맥과 대사 근거
3. 등록된 용어집·캐릭터·관계도·말투 규칙
4. AI 분석 또는 번역 제안

세부 정책은 `workflow/PLAYTEST-FEEDBACK-POLICY.md`를 따릅니다.

## 템플릿

새 프로젝트를 만들 때 다음 템플릿을 복사해서 게임별로 채울 수 있습니다.

- `templates/AGENTS.template.md`
- `templates/glossary.template.csv`
- `templates/characters.template.csv`
- `templates/relationships.template.csv`
- `templates/speech-style.template.csv`

## 공개 저장소 주의

이 아카이브에는 다음 자료를 넣지 않습니다.

- 게임 본편 또는 원본 RomFS
- NSP/XCI/NCA
- 키 파일
- 원작 이미지·음성·영상의 대량 원본
- 전체 원문 스크립트 덤프
- 개인 PC 절대 경로
- 토큰·비밀번호·Secret
- 개인 서버나 계정 식별정보

새 프로젝트에서 얻은 노하우를 이 아카이브로 되돌릴 때는 **다른 게임에서도 재사용 가능한 원리와 실패/성공 근거만 추려서** 기록합니다.
