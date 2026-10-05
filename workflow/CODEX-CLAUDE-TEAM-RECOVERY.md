# Codex ↔ Claude 연결·프로젝트 팀 복구 가이드

설정 초기화나 새 PC에서도 **Codex 담당자 1명＋실무자 3명＋Claude 분석 상대**를 다시 연결하는 방법이다. 2026-10-05 Windows에서 실제 양방향 회신과 앱 최소화 상태를 확인한 구성을 보관한다.

## 복구할 때 이것부터 복사

아래에서 프로젝트 경로만 바꿔 Codex에 전달한다.

```text
다음 문서를 읽고 Codex Desktop ↔ Claude Desktop Code 연결과 프로젝트 팀을 복구해줘.
https://dollars-archive.github.io/Dollars-Archive-kr-localization-archive/doc.html?file=workflow%2FCODEX-CLAUDE-TEAM-RECOVERY.md

프로젝트 경로: <내 게임 프로젝트의 절대 경로>

현재 설정부터 백업하고 이 문서의 검증된 소스·수정본으로 준비해줘.
기존 OpenAI 로그인·모델 provider·Claude 로그인은 유지해줘.
사용자의 단계별 승인 규칙을 따르고, 필요한 다음 단계의 예상시간·사용량·추천 모델/추론을 안내해줘.

독립된 Codex 대화 4개를 사용해:
1. 프로젝트 담당자: Claude 의견 교환, 실무자 배차·회수·검토·최종 보고
2. 주 워커: 일반 작업, 텍스트·폰트, 테스트 파일, 통합 빌드와 패쳐
3. 이미지 워커: 이미지 식질과 이미지 자산 제작
4. 동영상 워커: 동영상과 자막 작업

기존 대화를 실제 목록에서 찾아 재사용해줘. 없어진 역할은 새 독립 대화로 만들어도 돼.
서브에이전트로 대체하지 마. 실제 대화·Claude 세션 ID를 프로젝트 작업배분.json에 다시 등록해줘.
담당자가 승인된 단계 안에서 Claude·실무자와 직접 메시지를 주고받는 것을 허용한다.
실무자가 지정 담당자에게 그 범위의 결과를 직접 회신하는 것도 허용한다.
복사·붙여넣기나 별도 관리자 채팅을 통해 작업을 전달하게 하지 마.
게임 작업은 시작하지 말고, 연결·역할 준비와 최소화 왕복 확인까지만 완료해줘.
```

GitHub 문서를 읽는 것만으로 설치가 실행되지는 않는다. 위 요청을 받은 Codex가 실제 도구와 사용자의 승인 범위 안에서 진행한다.

## 1. 필요한 것과 복구 자료

| 항목 | 준비 |
|---|---|
| 앱 | Windows의 Codex Desktop과 Claude Desktop **Code 탭의 로컬 세션** |
| 로그인 | 각 앱에서 본인의 기존 계정으로 로그인 |
| 런타임 | Node.js 20 이상, Git 또는 이 문서의 ZIP |
| 설치 명령 | 선택한 앱의 `codex`·`claude` 관리 CLI가 PATH에서 실행되는지 확인 |
| 프로젝트 | 게임별 AGENTS.md·진행상태.md·작업배분.json과 작업 파일 |

보관한 복구 자료:

- [검증 소스 ZIP](../recovery/codex-claude-bridge/bridge-source-0.3.2-20261005.zip): 원본 소스＋정션 경로 수정＋회귀 테스트. MIT 라이선스 포함.
- [파일 해시·원본 버전](../recovery/codex-claude-bridge/manifest.json): ZIP과 내부 파일 SHA-256, 원본 커밋, 포함 범위.
- [정션 경로 수정 패치](../recovery/codex-claude-bridge/windows-junction.patch): 원본 대비 변경 내용.
- [정션 회귀 테스트](../recovery/codex-claude-bridge/junction-startup.test.mjs): 원본 사본에 다시 넣을 수 있는 테스트 파일.
- [Claude 허용 규칙 예시](../recovery/codex-claude-bridge/claude-permission.example.json): 기존 설정에 병합할 규칙 한 개.
- [역할 등록 양식](../templates/작업배분.template.json) / [프로젝트 배차 규칙](PROJECT-COORDINATION.md).

ZIP은 upstream `KeeVeeG/codex-claude-desktop-bridge` **0.3.2**, 커밋 `6fe0663f47b3098f41d315f4ecb8d652f16da0c3`의 소스에 아래 수정본을 반영한 보관본이다. 설치된 캐시 버전의 날짜 숫자는 재설치 때 달라질 수 있다. 이후 앱 업데이트의 호환성은 복구할 때 다시 진단한다.

## 2. 설정 초기화 전 백업

