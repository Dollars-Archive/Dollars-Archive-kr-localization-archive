from pathlib import Path
import hashlib

EXPECTED = {
    'CODEX-LOCALIZATION-BOOTSTRAP.md': 'e0acc9129aac680a13c6b987b9d227a50b39f8b7',
    'workflow/SOL-LUNA-AGENT-POLICY.md': '15d4ee26c5b0c527f32185b354bf188bd863a084',
    'workflow/PROJECT-OPERATING-MODEL.md': 'b373340f934af66355cd1683a119bd29baf95243',
    'workflow/WEB-SOL-DEVSPACE-OPERATING-CONTRACT.md': '2e48a4d20d93f1516918827a799e048fa7c24994',
    'templates/AGENTS.template.md': '4a64359801d809ca5f56e3458528967c1816fedf',
    'codex-auto-trigger/SKILL.md': '1451aa68da9e28d640f9a5cb2557f992c91bd5a3',
    'codex-auto-trigger/agents/openai.yaml': '5678f808073f2782f87f39466f21d62074e96d32',
    'README.md': 'ba5ea47f43cf956120bc96c447bae0fe88d2b71b',
}

def blob_sha(data):
    return hashlib.sha1(b'blob ' + str(len(data)).encode('ascii') + b'\0' + data).hexdigest()

def once(text, old, new):
    if text.count(old) != 1:
        raise ValueError(f'Expected one exact anchor: {old[:100]!r}; got {text.count(old)}')
    return text.replace(old, new, 1)

def span(text, start, end, replacement):
    if text.count(start) != 1 or text.count(end) != 1:
        raise ValueError(f'Ambiguous/missing section: {start!r} -> {end!r}')
    a, b = text.index(start), text.index(end)
    if b <= a:
        raise ValueError('Reversed section')
    return text[:a] + replacement.rstrip() + '\n\n' + text[b:]

