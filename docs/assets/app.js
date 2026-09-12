import { sanitizeMarkdownPath, resolveRepoPath } from './core.js';

const REPO = 'Dollars-Archive/Dollars-Archive-kr-localization-archive';
const RAW_BASE = `https://raw.githubusercontent.com/${REPO}/main/`;
const BLOB_BASE = `https://github.com/${REPO}/blob/main/`;

const docs = [
  {
    group: 'GPT / GITHUB',
    title: 'GPT → GitHub 작업 가이드',
    file: 'GPT-GITHUB-OPERATIONS.md',
    description: 'GPT가 GitHub 파일·Release를 안전하게 수정하고 검증하는 운영 절차.',
  },
  {
    group: 'LOCALIZATION BOOTSTRAP',
    title: 'Codex 한글화 프로젝트 부트스트랩',
    file: 'CODEX-LOCALIZATION-BOOTSTRAP.md',
    description: '게임별 프로젝트 구조, 검수 단계, 자료 관리와 에이전트 역할 분담.',
  },
  {
    group: 'PROJECT / WORKLOG',
    title: '공개 작업일지 운영 표준',
    file: 'workflow/PUBLIC-WORKLOG-STANDARD.md',
    description: '진행 중 프로젝트의 공개 제작일지와 노하우 비공개 경계를 관리하는 표준.',
  },
  {
    group: 'PAGES / DOCUMENTATION',
    title: 'GitHub Pages 설치 가이드 표준',
    file: 'workflow/GITHUB-PAGES-INSTALL-GUIDE-STANDARD.md',
    description: 'INSTALL.md 단일 원본과 게임별 테마 Pages 설명서를 연결하는 표준.',
  },
  {
    group: 'NINTENDO SWITCH',
    title: 'Nintendo Switch 한국어 패치 제작 워크플로',
    file: 'switch/SWITCH-KOREAN-LOCALIZATION-GUIDE.md',
    description: 'RomFS, 패처, 검증, LayeredFS와 실기 테스트까지 이어지는 제작 흐름.',
  },
];

function viewerUrl(file) {
  return `doc.html?file=${encodeURIComponent(file)}`;
}

function renderIndex() {
  const grid = document.getElementById('doc-grid');
  if (!grid) return;
  grid.innerHTML = docs.map((doc) => `
    <a class="doc-card" href="${viewerUrl(doc.file)}">
      <div class="kicker">${doc.group}</div>
      <h3>${doc.title}</h3>
      <p>${doc.description}</p>
      <div class="path">${doc.file}</div>
    </a>
  `).join('');
}

function slugify(text) {
  return text.toLowerCase().trim().replace(/[`*_~]/g, '').replace(/[^\p{L}\p{N}\s-]/gu, '').replace(/\s+/g, '-').replace(/-+/g, '-').replace(/^-|-$/g, '') || 'section';
}

function decorateCallouts(root) {
  const labels = { IMPORTANT:'중요', TIP:'팁', WARNING:'주의', CAUTION:'경고', NOTE:'참고' };
  root.querySelectorAll('blockquote').forEach((blockquote) => {
    const first = blockquote.querySelector('p');
    if (!first) return;
    const match = first.textContent.trim().match(/^\[!(IMPORTANT|TIP|WARNING|CAUTION|NOTE)\]/i);
    if (!match) return;
    const type = match[1].toUpperCase();
    blockquote.classList.add('callout', type.toLowerCase());
    first.innerHTML = first.innerHTML.replace(/^\[!(IMPORTANT|TIP|WARNING|CAUTION|NOTE)\]\s*/i, '');
    const label = document.createElement('div');
    label.className = 'callout-label';
    label.textContent = labels[type];
    blockquote.prepend(label);
    if (!first.textContent.trim()) first.remove();
  });
}

function buildToc(root) {
  const toc = document.getElementById('toc');
  if (!toc) return;
  const used = new Map();
  const headings = [...root.querySelectorAll('h2, h3')];
  toc.innerHTML = '';
  headings.forEach((heading) => {
    let id = slugify(heading.textContent);
    const n = (used.get(id) || 0) + 1;
    used.set(id, n);
    if (n > 1) id = `${id}-${n}`;
    heading.id = id;
    const link = document.createElement('a');
    link.href = `#${id}`;
    link.textContent = heading.textContent;
    if (heading.tagName === 'H3') link.classList.add('sub');
    toc.appendChild(link);
  });
  if ('IntersectionObserver' in window && headings.length) {
    const links = new Map([...toc.querySelectorAll('a')].map((a) => [a.getAttribute('href').slice(1), a]));
    const observer = new IntersectionObserver((entries) => {
      const visible = entries.filter((entry) => entry.isIntersecting).sort((a,b) => a.boundingClientRect.top - b.boundingClientRect.top)[0];
      if (!visible) return;
      links.forEach((link) => link.classList.remove('active'));
      links.get(visible.target.id)?.classList.add('active');
    }, { rootMargin:'-90px 0px -70% 0px', threshold:0 });
    headings.forEach((heading) => observer.observe(heading));
  }
}

