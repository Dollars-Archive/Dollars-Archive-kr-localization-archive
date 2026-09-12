from pathlib import Path


def replace_once(path: str, old: str, new: str) -> None:
    p = Path(path)
    text = p.read_text(encoding="utf-8")
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"{path}: expected anchor exactly once, found {count}")
    p.write_text(text.replace(old, new, 1), encoding="utf-8", newline="\n")


contract = '''# Web GPT-5.6 Sol XHIGH + DevSpace 검증 운영 계약

이 문서는 게임 한글화 프로젝트에서 **Oracle → Web GPT-5.6 Sol / XHIGH → DevSpace Tunnel** 경로를 실제 전문 실무에 사용할 때의 검증된 범위와 금지선을 고정합니다.

## 1. 검증된 실행 경로

2026-09-13 사용자 환경의 Oracle 0.20.0 기준 E2E에서 다음이 실제로 확인되었습니다.

```text
호스트 Codex 관리자
→ Oracle 0.20.0
→ ChatGPT 웹 GPT-5.6 Sol
→ Extra High / 매우 높음
→ DevSpace Tunnel
→ 승인된 정확한 프로젝트 루트
→ 파일 읽기·생성·정밀 수정·재읽기
→ 답변 로컬 회수
→ 호스트의 독립 검증
```

검증된 Oracle 지정값:

```text
--model gpt-5.6-sol
--effort extra-high
--app-name "DevSpace Tunnel"
```

실행기의 내부 브라우저 요청에서는 `model=gpt-5.6-sol`, `model_strategy=select`, `thinking_time=extra-high`가 유지되고, 실제 ChatGPT UI에서도 `GPT-5.6 Sol`과 `매우 높음` 선택이 각각 verified 상태로 확인되었습니다.

**Oracle 문서의 기본 예시가 Latest를 사용한다는 이유만으로 `GPT-5.6 Sol을 지원하지 않는다`고 판단하지 않습니다.** 지원 불가 판정은 실제 CLI 거부, 실제 모델 선택 실패, 실제 UI 미지원 또는 실행 오류처럼 관측된 근거가 있을 때만 내립니다.

이 검증은 현재 사용자 설치 환경의 성공 근거입니다. Oracle·ChatGPT UI·자동화 버전이 바뀌면 영향받은 선택/실행 경로만 재검증합니다. 다른 환경에 숫자·경로·버전을 무조건 복사하지 않습니다.

## 2. 실행 전 상태 판정

모델 선택 전에 다음 단계가 막힐 수 있습니다.

- Oracle 전용 브라우저 프로필 로그인
- 시험/실행용 프로필 복사 후 로그인 유지
- 임시채팅 개인화 확인
- ChatGPT 모델 선택기 로딩

로그인 화면이나 개인화 확인 실패를 곧바로 `모델 미지원`으로 분류하지 않습니다. 실제 실패 단계와 UI/로그 근거를 구분합니다.

호스트 관리자의 모델·추론 강도는 **사용자가 현재 선택한 값을 유지**합니다. Web Sol XHIGH를 호출한다는 이유로 호스트 Codex를 임의로 Sol XHIGH나 다른 고비용 모델로 상향하지 않습니다.

## 3. Web Sol XHIGH의 검증된 파일 작업 범위

다음 동작은 승인된 정확한 프로젝트 루트 안의 E2E에서 실제로 검증되었습니다.

| 동작 | 상태 | 운영 규칙 |
|---|---|---|
| 파일 읽기 | 검증 완료 | 프로젝트·파일 범위를 미션에 명시 |
| 새 파일 생성 | 검증 완료 | work/staging 등 승인된 경로 우선 |
| Web GPT가 생성한 파일 수정·재읽기 | 검증 완료 | 변경 후 다시 읽고 결과 반환 |
| 기존 파일 정밀 수정·재읽기 | 검증 완료 | 지정 범위만 수정하고 호스트가 diff/해시 독립 검증 |
| 답변 로컬 회수 | 검증 완료 | 회수 사실과 내용 정확성을 구분하여 판정 |
| 파일 삭제 | 기본 금지 / 보안 차단 관측 | 우회하지 않고 삭제 후보만 반환 |
| 파일 이동·이름 변경 | 미검증 / 기본 금지 | 별도 승인·검증 전에는 수행하지 않음 |

기존 파일 수정 E2E에서는 지정된 두 값만 바뀌고 식별값·줄 순서·UTF-8 BOM 없음·LF·끝 개행이 보존됐으며, 시험 대상 외 기존 파일의 결합 해시도 변하지 않는 것을 호스트가 독립 확인했습니다.

이 검증은 `모든 대량 변경이 안전하다`는 뜻이 아닙니다. 실제 작업은 여전히 `분석 → 단일 샘플 → diff/테스트 → 범위 확대` 순으로 진행합니다.

## 4. 삭제·이동·이름 변경 안전선

삭제 E2E에서는 Web GPT의 삭제 요청이 다음 보안 판정으로 차단되었습니다.

```text
요청의 보안 상태를 결정하지 못해 이 도구 요청은 OpenAI에 의해 차단되었습니다.
```

따라서 이를 `DevSpace에 삭제 기능이 없다`고 일반화하지 않지만, **현재 한글화 운영에서는 Web GPT 작업자의 삭제를 사용하지 않습니다.** 표현을 바꿔 재시도하거나 다른 도구·명령으로 우회하지 않습니다.

삭제가 필요한 작업은 Web GPT가 다음만 반환합니다.

- 삭제 후보 경로
- 삭제 이유
- 삭제 전 확인해야 할 의존성·영향

실제 삭제는 사용자 또는 별도로 승인된 호스트 경로에서 수행합니다. 이동·이름 변경도 별도 검증 전에는 같은 보수적 원칙을 적용합니다.

## 5. 미션 작성과 역할 고정

Web GPT 미션에는 다음 역할 경계를 유지합니다.

```text
당신은 이 미션을 직접 수행하도록 호출된 최종 작업 수행자다.
별도 지시가 없는 한 Oracle이나 다른 GPT를 호출하지 마라.
호스트 Codex/Oracle의 완료를 기다리지 마라.
지정된 프로젝트 자료와 허용 범위 안에서 직접 수행하고 결과를 반환하라.
직접 수행할 수 없다면 다른 작업자에게 재위임하지 말고 실제 막힌 이유와 필요한 입력만 반환하라.
```

파일 수정 작업에는 추가로 다음을 명시합니다.

- 정확한 프로젝트 루트와 허용 파일/폴더
- 수정하면 안 되는 원본·성공 자산·다른 프로젝트
- 생성/수정 허용 여부
- 삭제·이동·이름 변경 금지
- 원하는 결과와 테스트
- 결과를 남길 경로

## 6. 호출 실패와 대체 금지

정확한 Web GPT-5.6 Sol XHIGH 경로가 실패했을 때 **Codex의 로컬 Sol XHIGH나 다른 모델로 조용히 대체하지 않습니다.**

- CLI/선택기/로그인/개인화/DevSpace 중 실제 실패 단계를 보고합니다.
- `Latest` 기본 설명만으로 지원 불가라고 단정하지 않습니다.
- 자동 경로만 막힌 상당한 실무는 완성된 manual handoff를 우선 준비합니다.
- 사용자가 승인하지 않은 `Latest`, Pro, Codex Sol XHIGH, 새 유료 API 또는 새 공급자로 자동 대체하지 않습니다.

DevSpace `502` / `network_error`와 Web GPT 역할 혼동은 기존 라우팅 정책의 서로 다른 재시도 규칙을 그대로 따릅니다.

## 7. 호스트 검증 책임

Web GPT의 `완료했습니다`는 완료 증거가 아닙니다. 호스트 Codex는 작업 성격에 맞춰 다음을 독립 확인합니다.

- 실제 diff와 변경 파일
- 허용 범위 밖 변경 여부
- 필요한 파일 해시·개수·크기
- 인코딩·개행·구조 보존이 중요한 경우 그 조건
- 테스트·빌드·정적 검사
- 필요한 런타임/실기 결과
- 회수된 답변의 내용 정확성

```text
Web GPT 응답 완료 ≠ 파일 수정 검증 완료 ≠ 테스트 완료 ≠ 실제 게임 검증 완료
```

## 8. 검증 범위의 한계

현재 E2E가 직접 입증하지 않은 항목은 다음과 같습니다.

- 파일 삭제 성공
- 이동·이름 변경
- 여러 Web GPT의 동시 쓰기
- 장시간·대규모 수정의 무조건적 안정성
- 모든 Oracle/ChatGPT UI 버전에서의 동일 동작

이 항목을 검증 완료로 확대 보고하지 않습니다. 실제 작업에서는 복구 가능한 work/staging/브랜치·worktree를 우선하고, 성공 범위를 단계적으로 넓힙니다.

**한 줄 원칙: Web Sol XHIGH는 실제 파일을 읽고 만들고 기존 파일을 정밀 수정하는 주력 실무자로 사용할 수 있다. 삭제·이동·이름 변경은 기본 금지하고, Sol 관리자가 diff와 테스트를 독립 검증한 뒤 통합한다.**
'''
Path("workflow/WEB-SOL-DEVSPACE-OPERATING-CONTRACT.md").write_text(contract, encoding="utf-8", newline="\n")