POLICY = '''# 한글화 모델 운용 정책

> 2026-09-13 변경: **Codex GPT-5.6 Sol / Medium이 기본 실무자이며, Web GPT는 사용자 명시 요청 시에만 호출합니다.** 파일명은 기존 링크 호환을 위해 유지합니다.
> 과거의 Web 우선·자동 배차, Sol 감독 전담, 직접 작업 시 예외 사유 제출 규칙은 폐기합니다.

## 1. 기본 작업자는 Codex Sol Medium

평소 분석·설계·구현·디버깅·문서 정리·테스트·검증·통합은 Codex Sol Medium이 직접 수행합니다. 비자명한 작업이라는 이유만으로 Web GPT 위임을 의무화하지 않습니다. 직접 수행한 이유를 별도로 소명할 필요도 없습니다.

기본 설정은 GPT-5.6 Sol / Medium입니다. 사용자가 현재 세션에서 명시적으로 다른 설정을 선택했다면 그 값을 유지하고, 에이전트가 High/XHIGH/Astra로 임의 상향하지 않습니다. 문서 변경만으로 실행 중인 모델 설정이 바뀌었다고 주장하지 않습니다.

## 2. Web GPT는 사용자 지정 시에만

사용자가 현재 작업에 Web GPT 사용을 명시적으로 요청했을 때만 해당 범위에 사용합니다.

```text
평소 한글화 작업 → Codex Sol Medium 직접 수행
사용자: webgpt xh로 이 부분 분석해 → 지정 범위만 WebGPT Extra High
사용자: webgpt p로 독립 검토해 → 지정 범위만 WebGPT Pro
```

설치되어 있다는 사실, 이전 작업에서 사용했다는 사실, 작업이 어렵다는 판단은 새 호출 승인이 아닙니다. “한글화 준비해”, “작업 계속해”, “알아서 해”, “서브에이전트 활용해”만으로 외부 Web GPT 호출을 승인받았다고 해석하지 않습니다.

사용자 지정이 없으면 Web 위임을 위한 브라우저 시작·로그인/맞춤화 검사·연결 시험·미션 제출·대기·폴링·복구를 시작하지 않습니다. 매 작업마다 Web 사용 여부를 재질문하는 것도 기본 절차로 삼지 않습니다. 일반 웹 검색과 GitHub/Drive 자료 열람은 외부 Web GPT 작업자 호출과 다르므로 기존 작업 범위 안에서 사용할 수 있습니다.

사용자가 Nhahan/WebGPT를 지정하면 설치된 해당 스킬의 실제 기능과 문서를 확인하여 사용합니다. 기존 Oracle을 자동으로 호출하거나 두 실행기를 겹쳐 사용하지 않습니다. xh/p 같은 모드 표기를 특정 모델명과 동일시하지 않고 실제 UI 선택 상태를 확인합니다.

## 3. Luna 및 다른 모델

Luna XHIGH는 기존처럼 방법·범위·완료 조건이 정해진 저위험 반복 검색·집계·해시 비교·테스트 보조에 한정합니다. 병렬 호출 개수나 사용 의무는 없습니다. 직접 처리하는 편이 간단하면 Sol Medium이 수행하며, Web 미수행 전문 실무를 Luna 여러 개로 대체하지 않습니다.

설계·원인 판단·애매한 바이너리 추론·관계/존대 판정은 단순 반복 작업으로 취급하지 않습니다. Astra, 로컬 Sol XHIGH, Pro 등으로의 추가 호출이나 상향은 사용자 지정 또는 그 범위의 명시 승인 뒤에만 수행합니다. Terra는 기본 사용하지 않습니다.

## 4. 사용자 지정 위임의 범위와 결과

Web 사용 요청이 있을 때는 실제 사용자 승인 근거, 이번에 맡긴 작업, 읽기/쓰기 허용 경로, 금지 범위, 결과물·검증 조건을 미션에 전달합니다. 없는 승인을 만들어내지 않으며, 작업 승인과 도구 접근 권한을 별도로 확인합니다.

Web 작업자는 지정된 일을 직접 수행하는 최종 작업자입니다. 별도 승인 없이 Oracle/다른 GPT로 재위임하거나 호스트 완료를 기다리지 않습니다. 서로 의존하는 작업은 순차로 하고 같은 파일에 동시 쓰기를 하지 않습니다.

호출·제출 성공과 실질 결과 활용을 구분합니다. 승인 요청만 돌아오면 작업 미수행으로 기록하고, 새 호출·모델 대체·전문 실무 재배정을 자동 실행하지 않습니다. 사용자가 호스트 진행 등 실패 시 대안을 미리 승인했다면 그 범위만 따릅니다. 이 실패 규칙은 원래 Sol Medium이 직접 하는 일반 작업을 제한하는 규칙이 아닙니다.

기존 Oracle/DevSpace를 사용자가 명시적으로 지정한 경우에만 [선택형 Oracle/DevSpace 운영 계약](WEB-SOL-DEVSPACE-OPERATING-CONTRACT.md)을 적용합니다. 과거 E2E 성공은 새 WebGPT 설치나 다른 버전의 성공 증거가 아닙니다.

## 5. 대기·사용량·검증

이미 승인된 동일 Web 작업의 결과 대기·회수·독립 검증은 기존 작업 범위입니다. 단순 예상시간 초과만으로 “추가 대기 승인”을 요구하지 않습니다. 사용자 지정 시간·비용 상한 초과, 새 제출, 범위 확대, 실제 보안·권한 확인은 별도로 처리합니다.

실제 작업 이벤트나 산출물로 진행 여부를 확인하고, 프로세스 생존 또는 로그 갱신만으로 작업 성공을 단정하지 않습니다. 실행기의 정상 대기/완료 기능을 이용하고 불필요한 반복 상태 조회를 피합니다. 제출 여부가 불명확하면 확인 전 재전송하지 않습니다.

사용량 백분율이나 절감 효과를 근거 없이 계산하지 않습니다. 측정할 수 없으면 미측정으로 표시하고 실제 호출·제출·재전송 횟수, 경과시간, 결과 활용 여부만 기록합니다.

작업자는 누구든 실제 diff·허용 범위·관련 테스트·필요한 런타임 결과를 검증합니다. 사용자 실플레이 확정값, 원본 게임 파일, 다른 게임 자료는 보호합니다.

## 6. 기존 프로젝트와 설치 경계

기존 프로젝트는 폴더·원장·번역·성공 자산을 그대로 두고 모델 운용 조항만 최신 사용자 지시에 맞춥니다. 과거 설계 문서의 자동 배차 규칙을 현행 지시로 되살리지 않습니다. 전역/프로젝트 AGENTS.md에 남은 낡은 배차 문구를 정리할 때도 승인·보안·원본 보호 규칙은 없애지 않습니다.

기존 Oracle·DevSpace 설치, 로그인 프로필, 서비스, 진행 중인 run을 이 정책 변경만으로 삭제·종료·교체하지 않습니다. 새 WebGPT 설치·연결·권한 부여는 별도 실제 설치 작업이며, 저장소의 설치 예문 자체를 사용자 동의로 취급하지 않습니다. 설치 또는 파일 접근이 성공했다고 확인 없이 보고하지 않습니다.

사용자가 휴대폰/웹 ChatGPT에서 Google Drive CSV로 직접 수행하는 1차·2차·3차 언어 검수는 그대로 유지합니다. 이는 Codex의 자동 Web 위임과 별개입니다. 1차 1,000행 / 2차 1,000행 / 3차 500행, 각 차수의 최신 용어집 참조, 안정 row_key, 기술 안전성 게이트, 최종 CSV 반입 순서는 바꾸지 않습니다.

**한 줄 원칙: 평소에는 Sol Medium이 직접 일하고, Web GPT는 사용자가 부를 때만 쓴다.**
'''

