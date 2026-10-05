param(
    [string]$CodexHome,
    [string]$ProjectRoot,
    [string]$SkillDirectory,
    [string]$SourceDirectory,
    [switch]$Force
)

$ErrorActionPreference = 'Stop'

# Keep this installer source ASCII-only for Windows PowerShell 5.1 compatibility.
$RawBase = 'https://raw.githubusercontent.com/Dollars-Archive/Dollars-Archive-kr-localization-archive/main'
$SkillUrl = "$RawBase/codex-auto-trigger/SKILL.md"
$AgentYamlUrl = "$RawBase/codex-auto-trigger/agents/openai.yaml"
$BootstrapUrl = "$RawBase/CODEX-LOCALIZATION-BOOTSTRAP.md"

function Get-Utf8Text([string]$Url) {
    # Windows PowerShell 5.1 can misdecode UTF-8 text returned through
    # Invoke-WebRequest.Content when the response has no BOM. Download raw bytes
    # and decode them explicitly as UTF-8 instead.
    $client = New-Object System.Net.WebClient
    try {
        $bytes = $client.DownloadData($Url)
    } finally {
        $client.Dispose()
    }
    if (-not $bytes -or $bytes.Length -eq 0) { throw "Empty response: $Url" }
    $text = [System.Text.Encoding]::UTF8.GetString($bytes)
    if ($text.Length -gt 0 -and [int][char]$text[0] -eq 0xFEFF) {
        $text = $text.Substring(1)
    }
    return $text
}

function Write-Utf8NoBom([string]$Path, [string]$Text) {
    $parent = Split-Path -Parent $Path
    if ($parent) { New-Item -ItemType Directory -Force -Path $parent | Out-Null }
    $utf8 = New-Object System.Text.UTF8Encoding($false)
    [System.IO.File]::WriteAllText($Path, $Text, $utf8)
}

# GitHub requires TLS 1.2 on older Windows PowerShell/.NET configurations.
try {
    [Net.ServicePointManager]::SecurityProtocol = [Net.ServicePointManager]::SecurityProtocol -bor [Net.SecurityProtocolType]::Tls12
} catch {
    # Continue on runtimes where this setting is unavailable.
}

# Fetch and validate everything before touching local Codex configuration.
if ($SourceDirectory) {
    $SkillText = [IO.File]::ReadAllText((Join-Path $SourceDirectory 'codex-auto-trigger\SKILL.md'))
    $AgentYamlText = [IO.File]::ReadAllText((Join-Path $SourceDirectory 'codex-auto-trigger\agents\openai.yaml'))
    $BootstrapText = [IO.File]::ReadAllText((Join-Path $SourceDirectory 'CODEX-LOCALIZATION-BOOTSTRAP.md'))
} else {
    $SkillText = Get-Utf8Text $SkillUrl
    $AgentYamlText = Get-Utf8Text $AgentYamlUrl
    $BootstrapText = Get-Utf8Text $BootstrapUrl
}

if ($SkillText -notmatch 'name:\s*dollars-localization-bootstrap') { throw 'Unexpected SKILL.md content.' }
if ($AgentYamlText -notmatch 'allow_implicit_invocation:\s*true') { throw 'Implicit invocation policy missing.' }
$StepNumbers = @([regex]::Matches($BootstrapText, '(?m)^### (\d+)\. ') | ForEach-Object { [int]$_.Groups[1].Value })
if (($StepNumbers -join ',') -ne ((1..16) -join ',')) { throw 'Expected the ordered 16-step bootstrap.' }
if ($BootstrapText -notmatch 'templates/PROJECT-INSTRUCTIONS\.md') { throw 'Common project instructions are missing.' }

$HomeDir = [Environment]::GetFolderPath('UserProfile')
if (-not $HomeDir) { throw 'Could not resolve user profile.' }

$SkillRoot = if ($SkillDirectory) { [IO.Path]::GetFullPath($SkillDirectory) } else { Join-Path $HomeDir '.agents\skills\dollars-localization-bootstrap' }
$SkillAgentsDir = Join-Path $SkillRoot 'agents'
$SkillFile = Join-Path $SkillRoot 'SKILL.md'
$SkillAgentYaml = Join-Path $SkillAgentsDir 'openai.yaml'
$SnapshotFile = Join-Path $SkillRoot 'CODEX-LOCALIZATION-BOOTSTRAP.snapshot.md'
$EnvironmentFile = Join-Path $SkillRoot 'environment.md'
if ($ProjectRoot) { $ProjectRoot = [IO.Path]::GetFullPath($ProjectRoot) }

if ([string]::IsNullOrWhiteSpace($CodexHome)) {
    $CodexHome = if ($env:CODEX_HOME) { $env:CODEX_HOME } else { Join-Path $HomeDir '.codex' }
}
$CodexHome = [System.IO.Path]::GetFullPath($CodexHome)
$OverrideFile = Join-Path $CodexHome 'AGENTS.override.md'
$AgentsFile = if (Test-Path $OverrideFile) { $OverrideFile } else { Join-Path $CodexHome 'AGENTS.md' }