policy_anchor = """## 8. DevSpace Tunnel / Web GPT 운용

Web Sol XHIGH 또는 Web GPT-6 Pro에 프로젝트 실무를 맡길 때 연결 상태를 추측하지 않습니다.
"""
policy_repl = """## 8. DevSpace Tunnel / Web GPT 운용

Web Sol XHIGH 또는 Web GPT-6 Pro에 프로젝트 실무를 맡길 때 연결 상태를 추측하지 않습니다.

Web GPT-5.6 Sol XHIGH의 실제 Oracle/DevSpace 경로, 검증된 파일 작업 범위와 삭제·이동 금지선은 `workflow/WEB-SOL-DEVSPACE-OPERATING-CONTRACT.md`를 함께 따릅니다. **Oracle의 기본 예시가 Latest를 사용한다는 이유만으로 GPT-5.6 Sol을 지원하지 않는다고 판단하지 않습니다.** 현재 검증된 지정 경로는 `gpt-5.6-sol / extra-high / select`이며, 지원 불가 판정은 실제 실행 근거가 있을 때만 내립니다.
"""
replace_once("workflow/SOL-LUNA-AGENT-POLICY.md", policy_anchor, policy_repl)

policy_unavailable = """## 15. 모델 또는 기능을 사용할 수 없을 때

- 정해진 모델/추론 강도를 다른 모델로 조용히 대체하지 않습니다.
"""
policy_unavailable_repl = """## 15. 모델 또는 기능을 사용할 수 없을 때

- 정해진 모델/추론 강도를 다른 모델로 조용히 대체하지 않습니다.
- `Latest`가 기본 경로라는 문서만 보고 Web GPT-5.6 Sol XHIGH를 미지원으로 판정하지 않습니다. CLI 거부, 실제 웹 모델 선택 실패, UI 미지원 또는 실행 오류처럼 관측된 근거를 확인합니다.
- 로그인·임시채팅 개인화 실패는 모델 미지원과 구분합니다.
- 검증된 Web Sol XHIGH 경로가 막혀도 Codex Sol XHIGH나 다른 모델로 임의 대체하지 않습니다.
"""
replace_once("workflow/SOL-LUNA-AGENT-POLICY.md", policy_unavailable, policy_unavailable_repl)

