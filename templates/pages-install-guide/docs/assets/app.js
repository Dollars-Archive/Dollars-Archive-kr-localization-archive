import { config } from './config.js';
import { documentUrls, resolveDocumentReference, headingId } from './core.js';

function externalLink(link, url) {
  link.href = url;
  link.target = '_blank';
  link.rel = 'noopener noreferrer';
}

export function enhanceDocument(root, urls, toc) {
  const used = new Set();
  // 원문에 있는 id도 보존하고 자동 목차 id와의 충돌을 피합니다.
  root.querySelectorAll('[id]').forEach((node) => used.add(node.id));
  toc.replaceChildren();
  root.querySelectorAll('h2, h3').forEach((heading) => {
    if (!heading.id) {
      const base = headingId(heading.textContent);
      let id = base;
      let count = 2;
      while (used.has(id)) id = `${base}-${count++}`;
      heading.id = id;
      used.add(id);
    }
    const link = document.createElement('a');
    link.href = `#${heading.id}`;
    link.textContent = heading.textContent;
    if (heading.tagName === 'H3') link.className = 'sub';
    toc.append(link);
  });
  root.querySelectorAll('a[href]').forEach((link) => {
    const url = resolveDocumentReference(link.getAttribute('href'), 'link', urls);
    if (url === null) link.removeAttribute('href');
    else if (url.startsWith('#')) link.href = url;
    else externalLink(link, url);
  });
  root.querySelectorAll('img[src]').forEach((img) => {
    const url = resolveDocumentReference(img.getAttribute('src'), 'image', urls);
    if (url === null) img.removeAttribute('src');
    else img.src = url;
    img.loading = 'lazy';
    // srcset は Markdown 原本位置と異なるページ位置で解釈されるため使わない。
    img.removeAttribute('srcset');
  });
  const labels = { NOTE: '참고', TIP: '팁', IMPORTANT: '중요', WARNING: '주의', CAUTION: '경고' };
  root.querySelectorAll('blockquote').forEach((box) => {
    const first = box.querySelector('p');
    const match = first?.textContent.trim().match(/^\[!(NOTE|TIP|IMPORTANT|WARNING|CAUTION)\]/i);
    if (!match) return;
    const type = match[1].toUpperCase();
    box.className = `callout ${type.toLowerCase()}`;
    // 텍스트 노드에서 표식만 지워 본문의 링크·강조를 보존합니다.
    const walker = document.createTreeWalker(first, NodeFilter.SHOW_TEXT);
    const textNode = walker.nextNode();
    if (textNode) textNode.textContent = textNode.textContent.replace(/^\s*\[![A-Z]+\]\s*/i, '');
    const label = document.createElement('div');
    label.className = 'callout-label';
    label.textContent = labels[type];
    box.prepend(label);
  });
  root.querySelectorAll('pre').forEach((block) => {
    const code = block.querySelector('code');
    if (!code) return;
    const button = document.createElement('button');
    button.type = 'button';
    button.className = 'copy-btn';
    button.textContent = '복사';
    button.addEventListener('click', async () => {
      try {
        await navigator.clipboard.writeText(code.textContent);
        button.textContent = '복사됨';
      } catch {
        button.textContent = '직접 선택해 복사해 주세요';
      }
    });
    block.append(button);
  });
}

async function loadGuide() {
  const status = document.getElementById('status');
  let urls;
  try {
    urls = documentUrls(config, location.href);
    document.title = config.title;
    document.getElementById('title').textContent = config.title;
    const repo = document.getElementById('repo-link');
    externalLink(repo, `https://github.com/${config.repository}`);
    repo.hidden = false;
    if (config.releaseUrl) {
      if (!config.releaseUrl.startsWith(`https://github.com/${config.repository}/releases/`)) throw new Error('릴리스 설정을 확인하세요.');
      const release = document.getElementById('release-link');
      externalLink(release, config.releaseUrl);
      release.hidden = false;
    }
    const platforms = document.getElementById('platforms');
    for (const text of config.platforms) {
      const badge = document.createElement('span');
      badge.textContent = text;
      platforms.append(badge);
    }
    // CDN 실패도 본문 실패 안내에서 처리합니다.
    if (!globalThis.marked || !globalThis.DOMPurify) throw new Error('문서 렌더러를 불러오지 못했습니다.');
    const source = new URL(urls.source);
    source.searchParams.set('t', Date.now());
    const response = await fetch(source, { cache: 'no-store', signal: AbortSignal.timeout(20000) });
    if (!response.ok) throw new Error(`문서 응답 ${response.status}`);
    const markdown = (await response.text()).replace(/^\uFEFF/, '');
    if (!markdown.trim() || /^\s*(?:<!doctype html|<html)/i.test(markdown)) throw new Error('Markdown 문서를 확인하세요.');
    const root = document.getElementById('reader');
    root.innerHTML = DOMPurify.sanitize(marked.parse(markdown), { USE_PROFILES: { html: true } });
    enhanceDocument(root, urls, document.getElementById('toc'));
    status.hidden = true;
    root.hidden = false;
  } catch (error) {
    status.replaceChildren();
    const message = document.createElement('p');
    message.textContent = '설치 가이드를 불러오지 못했습니다. 잠시 후 새로고침해 주세요.';
    status.append(message);
    if (urls) {
      const fallback = document.createElement('a');
      fallback.textContent = '저장소 설치 설명서 확인 ↗';
      externalLink(fallback, urls.blob);
      status.append(fallback);
    }
    console.error('설치 가이드:', error.message);
  }
}

// defer CDN 스크립트와 모듈의 실행 순서가 달라도 모두 완료된 뒤 시작합니다.
if (document.readyState === 'complete') loadGuide();
else window.addEventListener('load', loadGuide, { once: true });
