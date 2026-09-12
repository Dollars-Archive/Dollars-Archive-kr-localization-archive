# GitHub Pages 설치 가이드 표준

게임 한국어 패치 저장소에서 설치 설명서를 사용자에게 보여줄 때 사용하는 기본 운영 표준입니다.

이 문서의 목표는 `INSTALL.md`를 관리용 원본으로 유지하면서, 사용자는 GitHub Pages의 읽기 좋은 웹 설치 가이드를 보도록 만드는 것입니다.

> [!IMPORTANT]
> 앞으로 새 게임 한국어 패치 저장소에서 설치 가이드를 만들거나 기존 설치 가이드를 전면 정비할 때는 **별도 지시가 없으면 이 GitHub Pages 방식을 기본값으로 사용합니다.**
>
> 단, ChatGPT가 사용자 요청 없이 미래의 저장소를 스스로 수정할 수 있는 것은 아닙니다. 해당 게임 저장소 작업을 요청받은 세션에서 설치 가이드 작업이 포함되면, 사용자가 매번 “Pages로 만들어 달라”고 다시 말하지 않아도 이 표준을 적용합니다.

---

## 1. 기본 구조

저장소는 아래 구조를 기본으로 사용합니다.

```text
.
├─ README.md
├─ INSTALL.md
└─ docs/
   ├─ index.html
   └─ assets/
      ├─ style.css
      └─ app.js
```

역할은 다음과 같습니다.

- `INSTALL.md`
  - 설치 가이드의 **단일 원본**
  - 설치 절차, 경로, 주의사항, 스크린샷 설명을 여기서 관리
- `docs/index.html`
  - GitHub Pages용 웹 문서 껍데기
  - 제목, 상단 내비게이션, 목차, 플랫폼 배지 등 담당
- `docs/assets/style.css`
  - 게임별 포인트 색, 레이아웃, 경고 박스, 모바일/다크모드 스타일 담당
- `docs/assets/app.js`
  - `INSTALL.md`를 불러와 HTML로 렌더링
  - 목차, 코드 복사, GitHub callout 변환, 링크 보정 등 담당

> [!NOTE]
> 설치 내용을 `INSTALL.md`와 `docs/index.html`에 중복 작성하지 않습니다. 설치 절차는 반드시 `INSTALL.md` 한 곳에서만 관리합니다.

---

## 2. 사용자 동선

사용자가 GitHub의 투박한 Markdown 화면을 직접 볼 필요가 없도록 아래 링크를 Pages 주소로 연결합니다.

### README

README 상단과 다운로드/설치 안내에서 다음 형태로 연결합니다.

```md
자세한 적용 방법은 **[웹 설치 가이드](https://dollars-archive.github.io/<repo>/)**를 확인해 주세요.
```

### 최신 Release

최신 공개 Release의 `설치 가이드` 링크도 GitHub의 `INSTALL.md` 주소가 아니라 Pages 주소를 사용합니다.

```text
https://dollars-archive.github.io/<repo>/
```

### INSTALL.md

`INSTALL.md`는 삭제하지 않습니다.

- Pages가 읽는 원본 데이터
- GitHub에서 원문을 확인할 때 사용하는 문서
- Pages가 일시적으로 동작하지 않을 때의 fallback

으로 유지합니다.

---

## 3. GitHub Pages 설정

저장소에서 다음 순서로 설정합니다.

```text
Settings
→ Pages
→ Source: Deploy from a branch
→ Branch: main
→ Folder: /docs
→ Save
```

기본 주소는 다음 형식입니다.

```text
https://dollars-archive.github.io/<repository-name>/
```

Pages 빌드가 시작된 직후에는 잠시 404가 표시될 수 있으므로, Actions의 `pages build and deployment`가 성공했는지 확인합니다.

---

## 4. 공통 디자인 원칙

모든 게임은 같은 계열의 레이아웃을 사용하되 **게임마다 포인트 색을 다르게 지정**합니다.

공통 요소:

- 큰 게임명/설치 가이드 제목
- 현재 패치 버전 배지
- Windows / Android / Nintendo Switch 등 지원 플랫폼 배지
- 왼쪽 또는 상단 목차
- 읽기 쉬운 카드형 본문
- GitHub `[!IMPORTANT]`, `[!TIP]`, `[!WARNING]`, `[!CAUTION]`, `[!NOTE]` 스타일 변환
- 코드/경로 블록 복사 버튼
- 이미지 반응형 표시
- 모바일 레이아웃
- 다크모드
- 상단 `원문 보기` 및 `GitHub` 링크

### 게임별 테마

