$ErrorActionPreference = 'Stop'
$repoRoot = (Resolve-Path (Join-Path $PSScriptRoot '../..')).Path
$testRoot = Join-Path ([IO.Path]::GetTempPath()) ('install-test-' + [guid]::NewGuid().ToString('N'))
$testCodex = Join-Path $testRoot 'codex'
$testSkill = Join-Path $testRoot 'skill'
$testProject = Join-Path $testRoot 'projects with spaces'
New-Item -ItemType Directory -Path $testCodex -Force | Out-Null
$overridePath = Join-Path $testCodex 'AGENTS.override.md'
[IO.File]::WriteAllText($overridePath, "# Existing rules`nKeep this instruction.`n")
$installer = Join-Path $repoRoot 'codex-auto-trigger/install-global.ps1'
function Invoke-TestInstall([bool]$WithProject) {
    $params = @('-NoProfile','-ExecutionPolicy','Bypass','-File',$installer,'-CodexHome',$testCodex,'-SkillDirectory',$testSkill,'-SourceDirectory',$repoRoot)
    if ($WithProject) { $params += @('-ProjectRoot',$testProject) }
    $output = & powershell.exe @params 2>&1
    if ($LASTEXITCODE -ne 0) { throw ($output | Out-String) }
}
Invoke-TestInstall $true
$agents = [IO.File]::ReadAllText($overridePath)
if (-not $agents.Contains('Keep this instruction.')) { throw 'Existing instruction lost.' }
if (-not (Test-Path "$overridePath.backup-*")) { throw 'Backup missing.' }
if (-not ([IO.File]::ReadAllText((Join-Path $testSkill 'environment.md'))).Contains($testProject)) { throw 'Custom project path lost.' }
Write-Output 'PASS: Windows PowerShell 5.1 install, custom paths, override and backup preservation.'
Invoke-TestInstall $false
$agents = [IO.File]::ReadAllText($overridePath)
if ([regex]::Matches($agents,'<!-- dollars-localization-bootstrap:start -->').Count -ne 1) { throw 'Duplicate managed block.' }
if (-not ([IO.File]::ReadAllText((Join-Path $testSkill 'environment.md'))).Contains($testProject)) { throw 'Environment lost on reinstall.' }
Write-Output 'PASS: Reinstall keeps one block and preserves project settings.'
$badCodex = Join-Path $testRoot 'malformed'
$badSkill = Join-Path $testRoot 'must-not-create'
New-Item -ItemType Directory -Path $badCodex | Out-Null
$badFile = Join-Path $badCodex 'AGENTS.md'
$badText = '# Existing rules' + "`n" + '<!-- dollars-localization-bootstrap:start -->'
[IO.File]::WriteAllText($badFile,$badText)
$params = @('-NoProfile','-ExecutionPolicy','Bypass','-File',$installer,'-CodexHome',$badCodex,'-SkillDirectory',$badSkill,'-SourceDirectory',$repoRoot)
$output = & powershell.exe @params 2>&1
if ($LASTEXITCODE -eq 0 -or (Test-Path $badSkill) -or [IO.File]::ReadAllText($badFile) -ne $badText) { throw 'Malformed block modified local files.' }
Write-Output 'PASS: Malformed managed block rejected before writes.'
$unconfiguredCodex = Join-Path $testRoot 'unconfigured-codex'
$unconfiguredSkill = Join-Path $testRoot 'unconfigured-skill'
$params = @('-NoProfile','-ExecutionPolicy','Bypass','-File',$installer,'-CodexHome',$unconfiguredCodex,'-SkillDirectory',$unconfiguredSkill,'-SourceDirectory',$repoRoot)
$output = & powershell.exe @params 2>&1
if ($LASTEXITCODE -ne 0) { throw ($output | Out-String) }
if (-not ([IO.File]::ReadAllText((Join-Path $unconfiguredSkill 'environment.md'))).Contains('NOT_CONFIGURED')) { throw 'Unexpected author path default.' }
Write-Output 'PASS: Unconfigured user prompts for own path, no author path default.'
Write-Output "Test workspace: $testRoot"
