# <게임명> — 프로젝트 지시문

- 게임: <게임명>
- 기종·판본: <기종과 지원 판본>
- 프로젝트 루트: `<사용자가 선택한 작업 경로>/<게임명>`
- 시작하기: <파일 또는 실제 링크>
- 진행상태: <파일 또는 실제 링크>
- 허용 수정 범위: <경로>
- 보존할 성공 자료·사용자 확정값: <파일 또는 링크>

현재 사용자 지시와 승인 규칙을 우선한다. Codex와 GPT는 [최신 16단계 부트스트랩](https://github.com/Dollars-Archive/Dollars-Archive-kr-localization-archive/blob/main/CODEX-LOCALIZATION-BOOTSTRAP.md)과 [공통 작업 지시문](https://github.com/Dollars-Archive/Dollars-Archive-kr-localization-archive/blob/main/templates/PROJECT-INSTRUCTIONS.md)을 읽고 같은 순서로 진행한다. 프로젝트 시작하기에도 이 링크를 넣는다.

## 프로젝트 구조

게임명이 정해지면 기본 폴더부터 만든다. 사용자에게 `00_원본`과 `08_전용_에뮬` 경로를 안내한다. 원본·포터블 복사는 사용자가 한다. 원본이 없다고 경로를 반복해서 묻거나 폴더 생성을 미루지 않는다.

기본 폴더는 `00_` → `01_` → `02_` → `03_` → `04_` → `05_` → `06_` → `07_` → `08_` 번호 순서대로 하나씩 생성하고, 마지막에 `버그 리포트`를 만든다.

테스트 롬·ISO/CSO·사용자 확인용 빌드는 모두 해당 게임의 `04_테스트 파일`에 저장한다. 최소 한글 출력, 초반 500개 대사, 이미지·동영상 자막, 통합 테스트에도 같은 저장 위치를 사용한다.

폴더와 시작 안내·진행상태 파일을 만든 뒤 실제 생성 경로를 확인하고 **“폴더 준비 완료”**를 먼저 보고한다. `00_원본`에는 원본 롬, `08_전용_에뮬`에는 포터블 에뮬을 넣도록 안내한다. 준비 보고 전에는 원본 탐색이나 한글패치 여부 조사를 시작하지 않는다. 파일 복사 전에는 원본 등록·전용 에뮬 세팅 대기로 기록하고, 복사 완료 후 등록 파일을 확인해 다음 작업을 진행한다.

```text
00_원본
01_프로젝트_문서
02_한글화_작업
03_검수_프로그램
04_테스트 파일
05_한글 패치 배포
06_한글 패치 완료
07_HD Pack
08_전용_에뮬
버그 리포트
```

원본과 다른 게임 프로젝트는 수정하지 않는다. 기존 폴더를 강제로 재배치하지 않는다. HD Pack은 사용자 요청이 있을 때만 제작한다.

## 전용 에뮬

`08_전용_에뮬`은 이 게임 테스트용이다. 사용자가 포터블을 복사한 뒤 설정·메모리카드·세이브·게임별 설정을 프로젝트 안에 분리한다. PCSX2 등의 실제 저장 경로와 재실행 후 설정 유지를 확인한다. 공용 문서 폴더의 설정·기존 세이브는 변경하지 않는다. 복사 전에는 세팅 대기이며, 저장 경로를 확인하기 전에는 분리 완료로 표시하지 않는다.

## 이어서 작업할 때

진행상태를 읽고 현재 단계의 입력·완료 조건을 확인한다. 결과 파일과 검증 근거를 기록한다. 실기 확인이 필요한 단계는 사용자 확인 전까지 완료로 표시하지 않는다. 실제 빌드·저장·모델 호출 없이 수행했다고 보고하지 않는다.

Drive 검수는 [공통 양식](https://github.com/Dollars-Archive/Dollars-Archive-kr-localization-archive/blob/main/templates/drive-review/README.md)을 사용한다. 1·2·3차 모두 최대 500개 데이터 행이며, 기존 프로그램의 CSV 열을 보존한다. 1차 번역 → 2차 화자·관계·용어 확정 → 3차 출력 규격·말투 반영 순서를 지킨다.

검수 프로그램은 최신 원장을 자동으로 불러오고 대사를 실제 스토리 순서로 표시한다. 검수 프로그램은 각자 게임에 맞춰 직접 제작한다. 실기 확인 순서는 부트스트랩 10~16번을 따른다.

모델과 작업 배분은 현재 사용자 지시를 따른다. Web GPT·Oracle·외부 모델과 보조 에이전트는 현재 작업에서 명시적으로 요청받았을 때만 사용한다. 문서를 읽는 것만으로 모델 호출을 허가받은 것으로 보지 않는다.

공개 작업일지는 필요할 때 [기존 표준](https://github.com/Dollars-Archive/Dollars-Archive-kr-localization-archive/blob/main/workflow/PUBLIC-WORKLOG-STANDARD.md)을 적용한다.

## Public Patch README Form

아래 Dollars-Archive 허브·공략집 연결은 작성자 운영용이다. 다른 사용자는 본인 저장소용으로 수정하거나 생략하고 작성자 저장소에 게시하지 않는다.
### 새 패치 저장소의 공략집 등록 안내

신규 공개 패치 저장소 생성은 README의 공략집 등록 지침 연결까지 포함합니다. `templates/README.template.md`의 안내를 보존하고 `REPOSITORY_NAME`을 실제 저장소 이름으로 바꿉니다. `templates/ensure_guide_registration.py`를 `.github/scripts/ensure_guide_registration.py`, `templates/guide-registration.yml`을 `.github/workflows/guide-registration.yml`로 함께 복사합니다. 첫 커밋 전에 `python .github/scripts/ensure_guide_registration.py --repo Dollars-Archive/실제저장소이름`을 실행합니다.

워크플로는 기본 브랜치 푸시와 수동 실행 때 누락된 연결만 자동으로 추가합니다. 기존 안내가 있으면 아무것도 변경하지 않습니다. 신규 저장소 생성 완료 전에 지침 주소·patch_repo·워크플로 실행 성공을 확인하며, 사용자가 따로 지침을 첨부하도록 요구하지 않습니다. 공략 등록 요청은 https://github.com/Dollars-Archive/Game-Walkthrough-Archive/blob/main/REGISTER-GUIDE.md 를 직접 읽고 처리합니다. 별도 PAT 없이 자기 저장소의 GITHUB_TOKEN을 사용합니다. 세부 절차는 `workflow/PATCH-README-STANDARD.md`에 있습니다.


공개 패치 저장소의 대문을 만들 때 canonical bootstrap의 `templates/README.template.md`를 사용합니다. 게임 정보 표에는 개발사·장르·발매일·플레이타임을 포함합니다. `타이틀 한글화 / 메뉴·UI / 대사 / 이미지 번역 / 동영상 자막`의 다섯 제목과 각 항목의 숨김 주석 `kr-patch:state:`를 유지합니다. 공개 상태 문구는 추가하거나 복원하지 않습니다. 완료·일부·미작업·해당 없음으로 명시하고 근거 없는 완료 표시를 하지 않습니다. README의 표와 상태가 허브의 입력 원본이며 `kr-patch:game-info:v1`, `kr-patch:scope:v1` 주석을 보존합니다. 실제 패치 저장소에는 kr-patch topic을 붙이고 후보 조사 아카이브에는 붙이지 않습니다. 게임 정보·현재 범위를 허브 patches.yml에 중복 입력하지 않습니다. 세부 규칙은 `workflow/PATCH-README-STANDARD.md`를 읽습니다. 기존 README 변경 전 백업하고 이미지·호환성·설치 정보를 보존합니다.