bootstrap_anchor = """DevSpace는 최고난도 문제에서만 쓰는 비상 경로가 아니라, **Web GPT-5.6 Sol XHIGH를 기본 전문 실무 책임자로 쓰기 위한 일반 실무 경로**이기도 합니다.

Web Sol XHIGH 또는 Web GPT-6 Pro에 프로젝트 작업을 맡길 때 연결 상태를 추측하지 않습니다.
"""
bootstrap_repl = """DevSpace는 최고난도 문제에서만 쓰는 비상 경로가 아니라, **Web GPT-5.6 Sol XHIGH를 기본 전문 실무 책임자로 쓰기 위한 일반 실무 경로**이기도 합니다.

Web Sol XHIGH를 실제 파일 작업에 사용할 때는 `workflow/WEB-SOL-DEVSPACE-OPERATING-CONTRACT.md`도 읽습니다. 현재 사용자 환경에서는 Oracle 0.20.0의 `gpt-5.6-sol / extra-high / select` 경로가 실제 웹 UI 선택, DevSpace 파일 읽기·생성·기존 파일 정밀 수정·재읽기·결과 회수까지 검증됐습니다. **Latest 기본 설명만으로 미지원이라 추정하지 않으며, 삭제·이동·이름 변경은 검증된 쓰기 범위에 포함하지 않습니다.**

Web Sol XHIGH 또는 Web GPT-6 Pro에 프로젝트 작업을 맡길 때 연결 상태를 추측하지 않습니다.
"""
replace_once("CODEX-LOCALIZATION-BOOTSTRAP.md", bootstrap_anchor, bootstrap_repl)