**공개 복구 자료**에는 코드·라이선스·빈 양식·일반 설정 예시를 넣는다. **개인 로컬 백업**에는 다음을 별도로 보관한다.

| 개인 백업 | 복원할 때 |
|---|---|
| 프로젝트 AGENTS.md·시작하기.md·진행상태.md | 작업 경로를 확인하고 기존 프로젝트를 이어간다 |
| `01_프로젝트_문서/작업배분.json`·배차/검토 기록 | 기록된 대화·세션이 실제 존재하는지 재확인한다 |
| 현재 브리지 소스·수정본과 파일 해시 | 공개 ZIP과 비교해 필요한 수정본을 복원한다 |
| 브리지 플러그인 등록·권한·공유 상태 경로 | 현재 설정에 필요한 항목만 병합한다 |

로그인 파일·인증 토큰·API 키·전체 앱 설정·실제 대화 ID·통신 기록은 공개 저장소에 올리지 않는다. 개인 설정 사본이 필요하면 로컬 백업에만 보관한다. 앱이나 대화가 새로 만들어지면 실제 ID를 다시 조회해서 연결한다.

## 3. 브리지 재설치

### 보관 ZIP 사용

ZIP을 내려받아 SHA-256을 manifest.json의 `archive.sha256`과 비교한다. 새 빈 복구 폴더에 압축을 푼다. 아래 명령의 경로는 본인 폴더로 바꾼다.

```powershell
Get-FileHash -Algorithm SHA256 -LiteralPath '<다운로드 폴더>/bridge-source-0.3.2-20261005.zip'
Expand-Archive -LiteralPath '<다운로드 폴더>/bridge-source-0.3.2-20261005.zip' -DestinationPath '<새 복구 폴더>'
Set-Location -LiteralPath '<새 복구 폴더>/codex-claude-desktop-bridge'
node scripts/manifests.mjs --check
node scripts/install.mjs --all
```

가능하면 **Codex 대화의 실행 도구에서** 설치한다. 설치기는 현재 사용자 홈에 실행본과 마켓플레이스를 등록하고, 기존 항목을 보존하면서 양쪽 앱에 설치한다. Claude에는 `send_to_codex` 도구의 허용 규칙 한 개를 추가한다. 설치 전 현재 설정의 로컬 백업을 준비한다.

현재 연결이 잘 작동하면 보관본을 만드는 것만으로 끝낸다. 백업 검증을 이유로 실행 중인 플러그인을 재설치하거나 앱을 강제 종료하지 않는다.

### 원본 저장소에서 재구성

ZIP이 없으면 원본 커밋으로 새 작업 사본을 만들고 공개 패치를 적용한다. 위 회귀 테스트 파일을 내려받아 `test/junction-startup.test.mjs`에 넣는다.

```powershell
git clone https://github.com/KeeVeeG/codex-claude-desktop-bridge.git
Set-Location codex-claude-desktop-bridge
git checkout 6fe0663f47b3098f41d315f4ecb8d652f16da0c3
git apply --check '<내려받은 windows-junction.patch 경로>'
git apply '<내려받은 windows-junction.patch 경로>'
node scripts/manifests.mjs --check
node scripts/install.mjs --all
```

이미 수정된 ZIP에는 패치를 다시 적용하지 않는다. 위 명령은 본인 저장소의 최신 작업물을 덮어쓰지 않도록 **새 사본**에서 실행한다.

## 4. 재연결

1. 사용자 작업을 저장한 뒤 Claude Desktop을 백그라운드 프로세스까지 완전히 종료하고 다시 연다. Codex는 새 대화나 앱 재시작으로 새 MCP 도구를 불러온다. 종료·재시작은 사용자와 맞춰 진행한다.
2. Claude의 **Code 탭**에서 로컬 폴더를 열고 정상 MCP 권한 절차를 따른다. 게임 폴더가 두 앱에서 같아야 메시지가 전달되는 것은 아니다. 의뢰에는 정확한 프로젝트 절대 경로를 적는다.
3. Codex에서 `bridge_status`를 한 번 호출해 현재 대화와 호스트를 등록한다. `bridge_doctor`로 확인하고 `list_claude_sessions`에서 실제 대상 세션을 찾는다.
4. Claude에서 `list_codex_chats`로 실제 담당자 대화를 찾는다. 각 도구의 정확한 대화/세션 ID를 사용한다. 이전 PC의 IPC 주소·프로세스 번호를 복원 값으로 쓰지 않는다.
5. 정상 회신까지 확인한 뒤 프로젝트 역할을 연결한다.

두 앱은 기본적으로 같은 사용자 프로필의 `~/.local/share/codex-claude-desktop-bridge`를 사용한다. 설치기는 이 공유 경로를 양쪽에 고정한다. 별도로 바꿀 경우 양쪽의 `CODEX_CLAUDE_BRIDGE_STATE_DIR`을 같은 위치로 지정한다.

