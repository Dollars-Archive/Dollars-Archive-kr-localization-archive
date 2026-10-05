import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import { spawnSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';
import test from 'node:test';
import { nativeFixture } from './native-helpers.mjs';

test('MCP initializes through a Windows profile junction', { skip: process.platform !== 'win32' }, async t => {
  const fixture = await nativeFixture(t);
  const source = fileURLToPath(new URL('../', import.meta.url));
  const runtime = path.join(fixture.root, 'real-runtime');
  fs.mkdirSync(runtime);
  for (const name of ['scripts', 'lib', 'assets']) {
    fs.cpSync(path.join(source, name), path.join(runtime, name), { recursive: true });
  }
  fs.copyFileSync(path.join(source, 'plugin.json'), path.join(runtime, 'plugin.json'));
  const alias = path.join(fixture.root, 'profile-junction');
  fs.symlinkSync(runtime, alias, 'junction');
  const env = { ...process.env };
  for (const key of ['CODEX_THREAD_ID', 'CODEX_APP_TOOLS_PIPE_PATH', 'CLAUDE_CODE_MESSAGING_SOCKET', 'CLAUDE_CODE_MESSAGING_TOKEN']) delete env[key];
  env.CODEX_CLAUDE_BRIDGE_STATE_DIR = fixture.stateDir;
  const result = spawnSync(process.execPath, ['./scripts/mcp.mjs'], {
    cwd: alias, env, windowsHide: true, encoding: 'utf8', timeout: 5000,
    input: JSON.stringify({ jsonrpc: '2.0', id: 1, method: 'initialize', params: {
      protocolVersion: '2024-11-05', capabilities: {}, clientInfo: { name: 'junction-test', version: '1' },
    } }) + '\n',
  });
  assert.equal(result.error, undefined);
  assert.equal(result.status, 0, result.stderr);
  const response = JSON.parse(result.stdout.trim());
  assert.equal(response.id, 1);
  assert.equal(response.result.serverInfo.name, 'codex-claude-desktop-bridge');
});