BOOT_ROUTING = '''# 모델 운용: Sol Medium 기본, Web GPT는 사용자 지정 시에만

**평소 한글화 엔지니어링은 Codex GPT-5.6 Sol / Medium이 직접 수행합니다.** 분석·설계·구현·디버깅·테스트·문서·통합을 맡으며, 직접 작업한 것을 예외로 취급하지 않습니다.

기존의 Web 우선·자동 배차, Sol 감독 전담 규칙은 폐기합니다. 사용자 지정이 없으면 Web 위임용 브라우저 시작·로그인/맞춤화 검사·연결 시험·미션 제출·대기·폴링·복구를 시작하지 않습니다. 일반 웹 검색이나 GitHub/Drive 자료 읽기를 금지한다는 뜻은 아닙니다.

사용자가 “webgpt xh로 분석해”, “webgpt p로 검토해”, “이 부분은 웹 GPT에 맡겨”처럼 지정했을 때만 그 작업 범위에 Web GPT를 사용합니다. 한 번의 지정은 후속 모든 작업의 자동 호출 허가가 아닙니다. 설치되어 있다는 이유로 실행하지 않습니다.

Luna XHIGH는 정해진 저위험 반복 작업의 보조이며 병렬 호출 의무는 없습니다. Astra·로컬 Sol XHIGH 등 고비용 모델로의 변경/추가 호출은 사용자 지정 또는 명시 승인 뒤에만 합니다. 사용자가 선택한 현재 모델·강도를 임의로 상향하지 않습니다.

세부 규칙은 [모델 운용 정책](workflow/SOL-LUNA-AGENT-POLICY.md)을 따릅니다. 기존 [Oracle/DevSpace 계약](workflow/WEB-SOL-DEVSPACE-OPERATING-CONTRACT.md)은 사용자가 그 경로를 지정한 때만 적용하는 선택형 계약입니다. Nhahan/WebGPT와 기존 Oracle의 설치·실행·검증 결과를 서로 혼동하지 않습니다.

이미 승인받아 제출한 동일 작업은 정상 대기·회수·검증까지 이어갑니다. 단순 예상시간 초과는 진행 보고로 처리하고, 사용자 지정 상한이나 실제 승인 범위를 넘길 때만 다시 확인합니다. 측정하지 않은 사용량 백분율이나 절감률을 보고하지 않습니다.

작업 완료는 실제 diff·테스트·필요한 게임 실행 결과로 확인합니다. Web 호출 여부와 실질 결과 활용 여부도 구분합니다.

---'''