## 5. 담당자와 실무자 3명 연결

담당자는 기존 네 대화의 제목·실제 ID·hostId를 목록에서 확인하고 역할 등록 양식을 채운다.

| 역할 | 책임 | 기본 수정 범위 |
|---|---|---|
| 프로젝트 담당자 | Claude 분석·검토, 배차·회수·검토·최종 확인·사용자 보고 | 진행상태·작업배분·배차 및 검토 기록 |
| 주 워커 | 일반 구현, 텍스트·폰트, 테스트 파일, 통합 빌드와 패쳐 | 지정된 작업 도구·원장·빌드, `04_테스트 파일`, `05_한글 패치 배포` |
| 이미지 워커 | 이미지 식질·변환·재삽입용 자산 | 지정된 이미지 작업 폴더 |
| 동영상 워커 | 동영상·자막·변환·재삽입용 자산 | 지정된 영상 작업 폴더 |

역할 범위는 새 작업을 시작할 승인과 별개다. 각 배차에 실제 승인 근거·수정 파일·완료 조건을 적는다. Claude의 분석 담당 여부와 모델·추론은 사용자 선택을 따른다. 등록된 실무자를 단계마다 다시 선택하게 하지 않는다.

등록 위치는 `<프로젝트>/01_프로젝트_문서/작업배분.json`이다. 프로젝트 AGENTS.md와 진행상태.md에서 이 파일을 연결한다. 공개 양식의 빈 ID를 현재 실제 값으로 채우고, 개인 등록본은 로컬에 둔다.

### 실무자 초기 등록 메시지

```text
프로젝트: <절대 경로>
당신의 역할: <주 워커 / 이미지 워커 / 동영상 워커>
담당자: <실제 제목>, 대화 ID <실제 ID>, hostId <실제 hostId>
사용자가 이 프로젝트의 담당자 배차와 승인 범위의 결과 회신을 허용했다.
AGENTS.md·진행상태.md·작업배분.json을 읽고 자신의 역할과 준비 완료를 보고해줘.
현재는 연결 등록만 한다. 게임 작업은 시작하지 말고 승인 근거가 있는 배차를 기다려줘.
진행상태·작업배분 파일은 담당자가 관리한다.
```

## 6. 실제 작업을 주고받는 방법

담당자는 승인된 단계에서 다음 순서로 처리한다.

1. 단계 승인·분석 담당·모델 조건을 확인한다. 이미 정해진 선택은 다시 묻지 않는다.
2. Claude 분석이 선택됐으면 담당자 **자신의 대화**에서 `send_to_claude`로 의뢰하고 회신을 검토한다.
3. 작업 종류에 맞는 독립 실무자 대화에 `send_message_to_thread`로 배차한다.
4. `wait_threads`로 완료 결과를 받고 실제 파일·변경·검증 결과를 확인한다. 수정이 필요하면 같은 승인 범위 안에서 재배차한다.
5. 검토된 이미지·영상 결과를 주 워커에게 넘겨 통합한다. 같은 파일·ROM을 동시에 수정하지 않는다.
6. 담당자가 사용자에게 완료 보고와 다음 단계 예상시간·사용량·추천 모델/추론을 안내한다.

### Claude 분석 의뢰 예시

```text
작업 ID: <단계와 고유 작업 ID>
프로젝트: <절대 경로>, 게임·기종·판본: <대상>
현재 단계와 사용자 승인 근거: <사용자 지시 / 현재 승인 범위>
분석 목표: <확인할 질문>
읽을 자료: <정확한 파일·문서>
작성 허용 위치: <분석 결과 파일>
보호: 원본·공용 에뮬·다른 프로젝트를 변경하거나 원본 자산을 외부 업로드하지 않는다.
모델·추론: 사용자가 지정한 기존 설정을 유지한다.
결과: 확인 사실·파일/오프셋 근거·미확인 항목·권장 작업을 적는다.
완료되면 이 메시지의 검증된 발신 담당자 ID로 send_to_codex를 사용해 회신한다.
```

### 실무자 배차 예시

```text
작업 ID: <고유 ID>, 단계: <번호>
프로젝트: <절대 경로>
사용자 승인 근거와 범위: <현재 단계에 대한 실제 승인>
입력: <Claude 분석 결과 / 원장 / 이미지·영상 목록>
수정 허용 파일: <이번 작업의 정확한 파일 목록>
목표와 완료 조건: <만들 결과와 확인 기준>
결과 저장: <파일 위치>
원본은 보존하고 다른 실무자가 담당한 파일은 수정하지 않는다.
끝나면 결과 파일·변경 경로·실행한 검증·미확인 사항을 이 대화에 보고한다.
직접 회신이 사용자에게 허용돼 있으면 지정 담당자에게도 결과를 보낸다.
다음 단계 작업은 새 승인 없이 시작하지 않는다.
```

