export function documentUrls(config, pageUrl) {
  if (!/^[\w.-]+\/[\w.-]+$/.test(config.repository) || config.repository === 'OWNER/REPOSITORY') {
    throw new Error('저장소 설정을 확인하세요.');
  }
  const parts = config.documentPath.split('/');
  if (!config.branch || !parts.every((p) => p && p !== '.' && p !== '..' && !/[\\?#:]/.test(p))) {
    throw new Error('문서 경로 설정을 확인하세요.');
  }
  const branch = encodeURIComponent(config.branch);
  const path = parts.map(encodeURIComponent).join('/');
  const raw = `https://raw.githubusercontent.com/${config.repository}/${branch}/${path}`;
  const blob = `https://github.com/${config.repository}/blob/${branch}/${path}`;
  if (!['raw', 'published'].includes(config.sourceMode)) throw new Error('읽기 방식 설정을 확인하세요.');
  const source = config.sourceMode === 'published' ? new URL(config.publishedPath, pageUrl).href : raw;
  if (!/^https?:/.test(source)) throw new Error('웹 서버에서 실행하세요.');
  return { raw, blob, source };
}

export function resolveDocumentReference(reference, kind, urls) {
  const value = reference.trim();
  if (value.startsWith('#')) return value;
  if (/^(?:https?:|mailto:|tel:)/i.test(value) || value.startsWith('//')) return value;
  if (/^[a-z][a-z\d+.-]*:/i.test(value)) return null;
  // 이미지는 raw 파일, 다른 문서는 GitHub 화면으로 연결합니다.
  // 두 경우 모두 INSTALL.md의 원래 위치를 기준으로 상대 경로를 해석합니다.
  return new URL(value, kind === 'image' ? urls.raw : urls.blob).href;
}

export function headingId(text) {
  return text.trim().toLowerCase().replace(/[^\p{L}\p{N}\s-]/gu, '').replace(/\s+/g, '-') || 'section';
}