$Start = '<!-- dollars-localization-bootstrap:start -->'
$End = '<!-- dollars-localization-bootstrap:end -->'
$Block = @"
$Start
## Game localization auto-bootstrap
When the user starts, continues, reviews, debugs, or plans a Korean game localization, translation review, localization patch, patch-engineering, or localization HD Pack task, load and follow the personal skill at:
$SkillFile
Do this before planning or modifying the localization project. Do not ask the user to provide the bootstrap GitHub link again. The skill must read the latest canonical GitHub bootstrap when available and use its local snapshot only as fallback.
This managed block applies only to game localization work and does not change unrelated Codex tasks.
$End
"@

$OldAgents = if (Test-Path $AgentsFile) { [System.IO.File]::ReadAllText($AgentsFile) } else { '' }
$EscStart = [regex]::Escape($Start)
$EscEnd = [regex]::Escape($End)
$Pattern = "$EscStart[\s\S]*?$EscEnd"
$StartCount = [regex]::Matches($OldAgents, $EscStart).Count
$EndCount = [regex]::Matches($OldAgents, $EscEnd).Count
if ($StartCount -ne $EndCount -or $StartCount -gt 1 -or ($StartCount -eq 1 -and $OldAgents -notmatch $Pattern)) {
    throw "Malformed or duplicate managed localization block in $AgentsFile. Inspect before reinstalling."
}

$Stamp = Get-Date -Format 'yyyyMMdd-HHmmss-fff'
if (Test-Path $SkillRoot) {
    $BackupSkill = "$SkillRoot.backup-$Stamp"
    Copy-Item -Recurse -Force $SkillRoot $BackupSkill
}

New-Item -ItemType Directory -Force -Path $SkillAgentsDir | Out-Null
Write-Utf8NoBom $SkillFile $SkillText
Write-Utf8NoBom $SkillAgentYaml $AgentYamlText
Write-Utf8NoBom $SnapshotFile $BootstrapText
if ($ProjectRoot) {
    Write-Utf8NoBom $EnvironmentFile "# Local environment`n`nProject root: $ProjectRoot`n`nUse this path instead of the author's example paths. Configure GitHub and Drive for the current user; do not publish to the author's repositories.`n"
} elseif (-not (Test-Path $EnvironmentFile)) {
    Write-Utf8NoBom $EnvironmentFile "# Local environment`n`nProject root: NOT_CONFIGURED`n`nAsk for the project root once before the first project. Use the current user's GitHub and Drive. The author's paths and repositories are examples.`n"
}

New-Item -ItemType Directory -Force -Path $CodexHome | Out-Null
if (Test-Path $AgentsFile) { Copy-Item -Force $AgentsFile "$AgentsFile.backup-$Stamp" }

if ($StartCount -eq 1) {
    $ManagedRegex = New-Object System.Text.RegularExpressions.Regex($Pattern)
    $Evaluator = [System.Text.RegularExpressions.MatchEvaluator]{ param($m) $Block }
    $NewAgents = $ManagedRegex.Replace($OldAgents, $Evaluator, 1)
} elseif ([string]::IsNullOrWhiteSpace($OldAgents)) {
    $NewAgents = $Block + [Environment]::NewLine
} else {
    $NewAgents = $OldAgents.TrimEnd() + [Environment]::NewLine + [Environment]::NewLine + $Block + [Environment]::NewLine
}

Write-Utf8NoBom $AgentsFile $NewAgents

# Fresh verification using ASCII anchors only.
$VerifyAgents = [System.IO.File]::ReadAllText($AgentsFile)
$VerifySkill = [System.IO.File]::ReadAllText($SkillFile)
$VerifySnapshot = [System.IO.File]::ReadAllText($SnapshotFile)

if ([regex]::Matches($VerifyAgents, $EscStart).Count -ne 1) { throw 'Global AGENTS managed block verification failed.' }
if ([regex]::Matches($VerifyAgents, $EscEnd).Count -ne 1) { throw 'Global AGENTS managed block end marker verification failed.' }
if ($VerifyAgents -notmatch [regex]::Escape($SkillFile)) { throw 'Installed skill path is missing from global AGENTS.' }
if ($VerifySkill -notmatch 'dollars-localization-bootstrap') { throw 'Installed skill verification failed.' }
if ($VerifySnapshot -ne $BootstrapText) { throw 'Bootstrap snapshot verification failed.' }
if (-not (Test-Path $EnvironmentFile)) { throw 'Local environment file verification failed.' }

$Hash = (Get-FileHash -Algorithm SHA256 $SnapshotFile).Hash.ToLowerInvariant()

Write-Host ''
Write-Host 'Installed Dollars game-localization auto-bootstrap.'
Write-Host "Skill: $SkillFile"
Write-Host "Global instructions: $AgentsFile"
Write-Host "Local environment: $EnvironmentFile"
Write-Host "Bootstrap snapshot SHA-256: $Hash"
Write-Host 'Restart Codex or start a new Codex session before testing the trigger.'
Write-Host 'Test with any normal game-localization request.'
