# GitHub Pages 설치 가이드 표준

**설치 내용은 `INSTALL.md` 한 곳에서 관리하고, 사용자는 Pages에서 읽게 합니다.** GPT·Codex는 아래 순서대로 작업합니다. 기존 게임의 설치 방법과 사이트 설정을 먼저 확인하고, 배포 성공 후 공개 링크를 바꿉니다.

새 설치 가이드는 별도 지시가 없으면 이 표준을 사용합니다. 사용자가 Pages를 원하지 않으면 생략합니다. 작업 범위·승인은 해당 세션과 프로젝트 규칙을 따릅니다.

## 1. 먼저 확인할 것

1. 대상 저장소의 README, `INSTALL.md`, 최신 공개 Release를 읽습니다.
2. 기본 브랜치, 기존 `docs/` 내용, Pages 배포 방식·경로·실제 URL을 확인합니다.
3. 기존 Actions, 커스텀 도메인, `CNAME`, 다른 웹페이지가 있으면 보존합니다. 기존 `docs/`를 통째로 덮어쓰지 않습니다.
4. 파일 수정 권한과 Pages 설정 권한은 별도로 확인합니다. `push: true`만으로 Pages 설정 변경까지 가능하다고 판단하지 않습니다.

GitHub 연결 도구를 우선 사용하고, 로컬에서 GitHub CLI가 연결되어 있다면 다음처럼 조회할 수 있습니다. `OWNER/REPO`는 실제 저장소로 바꿉니다.

```sh
gh api repos/OWNER/REPO --jq '{default_branch,permissions}'
gh api repos/OWNER/REPO/pages --jq '{html_url,status,build_type,source,cname}'
gh api repos/OWNER/REPO/releases/latest
```

Release가 없거나 Pages 조회가 실패하면 실제 응답을 확인합니다. 특히 Pages의 404만 보고 사이트가 없다고 단정하지 않습니다. 저장소 접근·토큰 권한·조직 정책 때문에 조회가 안 될 수도 있습니다. 권한 오류는 다른 경로로 우회하지 않고 사용자에게 필요한 조치를 안내합니다.

## 2. 새 사이트에 복제할 템플릿

실제 파일은 [설치 페이지 공통 템플릿](../templates/pages-install-guide/README.md)에 있습니다.

```text
INSTALL.md                     설치 내용의 단일 원본
docs/
├─ index.html                  웹페이지 제목·틀
└─ assets/
   ├─ config.js                저장소·브랜치·원문 경로·게임명·플랫폼·Release 링크
   ├─ core.js                  상대 경로·목차 처리
   ├─ app.js                   원문 읽기·렌더링·복사·오류 안내
   └─ style.css                반응형·다크모드·게임별 색
```

템플릿의 `docs/` 파일을 대상 저장소에 복제한 뒤 `config.js`와 HTML 제목·설명을 변경합니다. `INSTALL.template.md`는 새 원문이 필요할 때만 참고합니다. 기존 설치 내용은 보존합니다.

- `repository`: 실제 `소유자/저장소`
- `branch`: 확인한 원본 브랜치. `main`으로 추측하지 않습니다.
- `documentPath`: 저장소 루트 기준 원문 위치. 기본값 `INSTALL.md`
- `title`, `platforms`: 실제 게임명과 지원 플랫폼
- `releaseUrl`: 공개 정식 배포가 있으면 `https://github.com/OWNER/REPO/releases/latest`
- 색: `style.css`의 `--accent`, `--accent-soft` 등

공개 Release가 없으면 `releaseUrl`은 비워 둡니다. 여러 게임을 한 저장소에서 배포하거나 사전 공개 버전을 안내할 때는 해당 Release 주소를 명시합니다. `/releases/latest`는 최신 정식 공개 Release로 가는 링크이며 모든 프로젝트에 무조건 맞는 주소는 아닙니다.

템플릿은 게임 버전을 추측해서 표시하지 않습니다. 현재 버전이 필요하면 `INSTALL.md`에 실제 버전을 적습니다. 고정 버전 배지를 따로 만들 경우 갱신 책임도 정해야 합니다.

## 3. 원문을 읽는 두 방식

### A. GitHub 원본 직접 읽기 — 새 템플릿의 기본값

```text
INSTALL.md 수정 → 원본 브랜치 반영 → 페이지 새로고침 때 원본 다시 읽기
```

