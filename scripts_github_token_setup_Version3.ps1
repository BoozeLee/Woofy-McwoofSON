<#
GitHub Token Secure Setup (no secrets stored)
#>
Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

Write-Host "[INFO] Starting GitHub token setup scaffold."

if (-not (Test-Path ".env")) {
  "GITHUB_TOKEN=" | Out-File ".env" -Encoding UTF8
  Write-Host "[OK] .env placeholder created."
}

if (-not (Test-Path ".gitignore")) {
  "" | Out-File ".gitignore" -Encoding UTF8
}

$gitIgnore = Get-Content ".gitignore"
if ($gitIgnore -notcontains ".env") {
  Add-Content ".gitignore" ".env"
  Write-Host "[OK] Added .env to .gitignore."
}

$logFile = "knowledge-vault/CREDENTIAL_ROTATION_AND_HISTORY_CLEANUP.md"
if (-not (Test-Path "knowledge-vault")) { New-Item "knowledge-vault" -ItemType Directory | Out-Null }
if (-not (Test-Path $logFile)) { New-Item $logFile -ItemType File | Out-Null }

$content = Get-Content $logFile -Raw
if ($content -notmatch "## GitHub Token Rotations") {
  Add-Content $logFile "`n## GitHub Token Rotations"
  Add-Content $logFile "- $(Get-Date).ToUniversalTime().ToString('yyyy-MM-ddTHH:mm:ssZ') – Initialized rotation log (no token stored)."
  Write-Host "[OK] Rotation section initialized."
} else {
  Write-Host "[INFO] Rotation section already present."
}

Write-Host "[DONE] Scaffold complete. Store actual token ONLY as a GitHub secret."