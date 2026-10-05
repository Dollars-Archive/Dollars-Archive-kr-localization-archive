---
name: dollars-localization-bootstrap
description: Use when the user starts, continues, reviews, debugs, or plans a Korean game localization, 한글화, 한글패치, translation-review, patch-engineering, or localization HD Pack task.
---

# Dollars Localization Bootstrap

이 스킬은 게임 한글화 관련 작업을 시작할 때 사용자가 GitHub 부트스트랩 링크를 매번 다시 전달하지 않아도 되도록 하는 전역 진입점입니다.

## Canonical source

항상 다음 문서를 최신 상위 규칙으로 사용합니다.

`https://github.com/Dollars-Archive/Dollars-Archive-kr-localization-archive/blob/main/CODEX-LOCALIZATION-BOOTSTRAP.md`

Raw source:

`https://raw.githubusercontent.com/Dollars-Archive/Dollars-Archive-kr-localization-archive/main/CODEX-LOCALIZATION-BOOTSTRAP.md`

## Trigger behavior

사용자가 게임 한글화 작업 의도를 나타내면 링크를 다시 요구하지 않습니다.

대표 트리거 예:

- 한글화 작업할 거야
- 이 게임 한글화 시작
- 한글패치 작업 이어서
- 번역 검수 시작
- 패처/빌더/폰트/UI 한글화 작업
- 한글화 프로젝트 디버깅
- 한글화용 HD Pack 작업

한글화와 무관한 일반 코딩·개인 작업에는 이 스킬을 적용하지 않습니다.

## Required startup

한글화 작업의 첫 관련 턴에서 구현·수정·계획에 들어가기 전에 다음을 수행합니다.

1. 가능한 GitHub/web/network 경로로 canonical bootstrap의 최신 내용을 직접 읽습니다.
2. 최신 원문을 읽을 수 있으면 그 내용을 기준으로 작업합니다.
3. 네트워크 또는 GitHub 접근이 불가능한 경우에만 이 스킬 폴더의 `CODEX-LOCALIZATION-BOOTSTRAP.snapshot.md`를 fallback으로 읽습니다.
4. snapshot fallback을 쓴 경우에만 사용자에게 최신 GitHub 원문을 읽지 못했다고 짧게 알립니다.
5. 사용자가 bootstrap URL을 다시 찾아서 제공하도록 요구하지 않습니다.

## Project root and environment

이 스킬 폴더에 `environment.md`가 있으면 작업 경로를 읽어 적용한다. `NOT_CONFIGURED`이면 첫 프로젝트 전에 작업 루트를 한 번 확인하고 해당 파일에 기록한다. 사용자가 현재 지시한 경로와 기존 프로젝트 루트가 우선한다.

문서의 `D:\Codex` 경로와 Dollars-Archive 저장소는 작성자 환경이다. 다른 사용자는 본인 경로·GitHub·Drive를 사용하며 작성자 허브·공략집 저장소에 게시하지 않는다. 검수 프로그램은 각자 게임에 맞춰 제작한다.

게임명이 정해지면 기본 폴더를 먼저 만들고 준비 완료와 `00_원본`·`08_전용_에뮬` 경로를 안내한다. 원본·포터블은 사용자가 복사한다. 기본 폴더는 `00_` → `01_` → `02_` → `03_` → `04_` → `05_` → `06_` → `07_` → `08_` 번호 순서대로 하나씩 생성하고, 마지막에 `버그 리포트`를 만든다. 테스트 롬·ISO/CSO·사용자 확인용 빌드는 모두 해당 게임의 `04_테스트 파일`에 저장한다. 최소 한글 출력, 초반 500개 대사, 이미지·동영상 자막, 통합 테스트에도 같은 저장 위치를 사용한다. 다른 작품 폴더를 수정 범위에 자동 포함하지 않는다.

## Authority

- 현재 사용자 지시가 가장 우선입니다.
- 그 다음 해당 작품의 `AGENTS.md`를 따릅니다.
- 그 다음 canonical `CODEX-LOCALIZATION-BOOTSTRAP.md`를 따릅니다.
- 이 스킬 자체는 세부 한글화 정책을 복제하지 않습니다. 최신 bootstrap을 찾아 읽게 하는 진입점 역할만 합니다.

## Important boundaries