`sourceMode: 'raw'`로 설정합니다. 설치 내용 변경만으로 HTML을 다시 작성할 필요가 없습니다. CSS·HTML·JavaScript 수정은 Pages 재배포가 필요합니다. raw 서버·네트워크 사정에 따라 반영이 지연될 수 있으므로 실제 본문까지 확인합니다.

### B. Pages에 배포된 사본 읽기 — 기존 구현 유지 시

```text
INSTALL.md 수정 → docs/INSTALL.md 자동 복사 → Pages 빌드·배포 → 새로고침
```

`sourceMode: 'published'`, `publishedPath: './INSTALL.md'`로 설정합니다. `docs/INSTALL.md`는 자동 생성물이며 직접 수정하는 두 번째 원본으로 사용하지 않습니다.

이 방식에는 동기화와 재배포가 모두 필요합니다. `GITHUB_TOKEN`으로 만든 커밋은 Pages 빌드를 자동으로 시작하지 않으므로, 기존 동기화 workflow에 명시적 Pages 재빌드 요청 또는 Pages 배포 job이 있는지도 확인합니다. 사본만 바뀌고 배포가 빠지면 웹 내용은 그대로 남을 수 있습니다. [GitHub 게시 소스 안내](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)

기존 사이트를 이유 없이 다른 방식으로 이관하지 않습니다. 읽기 방식과 동기화 경로를 작업 기록에 남깁니다.

## 4. 게시 설정과 확인 순서

**이미 Pages가 있다면 기존 설정을 유지합니다.** 새 정적 사이트이며 `/docs`가 비어 있거나 설치 페이지용으로 합의된 경우에만 다음 설정을 기본으로 사용합니다.

```text
Settings → Pages → Deploy from a branch
→ 실제 게시 브랜치 → /docs → Save
```

소스 브랜치는 반드시 존재해야 합니다. 프로젝트 사이트의 일반 주소는 `https://OWNER.github.io/REPO/`지만, 대소문자·커스텀 도메인 등을 추측하지 말고 Pages 응답의 `html_url`을 사용합니다.

CLI로 새 Pages를 설정해야 할 경우, 기존 설정 조회 후 필요한 권한과 승인을 확인한 뒤 실행합니다. 아래는 **신규 생성 예시**이며 이미 운영 중인 사이트에 재실행하지 않습니다.

```sh
gh api --method POST repos/OWNER/REPO/pages \
  -f build_type=legacy \
  -f 'source[branch]=ACTUAL_BRANCH' \
  -f 'source[path]=/docs'
```