OP_ROUTING = '''## 4. 기본 실무와 선택형 Web GPT

**Codex GPT-5.6 Sol / Medium이 기본 실무자**입니다. 평소 파일 분석·설계·추출기/빌더/패처/검수 도구 구현·디버깅·테스트·검증·통합은 직접 수행합니다. 감독만 하고 전문 실무를 반드시 위임해야 한다는 종전 규칙은 적용하지 않습니다.

Web GPT는 사용자 명시 요청 시에만 지정된 범위에 사용합니다. 요청이 없으면 위임을 위한 브라우저·연결 검사·미션 제출·대기·복구를 수행하지 않습니다. 일반 웹 검색 및 GitHub/Drive 자료 확인은 외부 Web 작업자 호출과 구분합니다.

Luna XHIGH는 정해진 저위험 반복 작업의 선택적 보조입니다. 다중 호출 의무는 없으며, 고난도 판단을 대신 맡기지 않습니다. Astra·로컬 Sol XHIGH 등 추가 고비용 모델은 사용자 지정/명시 승인 뒤에만 사용합니다. 세부 기준은 `workflow/SOL-LUNA-AGENT-POLICY.md`를 따릅니다.

기존 Oracle·DevSpace는 임의 제거하거나 교체하지 않습니다. 사용자가 해당 경로를 지정한 경우에만 선택형 `workflow/WEB-SOL-DEVSPACE-OPERATING-CONTRACT.md`를 적용합니다.

### 웹 ChatGPT + Google Drive 언어 검수는 유지

사용자가 PC 없이 휴대폰/웹 ChatGPT에서 Drive의 게임별 CSV와 기준자료로 수행하는 대량 번역/검수는 그대로입니다. Codex가 외부 웹 작업자를 자동 호출하는 것과 별개입니다.

- 0단계: 앞선 기술 게이트·전체 원장·분류·검수 프로그램을 바탕으로 용어집·캐릭터·관계·말투 준비
- 1차: 전체 대사집을 1,000행 단위로 기초 검수
- 2차: 1차 결과 전체를 다시 1,000행 단위로 자연화·말투 보정
- 3차: 2차 결과 전체를 다시 500행 단위로 최종 정밀검수

세 차수 모두 최신 용어집을 참고하며, Codex가 이 대량 언어 검수를 자동으로 대신 시작하지 않습니다.'''

TEMPLATE_ROUTING = '''## Agent Model Policy

- Default implementation owner: `Codex GPT-5.6 Sol / Medium`
- Web GPT delegation: `사용자 명시 요청 시에만`
- Current user-selected model/effort: `<CURRENT_SETTING>`
- Explicit Web task scope, if requested: `<NONE_OR_APPROVED_SCOPE>`

평소 분석·설계·구현·디버깅·문서·테스트·통합은 Sol Medium이 직접 수행합니다. 직접 작업을 예외로 보거나 이유를 요구하지 않습니다. 종전 Web 우선·자동 배차와 Sol 감독 전담 규칙은 적용하지 않습니다.

Web 사용 요청이 없으면 위임용 연결 검사·브라우저 시작·미션 제출·대기·복구를 시작하지 않습니다. 요청이 있으면 그 범위에만 지정된 도구와 모드를 사용하고, 실제 승인 근거·허용 경로·결과물을 인계합니다. 보안·권한 확인은 생략하지 않습니다.

Luna XHIGH는 확정된 저위험 반복 작업 보조이며 병렬 호출 의무는 없습니다. 고비용 모델로의 변경/추가 호출은 사용자 지정/명시 승인 뒤에만 합니다. 사용자가 선택한 현재 세션 설정을 임의 변경하지 않습니다.

세부 기준은 최신 `workflow/SOL-LUNA-AGENT-POLICY.md`입니다. 기존 Oracle/DevSpace 사용을 명시 지정한 경우에만 `workflow/WEB-SOL-DEVSPACE-OPERATING-CONTRACT.md`를 추가 적용합니다. 설치·서비스·로그인 프로필을 임의 교체하거나 과거 시험을 새 WebGPT 설치 성공으로 주장하지 않습니다.

예상시간만 초과한 동일 작업은 재승인 없이 정상 대기·회수·검증하며, 실제 사용자 상한/승인 범위를 넘길 때만 확인합니다. 사용량은 측정하지 않았으면 미측정으로 보고합니다.

기존 프로젝트의 성과와 안전 규칙을 보존합니다. 이 변경은 모델 운용에만 적용하며, Google Drive에서 사용자가 직접 진행하는 1차 1,000행 / 2차 1,000행 / 3차 500행 및 최신 용어집 참조 규칙은 유지합니다.'''

