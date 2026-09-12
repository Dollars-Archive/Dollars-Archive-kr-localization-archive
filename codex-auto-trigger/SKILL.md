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

## Project root

기본 한글화 상위 루트는 다음입니다.

`D:\Codex\한글화 프로젝트`

사용자가 작품을 지정했다면 해당 작품 폴더를 대상으로 합니다. 정확한 대상 작품이 불명확할 때만 작품명 또는 프로젝트 경로를 확인합니다.

다른 작품 폴더를 자동으로 수정 범위에 포함하지 않습니다.

## Authority

- 현재 사용자 지시가 가장 우선입니다.
- 그 다음 해당 작품의 `AGENTS.md`를 따릅니다.
- 그 다음 canonical `CODEX-LOCALIZATION-BOOTSTRAP.md`를 따릅니다.
- 이 스킬 자체는 세부 한글화 정책을 복제하지 않습니다. 최신 bootstrap을 찾아 읽게 하는 진입점 역할만 합니다.

## Important boundaries

- 사용자가 별도로 요청하지 않은 HD Pack 제작을 자동 시작하지 않습니다.
- Web GPT / DevSpace / Oracle 위임은 canonical bootstrap의 최신 안전장치를 그대로 따릅니다.
- Web GPT-5.6 Sol XHIGH 실무 배차가 관련되면 canonical repo의 `workflow/WEB-SOL-DEVSPACE-OPERATING-CONTRACT.md`도 읽습니다. Latest 기본 예시만으로 Sol 미지원이라고 단정하지 않으며, 삭제·이동·이름 변경은 검증된 기본 쓰기 범위에 포함하지 않습니다.
- ChatGPT 계정 로그인/MFA, 계정 전환, 계정 전역 메모리·개인화, 앱·권한·OAuth 설정은 사용자만 처리합니다.
- 위 계정 수준 경계와 Oracle이 소유한 **현재 임시채팅 탭의 맞춤화 확인·활성화**를 혼동하지 않습니다. 정확한 비활성 제어가 하나로 식별되면 검증된 temporary-chat helper가 그 임시채팅 안에서만 자동 활성화·확인할 수 있으며, 이를 계정 전역 개인화 변경으로 취급하거나 사용자에게 매 run 수동 토글을 요구하지 않습니다.
- 임시채팅 제어가 없거나 모호하거나 로그인/MFA/계정 설정 변경이 필요할 때만 자동 조작을 멈추고 사용자에게 실제 막힌 지점을 요청합니다.
- 모델 호출이나 연결을 실제로 수행하지 않았다면 수행했다고 보고하지 않습니다.
- 실제 프로젝트 상태와 테스트를 확인하기 전에는 완료로 판단하지 않습니다.