신규 Pages 생성에는 파일 쓰기 권한 외에 Pages·관리 권한이 필요할 수 있습니다. 접근 가능한 연결 방식에서 권한이 없다면 사용자가 Settings에서 설정하도록 안내합니다. 토큰·인증 설정을 임의로 바꾸지 않습니다. [GitHub Pages REST API](https://docs.github.com/en/rest/pages/pages)

기존 사이트가 GitHub Actions 방식이면 기존 workflow를 확인합니다. 배포 job은 `pages: write`, `id-token: write`, `github-pages` 환경, 빌드 artifact와 job 의존 관계가 필요합니다. 이 템플릿을 쓰기 위해 정상 운영 중인 Actions 사이트를 브랜치 방식으로 바꾸지 않습니다. [공식 Pages workflow 안내](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages)

작업 순서는 다음과 같습니다.

1. 기존 문서·사이트 설정 확인
2. `INSTALL.md` 작성·수정, 템플릿 설정과 상대 경로 검증
3. 승인된 파일을 게시 브랜치에 반영
4. 새 사이트만 Pages 활성화, 기존 사이트는 현재 배포 경로 사용
5. 해당 커밋의 Pages 빌드·배포 성공 확인
6. **실제 Pages URL에서 새 내용·이미지·다운로드 동선을 확인**
7. 확인된 Pages URL로 README와 해당 Release의 설치 링크 변경
8. 두 문서를 재조회하여 링크와 기존 내용 보존 확인

빌드 중에는 404가 나올 수 있습니다. 고정 시간만 기다리고 성공 처리하지 말고 배포 상태와 실제 응답을 확인합니다. 이 문서 아카이브 자체는 기존 `main /docs` 게시 설정을 유지합니다.

## 5. 렌더링·동선 기본값

- 읽기 쉬운 제목, 플랫폼 배지, H2/H3 목차
- GitHub callout 5종, 코드·경로 복사 버튼
- 작은 화면에서 세로 배치, 표 가로 스크롤, 이미지 반응형, 다크모드
- 공개 Release가 있으면 상단 `Release / 다운로드 ↗`, `GitHub ↗`
- 원문 보기 버튼은 일반 화면에 두지 않고, 읽기 실패 시 원본 설명서 링크 제공
- `fetch`는 `cache: 'no-store'`와 시간 매개변수 사용
- Markdown의 HTML은 정화 후 렌더링; 라이브러리는 버전 고정

상대 링크와 이미지 기준은 **웹페이지 위치가 아닌 원래 INSTALL.md 위치**입니다.

```text
INSTALL.md의 images/step.png → 같은 저장소·브랜치의 raw 이미지
INSTALL.md의 ../README.md   → 원문 위치를 기준으로 GitHub 문서 링크
#설치-방법                   → 페이지 안의 목차·제목 이동
```

상대 이미지에는 raw 주소를, 다른 파일 링크에는 GitHub blob 주소를 사용합니다. 설치 문서가 하위 폴더에 있거나 브랜치 이름에 `/`가 있어도 확인합니다. 외부 이미지·절대 URL은 유지하고, 위험한 URL·HTML 이벤트는 제거합니다.

## 6. README·Release 링크 수정

배포 확인 후 README에 다음처럼 연결합니다.

```md
자세한 적용 방법은 **[웹 설치 가이드](확인한_Pages_URL)**를 확인해 주세요.
```

Release는 수정 직전에 다시 조회하고 **기존 설치 가이드 링크만** 바꿉니다. 본문 전체를 기억에 의존해 재작성하거나 첨부파일·태그·공개 상태를 변경하지 않습니다. 수정은 가능한 GitHub 연결 도구 또는 인증된 `gh api PATCH`를 우선 사용합니다. 권한 거부를 우회하기 위해 workflow를 만들지 않습니다.

직접 수정 기능만 없고 필요한 권한·작업 승인이 있는 경우의 대체 절차는 [GPT → GitHub 작업 가이드](../GPT-GITHUB-OPERATIONS.md)를 참고합니다. 임시 workflow를 사용했다면 성공·Release 재조회·임시 파일 정리까지 확인합니다.

## 7. 완료 체크

- [ ] 저장소·브랜치·원문 위치·읽기 방식이 실제 구성과 맞음
- [ ] 기존 사이트·도메인·배포 설정을 보존함
- [ ] 공개 커밋의 배포 성공과 실제 Pages 본문을 확인함
- [ ] 새로고침 후 INSTALL.md의 수정 내용이 보임
- [ ] 상대 이미지와 문서 링크, 중복 제목 목차가 동작함
- [ ] 코드 복사, callout, 좁은 화면·다크모드 표시를 확인함
- [ ] Release 직행 링크가 해당 게임의 최신 또는 지정 배포로 연결됨
- [ ] 읽기 실패 안내와 원본 설명서 링크가 동작함
- [ ] README·Release 링크를 마지막에 바꾸고 재조회함

화면 검증을 수행하지 못한 경우에는 그 한계를 보고합니다. 테스트 결과와 실제 배포 결과를 구분하며, 파일 작성만으로 배포 완료라고 말하지 않습니다.

## 8. 현재 참고 사례

2026-10-05 확인 기준이며, 작업 시 다시 조회합니다.

| 게임 | 사이트 | 읽기 방식 |
| --- | --- | --- |
| EVE rebirth terror | [웹 설치 가이드](https://dollars-archive.github.io/eve-rebirth-terror-kr-patch/) | Pages의 `./INSTALL.md` 사본. 동기화 workflow가 복사·커밋 후 Pages 재빌드 요청 |
| EVE ghost enemies | [웹 설치 가이드](https://dollars-archive.github.io/eve-ghost-enemies-kr-patch/) | GitHub raw의 원본 `INSTALL.md` 직접 읽기 |

두 사이트 모두 Pages 상단에 Release / 다운로드 링크를 제공합니다. 기존 사례는 참고용이며, 다른 게임의 설치 방식·기종·버전까지 그대로 복사하지 않습니다.