TRIGGER_BOUNDARIES = '''## Important boundaries

- 기본 담당은 **Codex GPT-5.6 Sol / Medium**입니다. 평소 분석·설계·구현·디버깅·테스트는 직접 수행합니다. 사용자의 현재 모델 선택을 임의 상향하지 않습니다.
- **Web GPT는 사용자 명시 요청 시에만** 지정 범위에 호출합니다. 이 bootstrap 스킬의 자동 로드는 Web GPT 자동 호출 허가가 아닙니다.
- 사용자 지정이 없으면 Web 위임을 위한 연결 확인·로그인/맞춤화 검사·브라우저 실행·미션 작성/제출·대기·복구를 시작하지 않습니다. 일반 웹 검색·GitHub/Drive 읽기는 별개입니다.
- 상세 모델 운용은 최신 `workflow/SOL-LUNA-AGENT-POLICY.md`를 따릅니다. 낡은 snapshot/프로젝트 문구의 Web 우선·자동 배차·Sol 감독 전담을 현재 사용자 지시보다 우선하지 않습니다.
- Oracle/DevSpace 경로를 사용자가 지정한 때만 `workflow/WEB-SOL-DEVSPACE-OPERATING-CONTRACT.md`를 적용합니다. Nhahan/WebGPT 설치와 과거 Oracle E2E 기록은 별개입니다.
- 기존 Oracle·DevSpace·로그인 프로필·진행 중인 작업은 정책 변경만으로 삭제·교체·종료하지 않습니다. 실제 승인·보안·권한 확인은 유지합니다.
- Luna는 정해진 저위험 반복 보조이며 병렬 호출 의무는 없습니다. 고비용 모델을 자동 대체 투입하지 않습니다.
- 사용자가 별도로 요청하지 않은 HD Pack 제작을 자동 시작하지 않습니다.
- 게임별 6폴더·기술 안전성·전체 원장/분류/검수 프로그램 선행·Drive 구조·1,000/1,000/500행·최신 용어집 참조는 그대로 유지합니다.
- 모델 호출이나 연결을 실제 수행하지 않았다면 수행했다고 보고하지 않습니다. 사용량은 근거가 없으면 미측정입니다.
- 실제 프로젝트 상태와 관련 테스트를 확인하기 전에는 완료로 판단하지 않습니다.
'''

CONTRACT_SCOPE = '''## 0. 적용 범위: 사용자 지정 시에만

**평소 작업은 Codex Sol Medium이 직접 수행하며, 이 계약은 사용자가 기존 Oracle/DevSpace 경유 Web GPT 작업을 명시적으로 지정했을 때만 적용합니다.** 자동 배차·사전 연결 확인·호출·대기·복구를 위한 상시 절차가 아닙니다. 일반 운용 기준은 [모델 운용 정책](SOL-LUNA-AGENT-POLICY.md)을 따릅니다.

아래 E2E 결과는 과거 사용자 설치 환경의 기록으로 보존합니다. Nhahan/WebGPT의 신규 설치·Windows 동작·파일 권한·모드·콜백·정리 성공까지 입증하지 않습니다. 사용자가 WebGPT를 지정하면 그 설치본의 문서와 실제 기능을 사용하며 Oracle로 자동 대체하지 않습니다.

기존 설치·서비스·로그인 프로필은 이 정책 변경만으로 삭제·교체하지 않습니다.

'''

CONTRACT_FAILURE = '''## 6. 사용자 지정 호출의 실패와 대기

요청한 Web 경로가 실패하면 실제 단계와 오류를 기록하고, 지정 작업을 다른 모델이나 Oracle/WebGPT 등 다른 실행기로 조용히 대체하지 않습니다. 새 질문 자동 재제출도 하지 않습니다. 사용자가 실패 시 호스트 진행을 미리 허용했다면 그 범위만 따르고, 그렇지 않으면 해당 작업의 대안을 확인합니다. 정상적인 일반 작업을 Sol Medium이 직접 하는 것은 대체 위반이 아닙니다.

승인 요청만 반환된 경우 호출 성공과 실질 작업 미수행을 구분합니다. 없는 승인을 만들거나 보안 확인을 무시하지 않습니다. 같은 작업의 결과 대기·회수·검증은 기존 승인 범위이므로 단순 예상시간 초과만으로 추가 대기 승인을 요구하지 않습니다. 사용자 지정 상한 초과·범위 확대·새 제출·실제 권한/보안 확인은 별개입니다.

DevSpace를 사용하는 해당 작업에서만 정확한 루트의 `open_workspace`를 실제 호출한 뒤 연결 상태를 판정합니다. `tool disabled`/`FORBIDDEN`이면 현재 ChatGPT 세션·앱 문제로 보고하며 DevSpace 수동 실행·재설치·Tailscale·Watchdog·OAuth 변경을 지시하지 않습니다. 실제 `502`/`network_error`일 때만 같은 작업의 연결 호출을 최소 1분 간격 5회 재시도한 뒤 MCP 경로를 조사합니다. 이는 Oracle 질문 재전송이 아닙니다.

역할 혼동·중첩 호출·승인만 반환한 수행 실패는 연결 재시도 대상으로 취급하지 않습니다. 사용자 요청이 없는 일반 작업에서는 이 진단/재시도 자체를 시작하지 않습니다.'''


