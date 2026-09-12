param(
    [switch]$Force
)

$ErrorActionPreference = 'Stop'

$RawBase = 'https://raw.githubusercontent.com/Dollars-Archive/Dollars-Archive-kr-localization-archive/main'
$SkillUrl = "$RawBase/codex-auto-trigger/SKILL.md"
$AgentYamlUrl = "$RawBase/codex-auto-trigger/agents/openai.yaml"
$BootstrapUrl = "$RawBase/CODEX-LOCALIZATION-BOOTSTRAP.md"

function Get-Utf8Text([string]$Url) {
    $r = Invoke-WebRequest -UseBasicParsing -Uri $Url
    if (-not $r.Content) { throw "Empty response: $Url" }
    return [string]$r.Content
}

function Write-Utf8NoBom([string]$Path, [string]$Text) {
    $parent = Split-Path -Parent $Path
    if ($parent) { New-Item -ItemType Directory -Force -Path $parent | Out-Null }
    $utf8 = New-Object System.Text.UTF8Encoding($false)
    [System.IO.File]::WriteAllText($Path, $Text, $utf8)
}

# Fetch and validate everything before touching local Codex configuration.
$SkillText = Get-Utf8Text $SkillUrl
$AgentYamlText = Get-Utf8Text $AgentYamlUrl
$BootstrapText = Get-Utf8Text $BootstrapUrl

if ($SkillText -notmatch 'name:\s*dollars-localization-bootstrap') { throw 'Unexpected SKILL.md content.' }
if ($AgentYamlText -notmatch 'allow_implicit_invocation:\s*true') { throw 'Implicit invocation policy missing.' }
if ($BootstrapText -notmatch 'Codex 한글화 프로젝트 부트스트랩') { throw 'Unexpected bootstrap content.' }
if ($BootstrapText -notmatch 'D:\\Codex\\한글화 프로젝트') { throw 'Localization project root rule missing from bootstrap.' }

$HomeDir = [Environment]::GetFolderPath('UserProfile')
if (-not $HomeDir) { throw 'Could not resolve user profile.' }

$SkillRoot = Join-Path $HomeDir '.agents\skills\dollars-localization-bootstrap'
$SkillAgentsDir = Join-Path $SkillRoot 'agents'
$SkillFile = Join-Path $SkillRoot 'SKILL.md'
$SkillAgentYaml = Join-Path $SkillAgentsDir 'openai.yaml'
$SnapshotFile = Join-Path $SkillRoot 'CODEX-LOCALIZATION-BOOTSTRAP.snapshot.md'

$CodexHome = if ($env:CODEX_HOME) { $env:CODEX_HOME } else { Join-Path $HomeDir '.codex' }
$OverrideFile = Join-Path $CodexHome 'AGENTS.override.md'
$AgentsFile = if (Test-Path $OverrideFile) { $OverrideFile } else { Join-Path $CodexHome 'AGENTS.md' }

$Start = '<!-- dollars-localization-bootstrap:start -->'
$End = '<!-- dollars-localization-bootstrap:end -->'
$Block = @"
$Start
## Game localization auto-bootstrap
When the user starts, continues, reviews, debugs, or plans a game Korean-localization / 한글화 / 한글패치 task, load and follow the personal skill at:
`$SkillFile`
Do this before planning or modifying the localization project. Do not ask the user to provide the bootstrap GitHub link again. The skill must read the latest canonical GitHub bootstrap when available and use its local snapshot only as fallback.
This managed block applies only to game localization work and does not change unrelated Codex tasks.
$End
"@

$Stamp = Get-Date -Format 'yyyyMMdd-HHmmss'
if (Test-Path $SkillRoot) {
    $BackupSkill = "$SkillRoot.backup-$Stamp"
    Copy-Item -Recurse -Force $SkillRoot $BackupSkill
}

New-Item -ItemType Directory -Force -Path $SkillAgentsDir | Out-Null
Write-Utf8NoBom $SkillFile $SkillText
Write-Utf8NoBom $SkillAgentYaml $AgentYamlText
Write-Utf8NoBom $SnapshotFile $BootstrapText

New-Item -ItemType Directory -Force -Path $CodexHome | Out-Null
$OldAgents = if (Test-Path $AgentsFile) { [System.IO.File]::ReadAllText($AgentsFile) } else { '' }
if (Test-Path $AgentsFile) { Copy-Item -Force $AgentsFile "$AgentsFile.backup-$Stamp" }

$EscStart = [regex]::Escape($Start)
$EscEnd = [regex]::Escape($End)
$Pattern = "$EscStart[\s\S]*?$EscEnd"

if ([regex]::Matches($OldAgents, $EscStart).Count -gt 1 -or [regex]::Matches($OldAgents, $EscEnd).Count -gt 1) {
    throw "Multiple managed localization blocks found in $AgentsFile. Inspect before reinstalling."
}

if ($OldAgents -match $Pattern) {
    $NewAgents = [regex]::Replace($OldAgents, $Pattern, [System.Text.RegularExpressions.MatchEvaluator]{ param($m) $Block }, 1)
} elseif ([string]::IsNullOrWhiteSpace($OldAgents)) {
    $NewAgents = $Block + [Environment]::NewLine
} else {
    $NewAgents = $OldAgents.TrimEnd() + [Environment]::NewLine + [Environment]::NewLine + $Block + [Environment]::NewLine
}

Write-Utf8NoBom $AgentsFile $NewAgents

# Fresh verification.
$VerifyAgents = [System.IO.File]::ReadAllText($AgentsFile)
$VerifySkill = [System.IO.File]::ReadAllText($SkillFile)
$VerifySnapshot = [System.IO.File]::ReadAllText($SnapshotFile)

if ([regex]::Matches($VerifyAgents, $EscStart).Count -ne 1) { throw 'Global AGENTS managed block verification failed.' }
if ($VerifySkill -notmatch 'dollars-localization-bootstrap') { throw 'Installed skill verification failed.' }
if ($VerifySnapshot -notmatch 'Codex 한글화 프로젝트 부트스트랩') { throw 'Bootstrap snapshot verification failed.' }

$Hash = (Get-FileHash -Algorithm SHA256 $SnapshotFile).Hash.ToLowerInvariant()

Write-Host ''
Write-Host 'Installed Dollars game-localization auto-bootstrap.'
Write-Host "Skill: $SkillFile"
Write-Host "Global instructions: $AgentsFile"
Write-Host "Bootstrap snapshot SHA-256: $Hash"
Write-Host 'Restart Codex or start a new Codex session before testing the trigger.'
Write-Host 'Test phrase: 한글화 작업할 거야'