레이아웃과 기능은 공통으로 유지하고 다음 값만 게임별로 조정합니다.

- `--accent`
- `--accent-soft`
- 배경 radial gradient
- 버전 배지 색상
- 필요 시 게임의 분위기에 맞는 보조색

예시:

- `EVE rebirth terror`: 따뜻한 와인/적갈색 계열
- `EVE ghost enemies`: 청보라 + 옅은 청록 계열

이렇게 하면 같은 시리즈/브랜드의 통일감은 유지하면서 각 게임의 개성을 살릴 수 있습니다.

---

## 5. INSTALL.md 자동 렌더링

`docs/assets/app.js`는 저장소의 raw `INSTALL.md`를 읽어 렌더링합니다.

개념적으로 다음 흐름입니다.

```text
INSTALL.md 수정
→ main 반영
→ Pages에서 raw INSTALL.md 다시 로드
→ 웹 설치 가이드 내용 자동 반영
```

따라서 설치 절차를 수정할 때는 Pages HTML을 다시 작성할 필요가 없습니다.

### 권장 기능

- `fetch(..., { cache: 'no-store' })`
- Markdown 렌더러 사용
- 첫 번째 H1은 웹페이지 hero와 중복되므로 본문에서 숨김
- H2/H3 기반 목차 자동 생성
- 상대 링크를 GitHub blob 링크로 보정
- 외부 링크는 새 탭으로 열기
- 코드 블록에 복사 버튼 추가
- GitHub callout 문법을 카드형 박스로 변환

---

## 6. 새 게임 저장소에 적용하는 기본 절차

1. 기존 `INSTALL.md`가 있으면 내용을 먼저 검토하고 실제 설치 방식과 맞는지 확인
2. 없다면 `INSTALL.md`를 먼저 작성
3. 공용 Pages 템플릿의 `docs/` 세트를 복제
4. 저장소 이름, 게임명, raw `INSTALL.md` URL을 변경
5. 게임에 맞는 포인트 색을 선택
6. README의 설치 링크를 Pages로 변경
7. 최신 공개 Release의 설치 가이드 링크를 Pages로 변경
8. GitHub Pages를 `main /docs`로 활성화
9. Pages build 성공 확인
10. 실제 Pages 주소에서 PC와 모바일 표시 확인

> [!WARNING]
> Pages가 아직 활성화되지 않은 상태에서 README/Release 링크를 먼저 바꾸면 사용자가 일시적으로 404를 볼 수 있습니다. 가능하면 Pages 활성화와 배포 성공 확인 후 공개 링크를 전환합니다.

---

## 7. Release 수정 규칙

직접 Release 수정 액션이 없을 경우 기존 `GPT-GITHUB-OPERATIONS.md`의 방식대로 일회용 GitHub Actions + REST API를 사용합니다.

Release 전체 본문을 새 내용으로 덮어쓰기보다, 최신 Release를 다시 가져온 뒤 **기존 설치 가이드 URL만 Pages URL로 치환**하는 방식이 안전합니다.

수정 후 반드시:

1. workflow 성공 확인
2. Release 재조회로 새 링크 확인
3. 기존 `INSTALL.md` 링크가 남지 않았는지 확인
4. 일회용 workflow 삭제

까지 수행합니다.

---

## 8. 기본 운영 규칙

앞으로 한글패치 저장소에서 설치 가이드를 새로 만들거나 대규모로 정리할 때는 다음을 기본값으로 봅니다.

```text
INSTALL.md = 관리용 단일 원본
GitHub Pages = 사용자용 설치 설명서
README / Release = Pages로 들어가는 입구
게임별 차이 = 포인트 색과 최소한의 테마 조정
```

사용자가 특별히 `INSTALL.md`만 원하거나 Pages를 원하지 않는다고 말한 경우에만 이 방식을 생략합니다.

---

## 9. 현재 적용 사례

### EVE rebirth terror

```text
https://dollars-archive.github.io/eve-rebirth-terror-kr-patch/
```

- 와인/적갈색 계열 테마
- README 및 최신 Release에서 Pages로 연결
- `INSTALL.md` 자동 렌더링

### EVE ghost enemies

```text
https://dollars-archive.github.io/eve-ghost-enemies-kr-patch/
```

- 청보라 + 청록 계열 테마
- README 및 최신 Release에서 Pages로 연결
- `INSTALL.md` 자동 렌더링

두 게임의 구현을 기본 참고 사례로 사용하되, 이후 게임에서는 저장소 구조와 실제 설치 방법을 먼저 확인한 뒤 적용합니다.