def transform(before):
    out = dict(before)
    p = 'CODEX-LOCALIZATION-BOOTSTRAP.md'
    t = out[p]
    t = span(t, '# 모델 자동 라우팅\n', '## Google Drive 검수 구조\n', BOOT_ROUTING)
    t = span(t, '## 모델 또는 기능을 사용할 수 없을 때\n', '## 템플릿\n', '''## 모델 또는 기능을 사용할 수 없을 때

평소 작업은 Sol Medium이 직접 수행합니다. 사용자 지정 Web 작업이 없는데 외부 연결 실패 여부부터 검사하며 일반 작업을 중단하지 않습니다.

사용자가 특정 Web 도구/모델을 지정했는데 실제로 사용할 수 없으면 해당 작업의 구체적인 실패만 보고합니다. 사용자 승인 없는 대체 모델·새 실행기·새 유료 API·중복 제출을 실행하지 않습니다. 실패 시 진행 대안을 미리 승인받았다면 그 범위만 따릅니다.

실제 실행하지 않은 모델 호출·연결·설치·검증을 수행했다고 보고하지 않습니다.

---''')
    t = once(t, '**Sol High가 기본 총괄자로서 자동으로 배차합니다.**', '**평소 작업은 Codex Sol Medium이 직접 수행하며, Web GPT는 사용자 명시 요청 시에만 호출합니다.**')
    old = '**사용자는 모델 배차를 매 작업마다 다시 지시할 필요가 없습니다.** Sol High는 감독·배차·최종 검증을 맡고, 일반~상당 난도의 전문 실무는 DevSpace + Web GPT-5.6 Sol XHIGH가 기본 책임집니다.'
    t = once(t, old, '**평소에는 Codex Sol Medium이 직접 작업합니다. Web GPT가 필요한 작업만 사용자가 지정합니다.** 한글화 순서와 Drive 언어 검수 규칙은 그대로 유지합니다.')
    out[p] = t
    out['workflow/SOL-LUNA-AGENT-POLICY.md'] = POLICY
    p = 'workflow/PROJECT-OPERATING-MODEL.md'
    out[p] = span(out[p], '## 4. Codex와 작업자 계층의 역할 분리\n', '## 5. 공통 코드 재사용과 게임 데이터 격리\n', OP_ROUTING)
    p = 'templates/AGENTS.template.md'
    out[p] = span(out[p], '## Agent Model Policy\n', '## Existing Approved Assets / Decisions\n', TEMPLATE_ROUTING)
    p = 'codex-auto-trigger/SKILL.md'
    t = out[p]
    if t.count('## Important boundaries\n') != 1:
        raise ValueError('Missing trigger boundaries')
    out[p] = t[:t.index('## Important boundaries\n')] + TRIGGER_BOUNDARIES
    p = 'workflow/WEB-SOL-DEVSPACE-OPERATING-CONTRACT.md'
    t = once(out[p], '# Web GPT-5.6 Sol XHIGH + DevSpace 검증 운영 계약', '# Oracle / Web GPT-5.6 Sol + DevSpace 선택형 운영 계약')
    t = once(t, '## 1. 검증된 실행 경로\n', CONTRACT_SCOPE + '## 1. 검증된 실행 경로\n')
    t = once(t, 'Web GPT 미션에는 다음 역할 경계를 유지합니다.', '사용자의 실제 Web 호출 요청과 해당 단계 승인 근거, 정확한 업무 범위·허용 경로·금지 작업·결과물을 미션에 함께 전달합니다. 호스트에서 받은 승인을 누락하지 않되 승인 범위를 확대하지 않습니다. 작업 허용 경로와 도구 접근 권한을 별도로 대조합니다.\n\nWeb GPT 미션에는 다음 역할 경계를 유지합니다.')
    t = span(t, '## 6. 호출 실패와 대체 금지\n', '## 7. 호스트 검증 책임\n', CONTRACT_FAILURE)
    t = once(t, '**한 줄 원칙: Web Sol XHIGH는 실제 파일을 읽고 만들고 기존 파일을 정밀 수정하는 주력 실무자로 사용할 수 있다. 계정 전역 개인화와 Oracle 소유 임시채팅 맞춤화를 구분하고, 삭제·이동·이름 변경은 기본 금지하며, Sol 관리자가 diff와 테스트를 독립 검증한 뒤 통합한다.**', '**한 줄 원칙: 평소에는 Sol Medium이 직접 작업한다. 사용자가 Oracle/DevSpace 경유 Web 작업을 지정한 경우에만 이 계약의 승인·권한·검증·안전선을 적용한다.**')
    out[p] = t
    p = 'README.md'
    out[p] = once(out[p], '  - GPT-5.6 Sol / Luna 역할 분담', '  - **Codex GPT-5.6 Sol / Medium 직접 작업이 기본, Web GPT는 사용자 명시 요청 시에만 호출**\n  - Luna는 저위험 반복 작업 보조이며 자동 Web 위임은 사용하지 않음')
    p = 'codex-auto-trigger/agents/openai.yaml'
    out[p] = once(out[p], 'Read the latest canonical bootstrap first, then continue within the project rules.', 'Read the latest canonical bootstrap first. Default to direct Codex Sol Medium work; invoke Web GPT only when the user explicitly requests it. Preserve project safety rules.')
    return out


