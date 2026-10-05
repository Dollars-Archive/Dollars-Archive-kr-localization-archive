# Codex–Claude Bridge 복구 자료

설치·복구·배차 설명은 [Codex ↔ Claude 연결·프로젝트 팀 복구 가이드](../../workflow/CODEX-CLAUDE-TEAM-RECOVERY.md)를 읽는다.

- `bridge-source-0.3.2-20261005.zip`: upstream 커밋 `6fe0663f47b3098f41d315f4ecb8d652f16da0c3`에 로컬 정션 수정과 회귀 테스트를 반영한 소스 보관본.
- `windows-junction.patch`: 같은 upstream 커밋 대비 두 MCP 시작 파일의 수정.
- `junction-startup.test.mjs`: ZIP에도 포함된 정션 시작 회귀 테스트의 별도 사본.
- `manifest.json`: 소스 출처, 포함 범위, ZIP·내부 파일 SHA-256.
- `claude-permission.example.json`: Claude 기존 설정에 병합할 허용 규칙 예시. 설정 전체를 이 파일로 교체하지 않는다.

ZIP은 소스·테스트·MIT 라이선스를 보관한다. `.git`, 설치 캐시, 개인 설정, 로그인, 통신 기록, 실제 프로젝트 역할 등록본은 포함하지 않는다. 설정 초기화 후 설치기는 본인의 현재 홈 경로에 실행본을 새로 등록한다.

이 자료 작성 과정에서는 실행 중인 앱을 재설치하거나 종료하지 않는다. 검증은 별도 임시 압축 해제 사본에서 수행한다.
