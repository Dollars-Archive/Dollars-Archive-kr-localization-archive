# Codex 한글화 자동 부트스트랩

목표: 사용자가 매 세션마다 `CODEX-LOCALIZATION-BOOTSTRAP.md` 링크를 다시 붙여넣지 않아도, Codex에서 게임 한글화 의도를 말하면 자동으로 최신 부트스트랩을 읽게 합니다.

## 한 번만 설치

이 저장소를 내려받은 환경에서 Windows 기준:

```text
codex-auto-trigger\install-global.cmd
```

또는 PowerShell:

```powershell
powershell.exe -NoLogo -NoProfile -ExecutionPolicy Bypass -File .\codex-auto-trigger\install-global.ps1
```

설치기는 `CODEX_HOME` 환경변수가 있으면 그 경로를 우선합니다. 별도 Codex 홈을 직접 지정해야 하는 환경에서는 다음처럼 한 번만 지정할 수 있습니다.

```powershell
.\codex-auto-trigger\install-global.cmd -CodexHome "<YOUR_CODEX_HOME>"
```

설치기는 다음을 수행합니다.

- `~/.agents/skills/dollars-localization-bootstrap/`에 개인 Skill 설치
- Skill의 implicit invocation 활성화
- 설치 시점의 `CODEX-LOCALIZATION-BOOTSTRAP.md`를 fallback snapshot으로 보존
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

프로젝트 기본 상위 루트:

`D:\Codex\한글화 프로젝트`

각 작품의 `AGENTS.md`와 현재 사용자의 직접 지시가 bootstrap보다 우선합니다.