def verify(before, after):
    assert set(before) == set(after) == set(EXPECTED)
    for path, text in after.items():
        assert text.strip() and '\x00' not in text, path
        assert 'Sol High' not in text, f'Obsolete Sol High role: {path}'
        assert '기본 전문 실무 책임자' not in text, f'Obsolete mandatory Web role: {path}'
        assert '자동으로 배차' not in text, f'Obsolete auto-dispatch: {path}'
        assert not any(line.rstrip() != line for line in text.splitlines()), path
    boot = after['CODEX-LOCALIZATION-BOOTSTRAP.md']
    assert 'Web GPT는 사용자 명시 요청 시에만' in boot
    assert '1차·2차·3차 검수 모두 `01_최신_용어집`' in boot
    for path in ('CODEX-LOCALIZATION-BOOTSTRAP.md', 'workflow/PROJECT-OPERATING-MODEL.md', 'templates/AGENTS.template.md'):
        for term in ('01_프로젝트_문서', '02_한글화_작업', '03_검수_프로그램', '04_최종_배포', '05_HD Pack', '버그 리포트', 'row_key', 'subcategory', '01_최신_용어집', '02_검수_필수파일', '03_검수_수정_CSV', '1,000행', '500행'):
            assert term in after[path], (path, term)
    for start, end in (('## Google Drive 검수 구조\n', '## 모델 또는 기능을 사용할 수 없을 때\n'), ('## 핵심 원칙\n', '# 모델 자동 라우팅\n')):
        old = before['CODEX-LOCALIZATION-BOOTSTRAP.md']
        new = boot
        new_end = '# 모델 운용: Sol Medium 기본, Web GPT는 사용자 지정 시에만\n' if end.startswith('# 모델 자동') else end
        assert old[old.index(start):old.index(end)] == new[new.index(start):new.index(new_end)], start
    old = before['workflow/WEB-SOL-DEVSPACE-OPERATING-CONTRACT.md']
    new = after['workflow/WEB-SOL-DEVSPACE-OPERATING-CONTRACT.md']
    assert old[old.index('## 1.'):old.index('## 5.')] == new[new.index('## 1.'):new.index('## 5.')]
    assert 'allow_implicit_invocation: true' in after['codex-auto-trigger/agents/openai.yaml']
    assert '이 bootstrap 스킬의 자동 로드는 Web GPT 자동 호출 허가가 아닙니다.' in after['codex-auto-trigger/SKILL.md']
    print('VERIFY_OK: 8 routing/entry documents; language, Drive and legacy E2E/safety content preserved')


def main():
    before = {}
    for path, expected in EXPECTED.items():
        data = Path(path).read_bytes()
        actual = blob_sha(data)
        if actual != expected:
            raise SystemExit(f'Concurrent change or baseline mismatch at {path}: {actual} != {expected}')
        before[path] = data.decode('utf-8')
    after = transform(before)
    verify(before, after)
    for path, text in after.items():
        Path(path).write_text(text, encoding='utf-8', newline='\n')
    print('UPDATED:', *after.keys(), sep='\n')

if __name__ == '__main__':
    main()
