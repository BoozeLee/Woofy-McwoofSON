# 🔐 Git Credential Manager Auto-Installation Script
# Created by Amazon Q for WOOFY McWOOFSON project
# Run this script when Big Boss is away for automated installation

Write-Host "🐕 WOOFY McWOOFSON - Git Credential Manager Installation" -ForegroundColor Green

# Download Git Credential Manager
$downloadUrl = "https://github.com/git-ecosystem/git-credential-manager/releases/latest/download/gcm-win-x86-2.4.1.exe"
$installerPath = "$env:TEMP\gcm-installer.exe"

Write-Host "📥 Downloading Git Credential Manager..." -ForegroundColor Yellow
try {
    Invoke-WebRequest -Uri $downloadUrl -OutFile $installerPath -UseBasicParsing
    Write-Host "✅ Download completed successfully" -ForegroundColor Green
} catch {
    Write-Host "❌ Download failed: $($_.Exception.Message)" -ForegroundColor Red
    exit 1
}

# Install silently
Write-Host "🔧 Installing Git Credential Manager..." -ForegroundColor Yellow
try {
    Start-Process -FilePath $installerPath -ArgumentList "/SILENT" -Wait
    Write-Host "✅ Installation completed successfully" -ForegroundColor Green
} catch {
    Write-Host "❌ Installation failed: $($_.Exception.Message)" -ForegroundColor Red
    exit 1
}

# Configure Git
Write-Host "⚙️ Configuring Git..." -ForegroundColor Yellow
git config --global credential.helper manager
git config --global credential.https://github.com.provider github

Write-Host "🎉 Git Credential Manager setup complete!" -ForegroundColor Green
Write-Host "🐕 WOOFY says: Secure authentication ready for repository operations!" -ForegroundColor Cyan

# Cleanup
Remove-Item $installerPath -Force -ErrorAction SilentlyContinue