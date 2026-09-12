export function sanitizeMarkdownPath(value) {
  if (!value || typeof value !== 'string') return null;
  let decoded;
  try { decoded = decodeURIComponent(value).trim(); } catch { return null; }
  if (!decoded.endsWith('.md')) return null;
  if (decoded.startsWith('/') || decoded.includes('\\') || decoded.includes('://')) return null;
  const parts = decoded.split('/');
  if (parts.some((part) => !part || part === '.' || part === '..')) return null;
  return parts.join('/');
}

export function resolveRepoPath(currentFile, href) {
  if (!href || href.startsWith('#') || href.startsWith('http://') || href.startsWith('https://') || href.startsWith('mailto:')) return href;
  const baseParts = currentFile.split('/');
  baseParts.pop();
  const combined = [...baseParts, ...href.split('/')];
  const out = [];
  for (const part of combined) {
    if (!part || part === '.') continue;
    if (part === '..') out.pop();
    else out.push(part);
  }
  return out.join('/');
}
