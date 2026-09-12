from pathlib import Path

path = Path("CODEX-LOCALIZATION-BOOTSTRAP.md")
text = path.read_text(encoding="utf-8")

old_flow = '''```text
1. 이 문서를 읽는다
2. 정확한 대상 프로젝트 루트를 확인한다
3. 프로젝트 AGENTS.md와 현재 상태를 읽는다
4. 실제 파일과 기존 성공 자산을 조사한다
5. Sol High가 소장처럼 작업을 분해하고 위험도·난이도를 판단한다
6. 비자명한 전문 실무는 DevSpace + Web GPT-5.6 Sol XHIGH를 기본 책임자로 배차하고, 안전한 단순 작업만 Luna에 배차한다
7. 고난도 구현·디버깅은 Astra, 최고난도 난제는 DevSpace + Web GPT-6 Pro로 올린다
8. Sol High가 작업자 결과를 재검증하고 충돌을 해결해 최종 통합한다
9. 실제 결과를 확인하기 전에는 완료라고 보고하지 않는다
```
'''
new_flow = '''```text
1. 이 문서를 읽는다
2. 대상 게임이 신규 프로젝트인지 기존 프로젝트인지 판정한다
3. 신규 프로젝트라면 다른 조사·추출·문서 작성보다 먼저 D:\\Codex\\한글화 프로젝트\\<게임명> 전용 폴더를 생성하고 그 폴더를 프로젝트 루트로 고정한다
4. 기존 프로젝트라면 현재 프로젝트 루트를 그대로 사용하고 폴더 구조를 소급 재편하지 않는다
5. 프로젝트 AGENTS.md와 현재 상태를 읽는다
6. 실제 파일과 기존 성공 자산을 조사한다
7. Sol High가 소장처럼 작업을 분해하고 위험도·난이도를 판단한다
8. 비자명한 전문 실무는 DevSpace + Web GPT-5.6 Sol XHIGH를 기본 책임자로 배차하고, 안전한 단순 작업만 Luna에 배차한다
9. 고난도 구현·디버깅은 Astra, 최고난도 난제는 DevSpace + Web GPT-6 Pro로 올린다
10. Sol High가 작업자 결과를 재검증하고 충돌을 해결해 최종 통합한다
11. 실제 결과를 확인하기 전에는 완료라고 보고하지 않는다
```
'''
if text.count(old_flow) != 1:
    raise SystemExit(f"basic flow anchor count={text.count(old_flow)}")
text = text.replace(old_flow, new_flow, 1)

anchor = '''아카이브의 문서는 범용 노하우입니다. 실제 대상 프로젝트의 파일, 현재 구현, 성공 샘플, 해시, 런타임 결과보다 우선하지 않습니다.\n\n---\n\n## 최초 한글 출력의 필수 합격 관문: 다음 장면까지 진행되는가\n'''
section = '''아카이브의 문서는 범용 노하우입니다. 실제 대상 프로젝트의 파일, 현재 구현, 성공 샘플, 해시, 런타임 결과보다 우선하지 않습니다.\n\n---\n\n## 신규 프로젝트는 게임 전용 폴더부터 만든다\n\n대상 게임이 정해졌고 아직 해당 게임의 한글화 프로젝트 루트가 없다면, **실제 조사·추출·문서 작성·도구 제작을 시작하기 전에 먼저 게임 전용 프로젝트 폴더를 생성합니다.**\n\n기본 경로:\n\n```text\nD:\\Codex\\한글화 프로젝트\\<게임명>\n```\n\n예:\n\n```text\nD:\\Codex\\한글화 프로젝트\\이상한 환상향 로터스 Lotus Labyrinth\n```\n\n게임명이 확정된 시점부터 이 폴더를 해당 작품의 **유일한 로컬 작업 루트**로 취급합니다. 이후 그 게임에 속하는 다음 자료는 원칙적으로 이 프로젝트 루트 안에서 생성·관리합니다.\n\n- 조사 메모와 분석 보고서\n- 프로젝트 문서와 `AGENTS.md`\n- 추출·변환·재삽입 작업 자료\n- `work` / analysis / staging 성격의 중간 산출물\n- 빌더·패처·검증 도구와 테스트 자료\n- 게임 전용 검수 프로그램 및 그 설정·기준자료\n- 빌드·패치·배포 준비 산출물\n- 런타임·실기 검증 기록과 실패/성공 증거\n\n**프로젝트 폴더를 만들기 전에 바탕화면, 사용자 홈, 공용 임시 작업 폴더, 다른 게임 프로젝트 안에 게임별 작업물을 먼저 만들어 흩뿌리지 않습니다.** 도구나 운영체제가 내부적으로 사용하는 일시적 캐시/임시파일은 예외지만, 재사용할 프로젝트 산출물이나 증거는 반드시 게임 전용 루트로 회수해 관리합니다.\n\n다른 게임의 프로젝트 폴더를 임시 작업장으로 빌려 쓰지 않습니다. 공통 코드나 범용 문서를 참조할 수는 있지만, 게임별 `work`, staging, 원장, 검수 프로그램, 빌드 결과, 테스트 기록을 서로 섞지 않습니다.\n\n기존 프로젝트가 이미 존재하면 이 규칙을 이유로 폴더를 새로 만들거나 이름을 바꾸거나 구조를 강제 재배치하지 않습니다. **신규 프로젝트 생성 시점부터 적용하고, 기존 프로젝트는 현재 루트를 그대로 존중합니다.**\n\n---\n\n## 최초 한글 출력의 필수 합격 관문: 다음 장면까지 진행되는가\n'''
if text.count(anchor) != 1:
    raise SystemExit(f"section anchor count={text.count(anchor)}")