template_anchor = """### Web GPT Worker Safety

Web GPT는 최종 작업 수행자로 호출합니다. 별도 지시 없이 Oracle/다른 GPT를 재호출하거나 호스트 완료를 기다리지 않습니다.
"""
template_repl = """### Web GPT Worker Safety

Web GPT는 최종 작업 수행자로 호출합니다. 별도 지시 없이 Oracle/다른 GPT를 재호출하거나 호스트 완료를 기다리지 않습니다.

Web Sol XHIGH 파일 작업에는 아카이브의 `workflow/WEB-SOL-DEVSPACE-OPERATING-CONTRACT.md`를 적용합니다. `gpt-5.6-sol / extra-high / select`의 실제 웹 선택·DevSpace 읽기·생성·기존 파일 수정·재읽기 경로는 검증된 범위로 취급하되, 삭제·이동·이름 변경은 기본 금지합니다. Latest가 기본 예시라는 이유만으로 Sol 미지원이라고 추정하거나 로컬 Codex Sol XHIGH로 임의 대체하지 않습니다.
"""
replace_once("templates/AGENTS.template.md", template_anchor, template_repl)

skill_anchor = """- Web GPT / DevSpace / Oracle 위임은 canonical bootstrap의 최신 안전장치를 그대로 따릅니다.
"""
skill_repl = """- Web GPT / DevSpace / Oracle 위임은 canonical bootstrap의 최신 안전장치를 그대로 따릅니다.
- Web GPT-5.6 Sol XHIGH 실무 배차가 관련되면 canonical repo의 `workflow/WEB-SOL-DEVSPACE-OPERATING-CONTRACT.md`도 읽습니다. Latest 기본 예시만으로 Sol 미지원이라고 단정하지 않으며, 삭제·이동·이름 변경은 검증된 기본 쓰기 범위에 포함하지 않습니다.
"""
replace_once("codex-auto-trigger/SKILL.md", skill_anchor, skill_repl)

checks = {
    "workflow/WEB-SOL-DEVSPACE-OPERATING-CONTRACT.md": [
        "--model gpt-5.6-sol",
        "--effort extra-high",
        "파일 삭제 | 기본 금지 / 보안 차단 관측",
        "기존 파일 정밀 수정·재읽기 | 검증 완료",
    ],
    "workflow/SOL-LUNA-AGENT-POLICY.md": [
        "WEB-SOL-DEVSPACE-OPERATING-CONTRACT.md",
        "Latest`가 기본 경로라는 문서만 보고",
        "Codex Sol XHIGH나 다른 모델로 임의 대체하지 않습니다",
    ],
    "CODEX-LOCALIZATION-BOOTSTRAP.md": [
        "WEB-SOL-DEVSPACE-OPERATING-CONTRACT.md",
        "DevSpace 파일 읽기·생성·기존 파일 정밀 수정·재읽기·결과 회수",
    ],
    "templates/AGENTS.template.md": [
        "WEB-SOL-DEVSPACE-OPERATING-CONTRACT.md",
        "삭제·이동·이름 변경은 기본 금지",
    ],
    "codex-auto-trigger/SKILL.md": [
        "WEB-SOL-DEVSPACE-OPERATING-CONTRACT.md",
        "Latest 기본 예시만으로 Sol 미지원이라고 단정하지 않으며",
    ],
}
for path, needles in checks.items():
    text = Path(path).read_text(encoding="utf-8")
    for needle in needles:
        if needle not in text:
            raise SystemExit(f"{path}: missing verification anchor: {needle}")
print("policy verification passed")
