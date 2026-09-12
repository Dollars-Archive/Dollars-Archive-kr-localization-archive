from pathlib import Path
p = Path('CODEX-LOCALIZATION-BOOTSTRAP.md')
text = p.read_text(encoding='utf-8')
old = '''3. 대상 프로젝트에 `AGENTS.md`가 있으면 가장 먼저 읽고 그 프로젝트의 규칙을 우선합니다.\n3. 실제 프로젝트 파일과 현재 상태를 조사합니다. 다른 게임에서 성공한 방식만 보고 구조를 추정하지 않습니다.\n5. `workflow/PROJECT-OPERATING-MODEL.md`를 읽습니다.\n'''
new = '''3. 대상 프로젝트에 `AGENTS.md`가 있으면 가장 먼저 읽고 그 프로젝트의 규칙을 우선합니다.\n4. 실제 프로젝트 파일과 현재 상태를 조사합니다. 다른 게임에서 성공한 방식만 보고 구조를 추정하지 않습니다.\n5. `workflow/PROJECT-OPERATING-MODEL.md`를 읽습니다.\n'''
if text.count(old) != 1:
    raise SystemExit(f'numbering anchor count={text.count(old)}')
text = text.replace(old, new, 1)
p.write_text(text, encoding='utf-8', newline='\n')
print('fixed bootstrap numbering')