text = text.replace(anchor, section, 1)

old_start = '''## Codex 작업 시작 순서\n\n1. 현재 작업 대상 게임과 정확한 프로젝트 루트를 확인합니다.\n2. 대상 프로젝트에 `AGENTS.md`가 있으면 가장 먼저 읽고 그 프로젝트의 규칙을 우선합니다.\n'''
new_start = '''## Codex 작업 시작 순서\n\n1. 현재 작업 대상 게임이 신규인지 기존인지 확인합니다.\n2. 신규 게임이고 프로젝트 루트가 아직 없으면 **다른 실작업보다 먼저** `D:\\Codex\\한글화 프로젝트\\<게임명>` 폴더를 생성하고 그 경로를 프로젝트 루트로 고정합니다. 기존 프로젝트라면 현재 루트를 그대로 사용합니다.\n3. 대상 프로젝트에 `AGENTS.md`가 있으면 가장 먼저 읽고 그 프로젝트의 규칙을 우선합니다.\n'''
if text.count(old_start) != 1:
    raise SystemExit(f"start anchor count={text.count(old_start)}")
text = text.replace(old_start, new_start, 1)
# Renumber the remaining list items in this section only, 3..16 -> 4..17.
start = text.index(new_start) + len(new_start)
end = text.index('\n---\n\n## 프로젝트 분리 원칙', start)
body = text[start:end]
for n in range(16, 2, -1):
    body = body.replace(f"\n{n}. ", f"\n{n+1}. ")
text = text[:start] + body + text[end:]

old_sep = '''## 프로젝트 분리 원칙\n\n기본 단위는 다음과 같습니다.\n'''
new_sep = '''## 프로젝트 분리 원칙\n\n로컬 작업도 게임별 전용 루트를 먼저 만들고 그 안에서 분리합니다. 신규 프로젝트의 기본 루트는 `D:\\Codex\\한글화 프로젝트\\<게임명>`이며, 한 게임의 조사·문서·work·검수 프로그램·테스트·산출물을 다른 게임 프로젝트와 섞지 않습니다.\n\n기본 단위는 다음과 같습니다.\n'''
if text.count(old_sep) != 1:
    raise SystemExit(f"separation anchor count={text.count(old_sep)}")
text = text.replace(old_sep, new_sep, 1)

old_summary = '''```text\nSol High 소장이 프로젝트를 파악하고 작업을 분해·배차한다\n→ 최초 한글 출력 때 가로폭·줄 수·[n]·반각/전각과 다음 장면 진행을 시험하고 착수 조건을 정한다\n'''
new_summary = '''```text\n신규 게임이면 먼저 D:\\Codex\\한글화 프로젝트\\<게임명> 전용 폴더를 만들고 모든 로컬 작업을 그 안에서 시작한다\n→ Sol High 소장이 프로젝트를 파악하고 작업을 분해·배차한다\n→ 최초 한글 출력 때 가로폭·줄 수·[n]·반각/전각과 다음 장면 진행을 시험하고 착수 조건을 정한다\n'''
if text.count(old_summary) != 1:
    raise SystemExit(f"summary anchor count={text.count(old_summary)}")
text = text.replace(old_summary, new_summary, 1)

for required in [
    '## 신규 프로젝트는 게임 전용 폴더부터 만든다',
    'D:\\Codex\\한글화 프로젝트\\<게임명>',
    '프로젝트 폴더를 만들기 전에 바탕화면',
    '기존 프로젝트는 현재 루트를 그대로 존중합니다',
    '다른 게임 프로젝트와 섞지 않습니다',
]:
    if required not in text:
        raise SystemExit(f"missing required phrase: {required}")

path.write_text(text, encoding="utf-8", newline="\n")
print("patched bootstrap new-project root policy")