function enhanceLinks(root, currentFile) {
  root.querySelectorAll('a[href]').forEach((a) => {
    const href = a.getAttribute('href');
    if (!href || href.startsWith('#') || href.startsWith('http://') || href.startsWith('https://') || href.startsWith('mailto:')) return;
    const resolved = resolveRepoPath(currentFile, href);
    if (resolved.endsWith('.md')) a.href = viewerUrl(resolved);
    else a.href = BLOB_BASE + resolved;
  });
  root.querySelectorAll('a[href^="http"]').forEach((a) => { a.target='_blank'; a.rel='noreferrer'; });
  root.querySelectorAll('img[src]').forEach((img) => {
    const src = img.getAttribute('src');
    if (!src || src.startsWith('http://') || src.startsWith('https://') || src.startsWith('data:')) return;
    img.src = RAW_BASE + resolveRepoPath(currentFile, src);
  });
}

function addCopyButtons(root) {
  root.querySelectorAll('pre').forEach((pre) => {
    const code = pre.querySelector('code');
    if (!code) return;
    const button = document.createElement('button');
    button.type='button'; button.className='copy-btn'; button.textContent='복사';
    button.addEventListener('click', async () => {
      try { await navigator.clipboard.writeText(code.textContent); button.textContent='완료'; }
      catch { button.textContent='실패'; }
      setTimeout(() => { button.textContent='복사'; }, 1200);
    });
    pre.appendChild(button);
  });
}

async function renderDoc() {
  const params = new URLSearchParams(location.search);
  const file = sanitizeMarkdownPath(params.get('file'));
  const reader = document.getElementById('reader');
  const status = document.getElementById('status');
  const rawLink = document.getElementById('raw-link');
  const pageTitle = document.getElementById('page-title');
  const pagePath = document.getElementById('page-path');

  if (!file) {
    status.innerHTML = '올바른 Markdown 문서 경로가 아닙니다.<br><a href="./">문서 목록으로 돌아가기</a>';
    return;
  }
  rawLink.href = BLOB_BASE + file;
  pagePath.textContent = file;

  try {
    const response = await fetch(`${RAW_BASE}${file}?t=${Date.now()}`, { cache:'no-store' });
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    const markdown = await response.text();
    if (!window.marked) throw new Error('Markdown renderer unavailable');
    const title = markdown.match(/^#\s+(.+)$/m)?.[1]?.trim() || file.split('/').pop().replace(/\.md$/i,'');
    pageTitle.textContent = title;
    document.title = `${title} · Dollars Archive`;
    marked.setOptions({ gfm:true, breaks:false, mangle:false, headerIds:false });
    reader.innerHTML = marked.parse(markdown);
    decorateCallouts(reader);
    enhanceLinks(reader, file);
    addCopyButtons(reader);
    buildToc(reader);
    status.hidden = true;
    reader.hidden = false;
  } catch (error) {
    console.error(error);
    status.innerHTML = `문서를 불러오지 못했습니다.<br><a href="${BLOB_BASE}${file}" target="_blank" rel="noreferrer">GitHub 원문에서 보기 ↗</a>`;
  }
}

if (document.body.dataset.page === 'index') renderIndex();
if (document.body.dataset.page === 'doc') renderDoc();
