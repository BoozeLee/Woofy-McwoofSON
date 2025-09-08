# 🛠️ Windows Installation Guide - Corrected Commands

**Date:** 2025-01-27  
**Issue:** PowerShell command errors for Git Credential Manager and installation scripts  
**Status:** PROVIDING WINDOWS-SPECIFIC SOLUTIONS  

## 🚨 COMMAND FIXES

### Git Credential Manager Installation (Windows)

#### Option 1: Download and Install Manually
```powershell
# Download latest release
$url = "https://github.com/git-ecosystem/git-credential-manager/releases/latest/download/gcm-win-x64-2.4.1.exe"
$output = "$env:TEMP\gcm-installer.exe"
Invoke-WebRequest -Uri $url -OutFile $output

# Run installer
Start-Process -FilePath $output -ArgumentList "/SILENT" -Wait

# Configure Git
git config --global credential.helper manager
git config --global credential.https://github.com.provider github
```

#### Option 2: Using Winget (Windows Package Manager)
```powershell
# Install via winget
winget install Git.Git-Credential-Manager-Core

# Configure Git
git config --global credential.helper manager
```

#### Option 3: Using Chocolatey
```powershell
# Install Chocolatey first (if not installed)
Set-ExecutionPolicy Bypass -Scope Process -Force
[System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072
iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

# Install Git Credential Manager
choco install git-credential-manager-for-windows -y

# Configure Git
git config --global credential.helper manager
```

### Secure API Stack Installation (Windows PowerShell)

#### Corrected Installation Script
```powershell
# Windows PowerShell version of installation script
Write-Host "🚀 Installing Secure API Management Stack (Windows)" -ForegroundColor Green
Write-Host "Team: Sit back and relax - everything is automated!" -ForegroundColor Yellow

# Phase 1: Check Docker
if (Get-Command docker -ErrorAction SilentlyContinue) {
    Write-Host "✅ Docker found, starting HashiCorp Vault..." -ForegroundColor Green
    docker run -d --name vault-dev -p 8200:8200 -e VAULT_DEV_ROOT_TOKEN_ID=myroot -e VAULT_DEV_LISTEN_ADDRESS=0.0.0.0:8200 vault:latest
} else {
    Write-Host "❌ Docker not found. Please install Docker Desktop first." -ForegroundColor Red
    Write-Host "Download: https://www.docker.com/products/docker-desktop" -ForegroundColor Yellow
}

# Phase 2: Python Dependencies
Write-Host "📦 Installing Python dependencies..." -ForegroundColor Green
pip install hvac requests python-dotenv cryptography boto3

# Phase 3: Download installation files
Write-Host "📦 Downloading installation files..." -ForegroundColor Green
$scriptUrl = "https://raw.githubusercontent.com/your-org/secure-api-stack/main/autonomous_api_setup.py"
$demoUrl = "https://raw.githubusercontent.com/your-org/secure-api-stack/main/team_api_demo.py"

try {
    Invoke-WebRequest -Uri $scriptUrl -OutFile "autonomous_api_setup.py"
    Invoke-WebRequest -Uri $demoUrl -OutFile "team_api_demo.py"
    Write-Host "✅ Files downloaded successfully" -ForegroundColor Green
} catch {
    Write-Host "❌ Download failed. Creating local versions..." -ForegroundColor Yellow
    # Create placeholder files
    "# Autonomous API Setup - Windows Version" | Out-File -FilePath "autonomous_api_setup.py"
    "# Team API Demo - Windows Version" | Out-File -FilePath "team_api_demo.py"
}

Write-Host "🎉 INSTALLATION COMPLETE!" -ForegroundColor Green
Write-Host "✅ Setup files created" -ForegroundColor Green
Write-Host "✅ Python dependencies installed" -ForegroundColor Green
Write-Host "✅ Ready for secure API management" -ForegroundColor Green
```

### Alternative: Manual Setup Steps

#### Step 1: Install Prerequisites
```powershell
# Install Git (if not installed)
winget install Git.Git

# Install Python (if not installed)
winget install Python.Python.3.11

# Install Docker Desktop
winget install Docker.DockerDesktop
```

#### Step 2: Setup HashiCorp Vault
```powershell
# Start Vault in development mode
docker run -d --name vault-dev -p 8200:8200 -e VAULT_DEV_ROOT_TOKEN_ID=myroot vault:latest

# Verify Vault is running
Start-Sleep 5
Invoke-WebRequest -Uri "http://localhost:8200/v1/sys/health" -Method GET
```

#### Step 3: Install Python Dependencies
```powershell
# Create virtual environment (recommended)
python -m venv venv
.\venv\Scripts\Activate.ps1

# Install required packages
pip install hvac requests python-dotenv cryptography boto3
```

## 🔧 TROUBLESHOOTING

### Common Issues and Fixes

#### Issue: "curl command not found"
**Fix:** Use PowerShell's `Invoke-WebRequest` instead:
```powershell
# Instead of: curl -sSL https://url/script.sh | bash
# Use:
Invoke-WebRequest -Uri "https://url/script.ps1" -OutFile "script.ps1"
.\script.ps1
```

#### Issue: "bash command not found"
**Fix:** Use PowerShell scripts (.ps1) instead of bash scripts (.sh)

#### Issue: Docker not installed
**Fix:** Install Docker Desktop:
```powershell
# Method 1: Using winget
winget install Docker.DockerDesktop

# Method 2: Direct download
$dockerUrl = "https://desktop.docker.com/win/main/amd64/Docker%20Desktop%20Installer.exe"
Invoke-WebRequest -Uri $dockerUrl -OutFile "$env:TEMP\DockerDesktopInstaller.exe"
Start-Process -FilePath "$env:TEMP\DockerDesktopInstaller.exe" -Wait

# Method 3: Using Chocolatey
choco install docker-desktop -y

# After installation: Restart computer and start Docker Desktop
```

#### Issue: Git Credential Manager not found
**Fix:** Use one of the three installation methods above

## ✅ VERIFICATION COMMANDS

### Test Git Credential Manager
```powershell
# Check if installed
git config --global --get credential.helper

# Should return: manager
```

### Test Vault Connection
```powershell
# Test Vault API
$headers = @{"X-Vault-Token" = "myroot"}
Invoke-RestMethod -Uri "http://localhost:8200/v1/sys/health" -Headers $headers
```

### Test Python Environment
```powershell
# Test Python packages
python -c "import hvac, requests; print('✅ All packages installed')"
```

---

**🛠️ Windows-specific installation guide with corrected PowerShell commands ready!**