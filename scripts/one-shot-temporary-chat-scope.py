from pathlib import Path


def replace_once(path: str, old: str, new: str) -> None:
    p = Path(path)
    text = p.read_text(encoding="utf-8")
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"{path}: expected anchor exactly once, found {count}")
    p.write_text(text.replace(old, new, 1), encoding="utf-8", newline="\n")


scope_rule = """계정 로그인·MFA·계정 전환·계정 전역 메모리/개인화·앱/권한/OAuth 설정은 사용자만 처리합니다. 반면 Oracle이 소유한 **현재 임시채팅 탭의 맞춤화/개인화 상태 확인과, 정확한 비활성 제어 1개를 식별했을 때 그 임시채팅 안에서만 활성화하는 동작**은 계정 전역 설정 변경이 아니며 검증된 `ensureTemporaryChatPersonalization` 계열 helper가 자동 처리할 수 있습니다. `chatgpt-workspace-setup` 또는 다른 스킬의 `user handles account personalization` 문구를 이 임시채팅 토글까지 확대해석하여 사용자에게 매 run 수동 조작을 요구하지 않습니다. 정확한 제어가 없거나 모호하거나 로그인/MFA/계정 수준 변경이 필요할 때만 자동 조작을 중단하고 사용자에게 실제 막힌 지점을 요청합니다."""

bootstrap_anchor = """Web Sol XHIGH를 실제 파일 작업에 사용할 때는 `workflow/WEB-SOL-DEVSPACE-OPERATING-CONTRACT.md`도 읽습니다. 현재 사용자 환경에서는 Oracle 0.20.0의 `gpt-5.6-sol / extra-high / select` 경로가 실제 웹 UI 선택, DevSpace 파일 읽기·생성·기존 파일 정밀 수정·재읽기·결과 회수까지 검증됐습니다. **Latest 기본 설명만으로 미지원이라 추정하지 않으며, 삭제·이동·이름 변경은 검증된 쓰기 범위에 포함하지 않습니다.**
"""
replace_once(
    "CODEX-LOCALIZATION-BOOTSTRAP.md",
    bootstrap_anchor,
    bootstrap_anchor + "\n" + scope_rule + "\n",
)

policy_anchor = """Web GPT-5.6 Sol XHIGH의 실제 Oracle/DevSpace 경로, 검증된 파일 작업 범위와 삭제·이동 금지선은 `workflow/WEB-SOL-DEVSPACE-OPERATING-CONTRACT.md`를 함께 따릅니다. **Oracle의 기본 예시가 Latest를 사용한다는 이유만으로 GPT-5.6 Sol을 지원하지 않는다고 판단하지 않습니다.** 현재 검증된 지정 경로는 `gpt-5.6-sol / extra-high / select`이며, 지원 불가 판정은 실제 실행 근거가 있을 때만 내립니다.
"""
replace_once(
    "workflow/SOL-LUNA-AGENT-POLICY.md",
    policy_anchor,
    policy_anchor + "\n" + scope_rule + "\n",
)

template_anchor = """Web Sol XHIGH 파일 작업에는 아카이브의 `workflow/WEB-SOL-DEVSPACE-OPERATING-CONTRACT.md`를 적용합니다. `gpt-5.6-sol / extra-high / select`의 실제 웹 선택·DevSpace 읽기·생성·기존 파일 수정·재읽기 경로는 검증된 범위로 취급하되, 삭제·이동·이름 변경은 기본 금지합니다. Latest가 기본 예시라는 이유만으로 Sol 미지원이라고 추정하거나 로컬 Codex Sol XHIGH로 임의 대체하지 않습니다.
"""
replace_once(
    "templates/AGENTS.template.md",
    template_anchor,
    template_anchor + "\n" + scope_rule + "\n",
)

# The canonical contract and auto-trigger skill were updated immediately before this
# one-shot. Assert those guards are present so the project-wide wording stays aligned.
contract = Path("workflow/WEB-SOL-DEVSPACE-OPERATING-CONTRACT.md").read_text(encoding="utf-8")
skill = Path("codex-auto-trigger/SKILL.md").read_text(encoding="utf-8")
for label, text in [("contract", contract), ("auto-trigger", skill)]:
    if "임시채팅" not in text or "계정" not in text:
        raise SystemExit(f"{label}: temporary-chat/account scope guard missing")

for path in [
    "CODEX-LOCALIZATION-BOOTSTRAP.md",
    "workflow/SOL-LUNA-AGENT-POLICY.md",
    "templates/AGENTS.template.md",
]:
    text = Path(path).read_text(encoding="utf-8")
    if "매 run 수동 조작" not in text:
        raise SystemExit(f"{path}: scope clarification missing")