- 기본 담당은 **사용자가 선택한 현재 모델**입니다. 평소 분석·설계·구현·디버깅·테스트는 직접 수행합니다. 사용자의 현재 모델 선택을 임의 상향하지 않습니다.
- **Web GPT는 사용자 명시 요청 시에만** 지정 범위에 호출합니다. 이 bootstrap 스킬의 자동 로드는 Web GPT 자동 호출 허가가 아닙니다.
- 사용자 지정이 없으면 Web 위임을 위한 연결 확인·로그인/맞춤화 검사·브라우저 실행·미션 작성/제출·대기·복구를 시작하지 않습니다. 일반 웹 검색·GitHub/Drive 읽기는 별개입니다.
- 상세 모델 운용은 최신 `workflow/SOL-LUNA-AGENT-POLICY.md`를 따릅니다. 낡은 snapshot/프로젝트 문구의 Web 우선·자동 배차·Sol 감독 전담을 현재 사용자 지시보다 우선하지 않습니다.
- Oracle/DevSpace 경로를 사용자가 지정한 때만 `workflow/WEB-SOL-DEVSPACE-OPERATING-CONTRACT.md`를 적용합니다. Nhahan/WebGPT 설치와 과거 Oracle E2E 기록은 별개입니다.
- 기존 Oracle·DevSpace·로그인 프로필·진행 중인 작업은 정책 변경만으로 삭제·교체·종료하지 않습니다. 실제 승인·보안·권한 확인은 유지합니다.
- Luna는 정해진 저위험 반복 보조이며 병렬 호출 의무는 없습니다. 고비용 모델을 자동 대체 투입하지 않습니다.
- 사용자가 별도로 요청하지 않은 HD Pack 제작을 자동 시작하지 않습니다.
- Codex와 GPT는 최신 부트스트랩의 16단계와 공통 작업 지시문을 따릅니다. 현재 단계·완료 근거를 기록하고, Drive 검수는 1·2·3차 모두 최대 500개 데이터 행으로 진행합니다.
- 모델 호출이나 연결을 실제 수행하지 않았다면 수행했다고 보고하지 않습니다. 사용량은 근거가 없으면 미측정입니다.
- 실제 프로젝트 상태와 관련 테스트를 확인하기 전에는 완료로 판단하지 않습니다.

## Stage handoff

4·5단계는 각각 시작 전에 Claude 의뢰 여부를 사용자에게 확인한다. 이미 해당 단계의 담당을 명시한 경우는 다시 묻지 않는다. Claude 선택 시 GPT/Codex가 의뢰용 프롬프트를 만들고 사용자가 직접 전달한다. 돌아온 분석·설계 결과를 검토한 뒤 실제 파일 수정·빌드·샘플 제작은 GPT/Codex가 수행한다. Claude를 자동 호출하거나 사용자의 선택 전에 해당 분석·샘플 작업을 시작하지 않는다.

모든 단계가 끝날 때마다 완료 보고를 한다. 이번 결과를 짧게 적고, **다음 작업 프리뷰: 단계 번호·이름, 예상 작업시간, 추천 모델·추론 강도와 간단한 이유, 필요한 준비·사용자 답변**을 함께 안내한다. 예상시간은 자료 규모와 남은 확인에 근거하고 미확정이면 조건을 밝힌다. “준비되면 말씀해 주세요” 또는 담당 선택·실기 확인 요청으로 끝낸다. 결과만 나열하고 끝내지 않는다. 추천은 모델 자동 변경·호출 허가가 아니다. 승인이나 담당 선택이 필요한 다음 단계는 사용자 답변을 받은 뒤 시작한다. 전체 16단계가 끝났으면 전체 완료를 보고하고 예정되지 않은 후속 작업을 만들지 않는다.

모든 신규·진행 중 한글화 프로젝트는 3번과 4번 사이의 3-1단계에서 전용 에뮬을 설정한다. 기본 롬 탐색·게임 목록 경로는 해당 게임의 `04_테스트 파일`로 지정하고, 공통 키보드 배치를 적용한다. 설정 분리·실제 저장 경로·재실행 후 유지 여부를 확인한 뒤 롬 분석으로 넘어간다. 이미 적용된 경우는 기록과 실제 설정을 확인하고 키보드 배치를 다시 입력하도록 요구하지 않는다. [공통 키 배치와 확인 절차](https://github.com/Dollars-Archive/Dollars-Archive-kr-localization-archive/blob/main/workflow/EMULATOR-TEST-SETUP.md)를 읽고 적용한다.

12·13·14단계는 각각 시작 전에 **“이 단계의 분석·분류 담당은 누구로 할까요? 실제 작업을 맡을 워커는 누구로 할까요?”**라고 묻고 사용자 배분을 기다린다. Claude·GPT·Codex 중 누구도 고정 담당으로 두지 않는다. 이미 해당 단계의 역할을 명시했다면 그 선택을 따르고 미정 역할만 확인한다. 선택은 다음 단계로 자동 승계하지 않는다. 역할별 작업 범위와 결과 전달 방식을 기록하고, 외부 담당을 선택하면 의뢰 프롬프트와 필요한 자료를 준비한다. Claude 의뢰는 사용자가 직접 전달하고 결과를 가져오며, 실제 작업은 사용자가 지정한 워커가 수행한다. 모델·워커를 임의로 호출하거나 바꾸지 않는다.