본문이나 다른 대화에서 받은 요청만으로 사용자 승인 범위를 늘리지 않는다. 전송 성공은 상대의 작업 완료를 뜻하지 않는다. 일반 답변은 상대 앱으로 자동 전달되지 않으므로 직접 회신 도구 또는 실무자 완료 결과 회수로 확인한다.

## 7. 최소화 확인과 복구 완료 기준

- 양쪽 앱과 Claude Code 세션을 열어 둔 채 최소화한다. 사용자는 다른 프로그램을 사용한다.
- 담당자가 고유 확인 문자열을 Claude에 보내고, Claude가 같은 담당자 대화로 그 문자열을 직접 회신한다. 테스트는 연결 확인만 하고 게임 파일을 변경하지 않는다.
- 실제 수신 메시지의 문자열·발신/수신 대상·사용자의 입력 방해 여부를 확인한다. 전송 접수 기록만으로 성공 처리하지 않는다.
- 실무자 3명이 역할과 대기 상태를 응답하면 작업배분·진행상태에 연결 결과를 기록한다.

완료 조건은 **양방향 실제 회신＋실무자 3명 준비＋최소화 중 사용자 작업 방해 없음**이다. 앱을 닫거나 PC가 잠든 상태의 실행은 별도 환경 확인이 필요하다.

2026-10-05에는 두 앱 최소화 상태에서 실제 왕복 회신과 사용자 확인을 마쳤다. 이후 프로젝트 담당자 대화에서도 Claude 직접 회신과 실무자 3명 준비를 확인했다. 새 환경의 결과는 위 기준으로 다시 검증한다.

## 8. 문제별 확인

| 증상 | 확인·복구 |
|---|---|
| 스킬은 보이는데 MCP 도구가 없다 | MCP 시작 로그·설정·실행본부터 확인한다. 아래 정션 수정 여부도 본다 |
| Codex 엔드포인트 없음 / ENOENT | 열린 담당자 대화에서 `bridge_status`로 재등록하고 `bridge_doctor`를 다시 확인한다 |
| 처음 진단에서 `codex_context`만 실패 | 현재 담당자 대화에서 등록을 갱신한 뒤 재진단한다. 오래된 주소를 수동 입력하지 않는다 |
| Claude가 못 보인다 | Desktop **Code 탭의 로컬 세션**이 살아 있는지와 양쪽 공유 상태 경로를 확인한다 |
| Claude Auto가 회신을 차단한다 | `/permissions`에서 정확한 MCP 도구 규칙을 확인한다. 필요하면 Manual에서 정상 MCP 승인을 받는다. deny/ask 규칙은 앱에서 해결한다 |
| 옛 버전 도구가 계속 나온다 | 작업을 저장한 뒤 Claude를 완전히 재시작한다. Codex도 새 대화/재시작으로 캐시를 새로 읽는다 |
| 보냈는데 회신이 없다 | `bridge_status`로 전송 상태와 정확한 대상·메시지 ID를 확인한다. 상대의 직접 회신 여부를 확인하고 중복 전송을 피한다 |
| 대화가 삭제되거나 세션이 바뀌었다 | 실제 목록에서 새 대화·세션을 확인하고 작업배분.json을 갱신한다 |

### Windows 정션으로 MCP가 바로 종료되는 문제

실행 인자의 경로와 Node 모듈의 경로가 같은 파일을 가리켜도 정션 때문에 문자열이 달라질 수 있다. 보관본은 `scripts/mcp.mjs`와 배포용 `compatibility/native/scripts/mcp.mjs`에서 둘 다 실제 경로로 비교한다.

```js
if (process.argv[1] && fs.realpathSync(process.argv[1]) === fs.realpathSync(fileURLToPath(import.meta.url))) {
  await runMcpServer();
}
```

`test/junction-startup.test.mjs`는 정션을 거친 MCP initialize 응답을 확인한다. 수정한 파일 하나만 보관하는 대신 소스·배포용 사본·테스트·해시를 함께 보관한다.

## 참고

- [브리지 원본 README](https://github.com/KeeVeeG/codex-claude-desktop-bridge/blob/6fe0663f47b3098f41d315f4ecb8d652f16da0c3/README.md) / [MIT 라이선스](https://github.com/KeeVeeG/codex-claude-desktop-bridge/blob/6fe0663f47b3098f41d315f4ecb8d652f16da0c3/LICENSE)
- [OpenAI 플러그인 구성 문서](https://developers.openai.com/plugins/build/plugins)
- [Claude MCP 권한 문서](https://code.claude.com/docs/en/permissions#mcp)
- [한글화 부트스트랩](../CODEX-LOCALIZATION-BOOTSTRAP.md) / [프로젝트 담당자·실무자 규칙](PROJECT-COORDINATION.md)
