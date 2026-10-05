# Codex 한글화 자동 부트스트랩

목표: 사용자가 매 세션마다 `CODEX-LOCALIZATION-BOOTSTRAP.md` 링크를 다시 붙여넣지 않아도, Codex에서 게임 한글화 의도를 말하면 자동으로 최신 부트스트랩을 읽게 합니다.

## 복사해서 Codex에 설치 요청

[부트스트랩 맨 아래 설치 프롬프트](https://github.com/Dollars-Archive/Dollars-Archive-kr-localization-archive/blob/main/CODEX-LOCALIZATION-BOOTSTRAP.md#다른-사용자용-설치시작)를 복사해 붙인다. Windows용 설치기이며, 작업 루트는 본인 경로로 설정한다. 일반 GPT와 Windows 외 환경은 같은 문서의 설치 없이 시작하는 프롬프트를 사용한다.

## 한 번만 설치

이 저장소를 내려받은 환경에서 Windows 기준:

```text
codex-auto-trigger\install-global.cmd
```

또는 PowerShell:

```powershell
powershell.exe -NoLogo -NoProfile -ExecutionPolicy Bypass -File .\codex-auto-trigger\install-global.ps1 -ProjectRoot "C:\한글화 프로젝트"
```

설치기는 `CODEX_HOME` 환경변수가 있으면 그 경로를 우선합니다. 별도 Codex 홈을 직접 지정해야 하는 환경에서는 다음처럼 한 번만 지정할 수 있습니다.

```powershell
.\codex-auto-trigger\install-global.cmd -CodexHome "<YOUR_CODEX_HOME>"
```

설치기는 다음을 수행합니다.

- `~/.agents/skills/dollars-localization-bootstrap/`에 개인 Skill 설치
- Skill의 implicit invocation 활성화
- 설치 시점의 `CODEX-LOCALIZATION-BOOTSTRAP.md`를 fallback snapshot으로 보존
- `environment.md`에 본인 작업 루트를 기록. 재설치 시 경로를 지정하지 않으면 기존 값을 유지
- 선택된 Codex 홈의 `AGENTS.md` 또는 기존 `AGENTS.override.md`에 관리 블록 1개 추가
- 기존 파일이 있으면 수정 전 백업 생성
- 설치 후 블록/Skill/snapshot을 다시 읽어 자체 검증

설치 후 Codex를 새 세션으로 시작합니다.

## 이후 사용

링크는 필요 없습니다. 예:

```text
한글화 작업할 거야. 가디언 엔젤 프로젝트 시작해.
```

```text
이 게임 한글패치 이어서 작업해.
```

```text
번역 검수 프로그램 작업하자.
```

Codex는 한글화 의도를 감지하면 `dollars-localization-bootstrap` Skill을 읽고, 최신 canonical bootstrap을 GitHub에서 먼저 읽습니다.

Canonical bootstrap:

`https://github.com/Dollars-Archive/Dollars-Archive-kr-localization-archive/blob/main/CODEX-LOCALIZATION-BOOTSTRAP.md`

GitHub 접근이 불가능한 경우에만 설치 당시 snapshot을 사용하고 그 사실을 사용자에게 알립니다.

## 범위

이 자동 트리거는 게임 한글화/한글패치/번역 검수/한글화 엔지니어링에만 적용합니다. 일반 코딩이나 다른 Codex 작업에는 개입하지 않습니다.

프로젝트 상위 루트는 설치할 때 `-ProjectRoot`로 선택한다. 지정하지 않으면 첫 프로젝트 전에 한 번 확인한다. 작성자의 `D:\Codex`를 다른 사용자 기본 경로로 적용하지 않는다. 검수 프로그램은 각자 제작한다.

각 작품의 `AGENTS.md`와 현재 사용자의 직접 지시가 bootstrap보다 우선합니다.

## 설치 확인과 시험

설치 출력의 Skill·Global instructions·Local environment 경로를 다시 읽어 확인한다. 새 세션에서는 `$dollars-localization-bootstrap`을 직접 지정해 시험할 수도 있다.

설치기는 로그인·인증·config.toml을 수정하지 않는다. 기존 스킬과 지시문은 백업하며, 자동 읽기 블록은 하나만 유지한다. 잘못된 중복 블록은 파일 변경 전에 중단한다.

개발용 격리 시험은 `-SourceDirectory <이 저장소>`·`-SkillDirectory <시험 스킬 폴더>`·`-CodexHome <시험 홈>`을 모두 지정한다. 보통 설치에는 이 세 옵션이 필요하지 않다.

설치 위치와 지시문 읽기 방식은 [공식 스킬 안내](https://learn.chatgpt.com/docs/build-skills)와 [AGENTS.md 안내](https://learn.chatgpt.com/docs/agent-configuration/agents-md)를 따른다.
