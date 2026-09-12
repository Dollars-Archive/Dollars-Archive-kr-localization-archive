from pathlib import Path


def read(path: str) -> str:
    return Path(path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    Path(path).write_text(text, encoding="utf-8", newline="\n")


def replace_span(text: str, start_marker: str, end_marker: str, replacement: str) -> str:
    start = text.find(start_marker)
    if start < 0:
        raise SystemExit(f"missing start marker: {start_marker}")
    end = text.find(end_marker, start + len(start_marker))
    if end < 0:
        raise SystemExit(f"missing end marker after {start_marker}: {end_marker}")
    return text[:start] + replacement.rstrip() + "\n\n" + text[end:]


def replace_to_eof(text: str, start_marker: str, replacement: str) -> str:
    start = text.find(start_marker)
    if start < 0:
        raise SystemExit(f"missing eof start marker: {start_marker}")
    return text[:start] + replacement.rstrip() + "\n"


# ---------------------------------------------------------------------------
# CODEX-LOCALIZATION-BOOTSTRAP.md
# ---------------------------------------------------------------------------
path = "CODEX-LOCALIZATION-BOOTSTRAP.md"
text = read(path)

text = replace_span(
    text,
    "## 링크 하나만 받은 Codex의 기본 동작",
    "---\n\n## 핵심 원칙",
    r'''## 링크 하나만 받은 Codex의 기본 동작

사용자가 이 문서 링크와 함께 새 게임 한글화 작업을 지시했다면 다음 순서를 기본값으로 사용합니다.

```text
1. 이 문서를 읽는다
2. 신규/기존 프로젝트를 판정한다
3. 신규라면 D:\Codex\한글화 프로젝트\<게임명> 아래 기본 6폴더부터 만든다
4. 롬/게임 파일 구조, 텍스트, 폰트, 인코딩, 추출·재삽입 경로를 분석한다
5. 최소 한글 출력 샘플을 만들고 사용자 실기 확인을 받는다
6. 가로폭·최대 줄 수·[n]·반각/전각·RSC/인코딩·다음 장면 진행 안전성을 검증한다
7. 안전한 경로가 확인된 뒤 일본어 원문 전체를 추출한다
8. 안정 row_key와 category/subcategory를 가진 원장을 만든다
9. 게임 전용 검수 프로그램을 구축해 원장·분류·수정 이력을 관리한다
10. 전체 원장과 분류를 근거로 번역 전 0단계 용어·캐릭터·말투·방향별 관계 기준을 만든다
11. F:\내 드라이브\검수 프로그램\<게임명>에 용어집·필수파일·분류 CSV를 준비하고 동기화/재조회를 확인한다
12. Google Drive를 기준으로 웹 ChatGPT에서 1차 1,000행 → 2차 1,000행 → 3차 500행으로 전체 데이터를 각각 다시 검수한다
13. <게임약칭>_최종대사_수정_누적.csv를 게임 전용 검수 프로그램 최신 원장에 반입한다
14. 모드/패치를 만들고 실제 플레이 검증 결과를 다시 원장에 확정한다
```

기존 프로젝트는 현재 루트와 성공 자산을 보존하고, 위 순서에서 이미 증거가 있는 단계는 반복하지 않습니다. 부족한 단계만 보강합니다.

사용자가 매 작업마다 모델을 직접 지정할 필요는 없습니다. **Sol High가 기본 총괄자로서 자동으로 배차합니다.** 작업에 필요한 정보가 이미 프로젝트와 이 문서에 있다면 같은 내용을 다시 설명하도록 요구하지 않습니다.'''
)

text = replace_span(
    text,
    "## 핵심 원칙",
    "---\n\n## 신규 프로젝트는 게임 전용 폴더부터 만든다",
    r'''## 핵심 원칙

```text
전용 프로젝트 생성
→ 롬/게임 구조 분석
→ 최소 한글 출력
→ 출력·진행 안전성 게이트
→ 전체 일본어 원문 추출
→ 안정 row_key + category/subcategory 원장
→ 게임 전용 검수 프로그램
→ 번역 전 0단계 기준자료
→ Google Drive 휴대폰/웹 검수 작업장
→ 1차 1,000행 → 2차 1,000행 → 3차 500행
→ 최종 누적 CSV 원장 반입
→ 모드/패치 생성
→ 실제 플레이 검증
```

**대량 번역보다 먼저 기술적 진행 가능성과 검수 가능한 데이터 구조를 완성합니다.** 한글 한 글자가 보였다는 이유만으로 대사를 대량 번역하지 않으며, 단순 일본어 문장 덤프를 검수용 CSV로 사용하지 않습니다.

아카이브의 문서는 범용 노하우입니다. 실제 대상 프로젝트의 파일, 현재 구현, 성공 샘플, 해시, 런타임 결과보다 우선하지 않습니다.'''
)

text = replace_span(
    text,
    "## 신규 프로젝트는 게임 전용 폴더부터 만든다",
    "---\n\n## 최초 한글 출력의 필수 합격 관문",
    r'''## 신규 프로젝트는 게임 전용 폴더부터 만든다

대상 게임이 정해졌고 아직 해당 게임의 한글화 프로젝트 루트가 없다면, **실제 조사·추출·문서 작성·도구 제작보다 먼저** 다음 구조를 만듭니다.

```text
D:\Codex\한글화 프로젝트\<게임명>\
├─ 01_프로젝트_문서
├─ 02_한글화_작업
├─ 03_검수_프로그램
├─ 04_최종_배포
├─ 05_HD Pack
└─ 버그 리포트
```

기본 역할:

- `01_프로젝트_문서`: 분석 보고서, 설계, 결정 기록, 인수인계 성격 문서
- `02_한글화_작업`: 롬/파일 분석, 추출·재삽입, 폰트/UI/대사, 빌더, 중간 분석·staging
- `03_검수_프로그램`: 게임 전용 원장, row_key, 카테고리화, 검수 프로그램, 최종 CSV 반입
- `04_최종_배포`: 최종 모드·패치·패처·배포 준비 산출물
- `05_HD Pack`: 모든 신규 프로젝트에서 폴더만 준비. 사용자 명시 요청 전 실제 HD Pack 작업 금지
- `버그 리포트`: 재현된 오류, 실플레이 문제, 증거와 추적 기록

`.github`, `docs`, `source`, `staging`, `tests`, `tools`, `work`, `셀프 검수 프로그램`, `인수인계`, `작업 자료` 등은 특정 프로젝트가 필요하면 추가할 수 있지만 **신규 프로젝트 공통 필수 베이스로 강제하지 않습니다.**

게임명이 확정된 뒤에는 해당 작품의 재사용 가능한 조사 자료·중간 산출물·검수 프로그램·증거를 이 프로젝트 루트 안에서 관리합니다. 바탕화면, 사용자 홈, 공용 임시 작업 폴더, 다른 게임 프로젝트를 임시 작업장으로 사용하지 않습니다.

기존 프로젝트가 이미 존재하면 이 규칙을 이유로 새 폴더를 중복 생성하거나 이름을 바꾸거나 구조를 강제 재배치하지 않습니다.'''
)

# Replace the old sentence that allowed language baseline work to be treated as a parallel peer before corpus/review-program preparation.
old = "이 기술 관문과 용어집·캐릭터·관계·말투의 언어 0단계는 둘 다 본 번역의 선행 조건입니다. 조사·기준자료 구축은 병행할 수 있습니다. **1차 1,000행 / 2차 1,000행 / 3차 500행은 그대로 유지**하고, 초반 기술 시험을 매 검수 묶음에 반복 전가하지 않습니다. 기존 프로젝트의 성공 자료·사용자 확정값은 보존하고 부족한 시험만 보강합니다."
new = "이 기술 관문을 통과한 뒤 전체 일본어 원문을 추출하고 안정 `row_key`와 `category/subcategory`를 갖춘 원장을 만든 다음 게임 전용 검수 프로그램을 준비합니다. **그 전체 원장과 분류를 근거로 언어 0단계 기준자료를 구축합니다.** 1차 1,000행 / 2차 1,000행 / 3차 500행은 그대로 유지하고, 초반 기술 시험을 매 검수 묶음에 반복 전가하지 않습니다. 기존 프로젝트의 성공 자료·사용자 확정값은 보존하고 부족한 시험만 보강합니다."
if old not in text:
    raise SystemExit("bootstrap early-gate ordering anchor missing")
text = text.replace(old, new, 1)

text = replace_span(
    text,
    "## Codex 작업 시작 순서",
    "---\n\n## 프로젝트 분리 원칙",
    r'''## Codex 작업 시작 순서

1. 현재 작업 대상 게임이 신규인지 기존인지 확인합니다.
2. 신규라면 `D:\Codex\한글화 프로젝트\<게임명>` 아래 기본 6폴더를 먼저 만듭니다. 기존 프로젝트는 현재 루트를 유지합니다.
3. 대상 프로젝트의 `AGENTS.md`와 기존 성공 자산·사용자 확정값을 확인합니다.
4. 롬/게임 파일에서 텍스트 위치·형식, 추출·재삽입, 인코딩, 폰트, 최소 빌더/패처 경로를 분석합니다.
5. 최소 한글 출력 샘플을 만들고 사용자가 실제 게임에서 한 글자 또는 짧은 문장을 확인합니다.
6. `workflow/EARLY-TEXT-RUNTIME-GATE.md`에 따라 가로폭, 최대 줄 수, 자동 줄바꿈, `[n]` 동작별 안전성, 반각/전각, 공백·문장부호, RSC/인코딩, 다음 대사·장면 진행을 검증합니다.
7. `진행 가능` 또는 검증된 보존 조건의 `조건부 진행`이 확보되기 전에는 대량 번역을 시작하지 않습니다.
8. 안전 경로가 확인되면 일본어 원문 전체를 추출하고 번역문과 독립적인 안정 `row_key`를 부여합니다.
9. 각 레코드에 `category`와 `subcategory`를 부여해 일반 대사·캐릭터 대사·튜토리얼·시스템·UI·아이템·무기·방어구·재료·스킬·던전 등 기능을 구분합니다.
10. `03_검수_프로그램`에 게임 전용 원장과 검수 프로그램을 구축합니다. 프로그램 구조는 EVE 고스트 에너미즈, 카테고리/세부분류 방식은 이상한 환상향 로터스 라비린스 검수 프로그램을 참고할 수 있으나 게임별 데이터는 복사하지 않습니다.
11. 전체 원장과 카테고리를 근거로 `review/PRE-TRANSLATION-SETUP.md`의 번역 전 0단계 기준자료를 구축합니다. 관계/존대/호칭은 반드시 화자 → 청자 방향별로 관리합니다.
12. `F:\내 드라이브\검수 프로그램\<게임명>`의 기존 구조를 확인하고 `01_최신_용어집`, `02_검수_필수파일`, `03_검수_수정_CSV` 역할을 준비합니다.
13. Drive에 최신 용어집, 캐릭터/관계/말투/출력 규격, 서로 분리된 1·2·3차 지시문, row_key/category/subcategory가 살아 있는 검수 CSV를 등록합니다.
14. 동기화 후 Drive의 등록 파일을 다시 읽어 실제 반영을 확인하기 전에는 0단계 완료 또는 1차 시작 가능이라고 판정하지 않습니다.
15. 웹 ChatGPT에서 전체 데이터를 1차 1,000행, 2차 1,000행, 3차 500행 단위로 각각 다시 검수합니다.
16. `<게임약칭>_최종대사_수정_누적.csv`를 게임 전용 검수 프로그램 최신 원장에 반입합니다.
17. 정적 검증 후 모드/패치를 만들고 실제 플레이에서 확인한 수정값을 가장 높은 우선순위의 확정값으로 원장에 반영합니다.

플랫폼별 기술 문서는 실제 대상과 일치할 때만 추가로 읽습니다. Nintendo Switch라면 `switch/SWITCH-KOREAN-LOCALIZATION-GUIDE.md`를 사용합니다. 공개 작업일지가 필요한 프로젝트는 `workflow/PUBLIC-WORKLOG-STANDARD.md`를 따릅니다.'''
)

# Replace Google Drive section with the actual mobile/web review workspace layout.
text = replace_span(
    text,
    "## Google Drive 검수 구조",
    "---\n\n## 실제 플레이 피드백",
    r'''## Google Drive 검수 구조

Google Drive는 단순 백업이 아니라 **PC를 켜두지 않고 밖에서 휴대폰/웹 ChatGPT만으로 1·2·3차 검수를 수행하기 위한 실제 검수 작업장**입니다.

PC 동기화 상위 루트:

```text
F:\내 드라이브\검수 프로그램
```

게임별 기본 실사용 구조:

```text
F:\내 드라이브\검수 프로그램\<게임명>\
├─ 01_최신_용어집
├─ 02_검수_필수파일
└─ 03_검수_수정_CSV
```

기존 게임 폴더가 이미 있으면 새 구조를 중복 생성하거나 강제 재배치하지 않고 동일 역할의 기존 폴더를 사용합니다. 예를 들어 로터스의 실제 검수 필수파일 위치는 `F:\내 드라이브\검수 프로그램\이상한 환상향 로터스 라비린스\02_검수_필수파일`입니다.

### `01_최신_용어집`

- 캐릭터명·별칭·칭호
- 세계관·조직·종족·지역·던전
- 아이템·무기·방어구·재료·스킬·시스템 용어
- 카테고리별 최신 용어집
- confirmed / provisional / HOLD 상태

### `02_검수_필수파일`

휴대폰의 웹 ChatGPT만 열어도 검수 기준을 복원할 수 있도록 다음을 둡니다.

- 번역 전 기준자료
- 캐릭터 성격과 기본 말투
- 화자 → 청자 방향별 관계도
- 방향별 반말/존댓말·호칭·예외
- HOLD와 출처
- `layout_profile` 또는 동등 출력/진행 규격
- `[n]`, 반각/전각, 가로폭, 최대 줄 수, RSC/인코딩 보호 규칙
- 1차 1,000행 전용 지시문
- 2차 1,000행 전용 지시문
- 3차 500행 전용 지시문

1차·2차·3차 지시문은 물리적으로 분리하고 서로의 지시문을 섞지 않습니다.

### `03_검수_수정_CSV`

게임 전용 검수 프로그램의 최신 원장에서 내보낸 검수용 CSV를 둡니다. 단순 일본어 문장 덤프를 사용하지 않습니다.

최소 유지 정보:

```text
row_key
japanese_source
category
subcategory
speaker
listener
control_tokens
current_translation
review_status
```

### 1차 시작 전 하드 게이트

다음이 끝나기 전에는 `0단계 완료` 또는 `1차 검수 시작 가능`이라고 보고하지 않습니다.

1. 정확한 게임별 Drive 작업공간 확인
2. `01_최신_용어집` 최신화
3. `02_검수_필수파일` 최신화
4. `03_검수_수정_CSV`에 분류된 원장 CSV 준비
5. Google Drive 동기화 확인
6. 등록 파일을 다시 읽어 실제 반영 확인

로컬의 0단계 자료만 존재하면 `LOCAL_DRAFT_ONLY`, Drive 반입 대기면 `DRIVE_REGISTRATION_PENDING`으로 취급합니다.

검수 흐름은 고정합니다.

```text
1차: 전체 대사집을 1,000행 단위로 처음부터 끝까지 검수
→ 2차: 1차 전체 결과를 다시 1,000행 단위로 처음부터 끝까지 검수
→ 3차: 2차 전체 결과를 다시 500행 단위로 최종 정밀검수
→ <게임약칭>_최종대사_수정_누적.csv
→ 게임 전용 검수 프로그램 최신 원장 반입
```

Google Drive의 중간 자료 전체를 로컬 프로젝트로 다시 복사할 필요는 없습니다. 3차 완료 후 로컬 검수 프로그램으로 돌아오는 핵심 산출물은 최종 누적 CSV입니다.'''
)

# Strengthen the beginning of the existing 0-stage section without duplicating all detailed language rules.
anchor = "# 번역 전 0단계: 기준자료와 용어집을 먼저 만든다\n\n"
if anchor not in text:
    raise SystemExit("bootstrap stage0 heading missing")
insert = r'''# 번역 전 0단계: 전체 원장과 분류를 보고 기준자료를 만든다

**이 0단계는 프로젝트 생성 직후가 아니라, 초기 기술 안전성 게이트를 통과하고 전체 일본어 원문·안정 `row_key`·`category/subcategory` 원장과 게임 전용 검수 프로그램을 준비한 뒤 수행합니다.** 그래야 아이템·시스템·튜토리얼·캐릭터 대사 등 문자열의 실제 기능과 반복 빈도를 본 상태에서 기준자료를 만들 수 있습니다.

'''
text = text.replace(anchor, insert, 1)

text = replace_to_eof(
    text,
    "# 한 줄 요약",
    r'''# 한 줄 요약

사용자가 이 문서 링크와 새 게임 한글화 작업을 전달하면:

```text
게임 전용 6폴더 생성
→ 롬/게임 구조 분석
→ 최소 한글 출력과 사용자 실기 확인
→ [n]·반각/전각·가로폭·줄 수·진행 안전성 게이트
→ 전체 일본어 원문 추출
→ 안정 row_key + category/subcategory 원장
→ 게임 전용 검수 프로그램
→ 번역 전 0단계 용어·캐릭터·말투·방향별 관계
→ F:\내 드라이브\검수 프로그램\<게임명>에 최신 용어집·필수파일·분류 CSV 준비
→ 휴대폰/웹 ChatGPT에서 전체 데이터를 1차 1000 → 2차 1000 → 3차 500으로 재검수
→ <게임약칭>_최종대사_수정_누적.csv를 최신 원장에 반입
→ 모드/패치 생성과 실제 플레이 검증
```

**사용자는 모델 배차를 매 작업마다 다시 지시할 필요가 없습니다.** Sol High는 감독·배차·최종 검증을 맡고, 일반~상당 난도의 전문 실무는 DevSpace + Web GPT-5.6 Sol XHIGH가 기본 책임집니다.'''
)
write(path, text)


# ---------------------------------------------------------------------------
# workflow/PROJECT-OPERATING-MODEL.md
# ---------------------------------------------------------------------------
path = "workflow/PROJECT-OPERATING-MODEL.md"
text = read(path)

text = replace_span(
    text,
    "## 2. 기준 프로젝트와 기본 디렉터리 구조",
    "### PS3 이하 작품의 `05_HD Pack`",
    r'''## 2. 신규 프로젝트의 기본 디렉터리 구조

게임이 정해지고 새 프로젝트를 시작하면 다음 여섯 폴더를 공통 기본 베이스로 먼저 만듭니다.

```text
D:\Codex\한글화 프로젝트\<작품 폴더명>\
├─ 01_프로젝트_문서
├─ 02_한글화_작업
├─ 03_검수_프로그램
├─ 04_최종_배포
├─ 05_HD Pack
└─ 버그 리포트
```

- `01_프로젝트_문서`: 분석 보고서, 설계, 결정 기록, 인수인계 성격 문서
- `02_한글화_작업`: 게임 파일 분석, 추출·재삽입, 폰트/UI/대사, 빌더, 중간 분석·staging
- `03_검수_프로그램`: 게임 전용 원장, 안정 row_key, 카테고리화, 검수 프로그램, 최종 CSV 반입
- `04_최종_배포`: 최종 모드·패치·패처·배포 준비 산출물
- `05_HD Pack`: 폴더만 기본 생성하며 사용자 요청 전 실제 제작 금지
- `버그 리포트`: 재현된 오류, 실플레이 문제, 증거와 추적 기록

`D:\Codex\한글화 프로젝트\이상한 환상향 로터스 Lotus Labyrinth`는 폴더 역할을 참고할 수 있는 기존 프로젝트지만, 특정 프로젝트에서 추가된 `.github`, `docs`, `source`, `staging`, `tests`, `tools`, `work`, `셀프 검수 프로그램`, `인수인계`, `작업 자료` 등을 모든 신규 프로젝트의 필수 최상위 폴더로 복제하지 않습니다.

프로젝트별 필요에 따라 추가 폴더를 만들 수는 있습니다. 단, 게임 전용 데이터·코드·번역·로그·오프셋·원본 자산을 다른 게임 프로젝트에서 복사하거나 섞지 않습니다.

기존 프로젝트는 이 구조를 이유로 강제 재배치하지 않습니다. 현재 루트와 성공 자산을 보존하고 필요한 연결 규칙만 보강합니다.'''
)

text = replace_span(
    text,
    "### PS3 이하 작품의 `05_HD Pack`",
    "### 한글화 폰트 후보 선정",
    r'''### `05_HD Pack` 운영 경계

`05_HD Pack`은 신규 한글화 프로젝트의 기본 6폴더 중 하나로 **폴더만 미리 생성**합니다.

**사용자가 `HD Pack 제작`, `HD팩 작업`, `텍스처 업스케일` 등으로 명시적으로 요청하기 전에는 실제 텍스처 덤프·업스케일·이미지 재가공·교체 작업을 시작하지 않습니다.**

사용자가 HD Pack 제작 또는 가능성 분석을 명시적으로 요청한 경우 `workflow/HD-PACK-PIPELINE.md`를 읽고, 가능한 플랫폼에서는 ROM/ISO 내부 자산 우선 → 소량 샘플 검증 → 에뮬레이터 dump/hash 매칭 → 신규 dump 증분 처리 원칙을 적용합니다.

HD Pack 결과는 번역/패치 결과와 자동으로 섞어 배포하지 않습니다.'''
)

text = replace_span(
    text,
    "### 번역 전 0단계: 용어집·캐릭터·관계 기준 선세팅",
    "## 3. 프로젝트 기본 단위",
    r'''### 번역 전 0단계에 들어가기 전 선행 작업

용어집·캐릭터·관계 기준을 만들기 전에 다음 엔지니어링 기반을 먼저 확보합니다.

```text
롬/게임 구조 분석
→ 최소 한글 출력
→ 출력·진행 안전성 게이트
→ 일본어 원문 전체 추출
→ 안정 row_key
→ category/subcategory 분류
→ 게임 전용 검수 프로그램
→ 번역 전 0단계 기준자료
```

기술 안전성 게이트는 `workflow/EARLY-TEXT-RUNTIME-GATE.md`를 따릅니다. 한글이 표시되는지만 확인하지 않고 `[n]` 유지/삭제/이동/추가/개수 변경, 반각/전각, 가로폭, 최대 줄 수, RSC/인코딩, 다음 대사·선택지·다음 장면 진행을 확인합니다. 안전한 경로가 없으면 대량 번역으로 넘어가지 않습니다.

기술 게이트 통과 후 일본어 원문 전체를 추출해 번역문과 독립적인 안정 `row_key`를 만들고, `category/subcategory`로 문자열의 기능을 분류합니다. 단순 일본어 문장 덤프는 검수 원장으로 사용하지 않습니다.

용어집을 최종화하기 전에 `03_검수_프로그램`에 게임 전용 검수 프로그램을 준비합니다.

- 프로그램 구조·원장·최종 CSV 반입의 기본 베이스: `D:\Codex\# 검수 프로그램\EVE 고스트 에너미즈`
- 카테고리/세부분류 방식 참고: `D:\Codex\# 검수 프로그램\이상한 환상향 로터스 라비린스`

재사용 가능한 구조와 기능만 참고하고 EVE/로터스의 실제 게임 데이터·용어·관계·오프셋·확정 번역은 새 프로젝트에 섞지 않습니다.

그 뒤 `review/PRE-TRANSLATION-SETUP.md`를 적용해 캐릭터명·세계관/아이템/스킬/시스템 용어, 성격·말투, 화자 → 청자 방향별 관계, 방향별 반말/존댓말·호칭·예외와 근거 상태를 구축합니다. `A → B`와 `B → A`는 독립 규칙이며 대칭 관계를 기본 가정하지 않습니다.

### Google Drive는 휴대폰/웹 검수용 실제 작업장

PC 동기화 루트는 다음입니다.

```text
F:\내 드라이브\검수 프로그램\<게임명>\
├─ 01_최신_용어집
├─ 02_검수_필수파일
└─ 03_검수_수정_CSV
```

- `01_최신_용어집`: 최신 용어 기준과 confirmed/provisional/HOLD 상태
- `02_검수_필수파일`: 캐릭터·말투·방향별 관계·출력 규격·출처·1차/2차/3차 전용 지시문
- `03_검수_수정_CSV`: 게임 전용 검수 프로그램 최신 원장에서 내보낸 `row_key/category/subcategory`가 살아 있는 검수 CSV

이 구조는 PC를 켜두지 않고 휴대폰/웹 ChatGPT만으로 검수를 계속하기 위한 것입니다. Drive 동기화와 등록 파일 재조회가 끝나기 전에는 0단계 완료나 1차 시작 가능이라고 보고하지 않습니다.

검수는 전체 대사집을 1차 1,000행 → 2차 1,000행 → 3차 500행으로 각각 다시 훑습니다. 마지막에는 `<게임약칭>_최종대사_수정_누적.csv`를 게임 전용 검수 프로그램 최신 원장에 반입하고 모드/패치와 실제 플레이 검증으로 이어갑니다.'''
)
write(path, text)


# ---------------------------------------------------------------------------
# review/PRE-TRANSLATION-SETUP.md
# ---------------------------------------------------------------------------
path = "review/PRE-TRANSLATION-SETUP.md"
text = read(path)

text = replace_span(
    text,
    "# 번역 전 기준자료·용어집 선세팅 정책",
    "## 2. 대량 번역 시작 전 필수 기준자료",
    r'''# 번역 전 기준자료·용어집 선세팅 정책

이 문서는 **전체 일본어 원장과 카테고리, 게임 전용 검수 프로그램이 준비된 뒤** 대량 번역 직전에 수행하는 언어 0단계 정책입니다.

## 0단계보다 먼저 충족할 엔지니어링 선행조건

0단계 언어 기준자료를 프로젝트 시작 직후 상상으로 만들지 않습니다. 다음 순서를 먼저 통과합니다.

```text
최소 한글 출력
→ 출력·진행 안전성 시험
→ 전체 일본어 원문 추출
→ 안정 row_key 부여
→ category/subcategory 분류
→ 게임 전용 검수 프로그램 준비
→ 0단계 언어 기준자료 구축
```

출력·진행 안전성은 [출력·진행 안전성 사전검증](../workflow/EARLY-TEXT-RUNTIME-GATE.md)을 따릅니다. 가로 픽셀 폭·조건부 표시량·최대 줄 수·자동 줄바꿈, `[n]` 유지/삭제/이동/추가/개수 변경, 반각/전각·공백·문장부호, RSC/인코딩과 다음 대사·선택지·다음 장면 진행을 실제 게임에서 확인합니다.

원장은 단순 문장 목록이 아니라 최소한 `row_key`, 일본어 원문, `category`, `subcategory`, 가능하면 화자/청자와 보호 제어문자 정보를 가져야 합니다. `row_key`는 번역문이 바뀌어도 안정적으로 같은 레코드를 가리켜야 합니다.

게임 전용 검수 프로그램은 용어집 최종화보다 먼저 준비합니다. 기본 구조는 `D:\Codex\# 검수 프로그램\EVE 고스트 에너미즈`, 카테고리/세부분류 방식은 `D:\Codex\# 검수 프로그램\이상한 환상향 로터스 라비린스`를 참고할 수 있지만 게임별 데이터는 섞지 않습니다.

# 핵심 원칙

**전체 원장과 문자열 기능을 본 상태에서 용어집·캐릭터·관계·말투를 만들고, 그다음 대량 대사 번역을 시작합니다.**

관계는 화자 → 청자 방향별입니다. `A → B = 반말`, `B → A = 존댓말` 같은 비대칭 관계를 정상 케이스로 취급하며 `서로 반말` 같은 대칭 가정을 기본값으로 두지 않습니다.

---

## 1. 고정 검수 파이프라인

```text
최소 한글 출력 + 출력·진행 안전성 게이트
→ 전체 일본어 원문 추출 + 안정 row_key + category/subcategory
→ 게임 전용 검수 프로그램
→ 0단계 기준자료·용어집
→ Google Drive 최신 용어집·필수파일·분류 CSV 등록/동기화/재조회
→ 1차: 전체 대사집을 1,000행 단위로 기초 검수
→ 2차: 1차 결과 전체를 다시 1,000행 단위로 자연화·말투 검수
→ 3차: 2차 결과 전체를 다시 500행 단위로 최종 정밀검수
→ <게임약칭>_최종대사_수정_누적.csv
→ 게임별 검수 프로그램 최신 원장 반입
→ 모드/패치 생성
→ 실제 게임 플레이 검증
```

각 차수는 전체 대사집을 다시 훑는 별도 패스이며 작업 묶음 크기만 1,000 / 1,000 / 500으로 다릅니다.'''
)

text = replace_span(
    text,
    "## 8. 검수 프로그램 등록 전 합격 게이트",
    "## 9. 각 검수 단계의 역할",
    r'''## 8. Google Drive 등록 및 1차 시작 합격 게이트

로컬에서 0단계 기준자료 초안을 만들었다는 이유만으로 `0단계 완료` 또는 `1차 시작 가능`이라고 판정하지 않습니다.

Google Drive의 PC 동기화 상위 루트는 다음입니다.

```text
F:\내 드라이브\검수 프로그램
```

게임별 실사용 구조는 다음 세 역할을 기본으로 합니다.

```text
<게임명>\
├─ 01_최신_용어집
├─ 02_검수_필수파일
└─ 03_검수_수정_CSV
```

기존 게임 폴더가 다른 이름/세부구조를 이미 사용하면 중복 생성이나 강제 재배치 없이 동일 역할의 기존 폴더를 사용합니다.

1차 검수 전에 반드시 확인합니다.

- `01_최신_용어집`에 최신 용어 기준과 confirmed/provisional/HOLD 상태가 반영됨
- `02_검수_필수파일`에 캐릭터·말투·방향별 관계/존대/호칭, HOLD/출처, layout_profile과 `[n]`·반각/전각·가로폭·최대 줄 수·RSC 규칙이 있음
- 1차 1,000행, 2차 1,000행, 3차 500행 지시문이 물리적으로 분리되어 있음
- `03_검수_수정_CSV`에 최신 원장에서 내보낸 검수 CSV가 있고 `row_key`, 일본어 원문, `category`, `subcategory`가 유지됨
- Google Drive 동기화가 완료됨
- 등록한 파일을 다시 읽어 실제 반영을 확인함

로컬만 준비된 상태는 `LOCAL_DRAFT_ONLY`, Drive 반입/동기화가 남은 상태는 `DRIVE_REGISTRATION_PENDING`으로 기록합니다. Drive 접근이 불가능하면 로컬 파일만으로 정상 완료 처리하지 않습니다.

Drive 작업공간의 목적은 **PC를 켜두지 않고 휴대폰/웹 ChatGPT에서 검수할 수 있게 하는 것**입니다. 3차 완료 후 로컬 검수 프로그램으로 돌아오는 핵심 산출물은 `<게임약칭>_최종대사_수정_누적.csv`입니다.'''
)
write(path, text)


# ---------------------------------------------------------------------------
# templates/AGENTS.template.md
# ---------------------------------------------------------------------------
path = "templates/AGENTS.template.md"
text = read(path)

text = replace_span(
    text,
    "## Standard Project Layout",
    "## Font Selection",
    r'''## Standard Project Layout

신규 게임은 다른 실작업보다 먼저 다음 6개 폴더를 생성합니다.

```text
<PROJECT_ROOT>/
├─ 01_프로젝트_문서/
├─ 02_한글화_작업/
├─ 03_검수_프로그램/
├─ 04_최종_배포/
├─ 05_HD Pack/
└─ 버그 리포트/
```

- `01_프로젝트_문서`: 분석·설계·결정·인수인계 문서
- `02_한글화_작업`: 파일 분석, 추출·재삽입, 폰트/UI/대사, 빌더, staging
- `03_검수_프로그램`: 안정 원장, row_key, category/subcategory, 게임 전용 검수 프로그램, 최종 CSV 반입
- `04_최종_배포`: 최종 모드·패치·패처·배포 준비
- `05_HD Pack`: 폴더만 기본 생성. 사용자 명시 요청 전 실제 HD Pack 작업 금지
- `버그 리포트`: 재현 오류·실플레이 문제·증거

`.github`, `docs`, `source`, `staging`, `tests`, `tools`, `work`, `WORKLOG.md` 등은 프로젝트에 필요하면 추가하지만 공통 필수 6폴더로 취급하지 않습니다. 기존 프로젝트는 이 템플릿 때문에 강제 재배치하지 않습니다.

- HD Pack requested by user: `<YES_OR_NO>`
- HD Pack status: `<NOT_STARTED_OR_STATUS>`

HD Pack이 명시적으로 요청된 경우에만 `workflow/HD-PACK-PIPELINE.md`를 읽고 실제 작업을 시작합니다.'''
)

text = replace_span(
    text,
    "## Pre-Translation Baseline Gate",
    "## Public Worklog",
    r'''## Localization Lifecycle / Pre-Translation Gates

대량 번역 전에 아래 상태를 프로젝트별로 기록합니다.

- Minimal Korean output: `<NOT_STARTED / PASS / FAIL>`
- Runtime/layout gate: `<NOT_STARTED / PASS / CONDITIONAL / NEEDS_TECH_WORK>`
- Full Japanese corpus extraction: `<NOT_STARTED / IN_PROGRESS / READY>`
- Stable row_key ledger: `<NOT_STARTED / IN_PROGRESS / READY>`
- Category/subcategory classification: `<NOT_STARTED / IN_PROGRESS / READY>`
- Game-specific review program: `<NOT_STARTED / IN_PROGRESS / READY>`
- Pre-translation language baseline: `<NOT_STARTED / LOCAL_DRAFT_ONLY / DRIVE_REGISTRATION_PENDING / READY>`
- Google Drive workspace: `F:\내 드라이브\검수 프로그램\<GAME_FOLDER>`
- Drive sync/readback: `<NOT_STARTED / PENDING / VERIFIED>`

고정 순서:

```text
최소 한글 출력
→ [n]·반각/전각·가로폭·줄 수·RSC/인코딩·다음 장면 진행 검증
→ 전체 일본어 원문 추출
→ 안정 row_key
→ category/subcategory
→ 게임 전용 검수 프로그램
→ 용어·캐릭터·말투·화자→청자 방향별 관계 0단계
→ Google Drive 검수 작업장
→ 1차 1000 → 2차 1000 → 3차 500
→ 최종 누적 CSV 최신 원장 반입
→ 모드/패치 + 실기 검증
```

게임 전용 검수 프로그램은 용어집 최종화 전에 준비합니다. 구조는 `D:\Codex\# 검수 프로그램\EVE 고스트 에너미즈`, 카테고리화는 `D:\Codex\# 검수 프로그램\이상한 환상향 로터스 라비린스`를 참고할 수 있으나 다른 게임의 데이터·용어·관계·오프셋은 복사하지 않습니다.

0단계 기준자료에는 캐릭터 이름·세계관/아이템/스킬/시스템 용어, 성격·말투, 화자 → 청자 방향별 관계, 방향별 반말/존댓말·호칭·예외와 출처/HOLD 상태를 포함합니다. A → B와 B → A를 별도로 관리합니다.

Google Drive 실제 검수 작업공간:

```text
F:\내 드라이브\검수 프로그램\<게임명>\
├─ 01_최신_용어집
├─ 02_검수_필수파일
└─ 03_검수_수정_CSV
```

`03_검수_수정_CSV`의 대사집은 단순 문장 덤프가 아니라 최신 원장에서 내보낸 `row_key`, 일본어 원문, `category`, `subcategory`를 유지해야 합니다. `02_검수_필수파일`의 1차·2차·3차 지시문은 서로 섞지 않습니다.

Drive 동기화와 등록 파일 재조회가 끝나기 전에는 0단계 완료 또는 1차 시작 가능이라고 표시하지 않습니다. 3차 완료 후 `<게임약칭>_최종대사_수정_누적.csv`를 최신 원장에 반입합니다.'''
)

text = replace_span(
    text,
    "## Stage Workflow",
    "## Required Tests",
    r'''## Stage Workflow

프로젝트의 기본 라이프사이클은 다음과 같습니다.

```text
프로젝트 6폴더 생성
→ 롬/게임 구조 분석
→ 최소 한글 출력
→ 출력·진행 안전성 게이트
→ 전체 일본어 원문 추출
→ 안정 row_key + category/subcategory
→ 게임 전용 검수 프로그램
→ 번역 전 0단계 기준자료
→ Google Drive 세팅/동기화/재조회
→ 1차 1,000행 전체 검수
→ 2차 1,000행 전체 재검수
→ 3차 500행 전체 정밀검수
→ 최종 누적 CSV 최신 원장 반입
→ 정적 검증
→ 모드/패치 생성
→ 실제 플레이 검증
```

현재 프로젝트의 단계: `<CURRENT_LIFECYCLE_STAGE>`

HD Pack은 위 라이프사이클의 자동 후속 단계가 아닙니다. `05_HD Pack` 폴더는 준비하되 사용자 명시 요청 전 실제 제작을 시작하지 않습니다.

폰트 작업이 필요한 경우 `workflow/FONT-SELECTION-POLICY.md`의 `규격 조사 → 후보 약 3개 → 동일 조건 샘플 → 사용자 선택 → 전체 반영` 순서를 별도로 적용합니다.'''
)
write(path, text)


# ---------------------------------------------------------------------------
# Static contract verification
# ---------------------------------------------------------------------------
files = {
    "bootstrap": read("CODEX-LOCALIZATION-BOOTSTRAP.md"),
    "operating": read("workflow/PROJECT-OPERATING-MODEL.md"),
    "pre": read("review/PRE-TRANSLATION-SETUP.md"),
    "agents": read("templates/AGENTS.template.md"),
}

required_all = [
    "01_프로젝트_문서",
    "02_한글화_작업",
    "03_검수_프로그램",
    "04_최종_배포",
    "05_HD Pack",
    "버그 리포트",
    "row_key",
    "category",
    "subcategory",
    "F:\\내 드라이브\\검수 프로그램",
    "01_최신_용어집",
    "02_검수_필수파일",
    "03_검수_수정_CSV",
    "1,000행",
    "500행",
    "최종대사_수정_누적.csv",
]
for name, data in files.items():
    missing = [needle for needle in required_all if needle not in data]
    if missing:
        raise SystemExit(f"{name}: missing required lifecycle terms: {missing}")

bootstrap = files["bootstrap"]
order_terms = [
    "최소 한글 출력",
    "전체 일본어 원문 추출",
    "안정 row_key",
    "게임 전용 검수 프로그램",
    "번역 전 0단계",
    "Google Drive",
]
pos = [bootstrap.find(x) for x in order_terms]
if any(x < 0 for x in pos) or pos != sorted(pos):
    raise SystemExit(f"bootstrap lifecycle ordering not found in expected order: {list(zip(order_terms, pos))}")

# Old generic layout must not remain the canonical required layout in the two files that define new-project structure.
for name in ("operating", "agents"):
    data = files[name]
    old_required = "├─ .github/\n├─ docs/\n├─ source/\n├─ staging/\n├─ tests/\n├─ tools/\n├─ work/"
    if old_required in data:
        raise SystemExit(f"{name}: obsolete generic layout still present as a block")

# Preserve fixed review sizes and directional relationship semantics.
for name in ("bootstrap", "operating", "pre", "agents"):
    data = files[name]
    if "화자 → 청자" not in data and "A → B" not in data:
        raise SystemExit(f"{name}: directional relationship semantics missing")

print("LIFECYCLE_POLICY_PATCH_OK")
