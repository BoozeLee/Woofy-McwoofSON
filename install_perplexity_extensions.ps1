# Install Perplexity VS Code Extensions
Write-Host "🚀 Installing Perplexity extensions for VS Code..." -ForegroundColor Green

# Extension IDs (check VS Code marketplace for exact IDs)
$extensions = @(
    "perplexity-ai.perplexity-ai",
    "perplexity.perplexity-search",
    "perplexity.perplexity-bot"
)

foreach ($extension in $extensions) {
    Write-Host "📦 Installing $extension..." -ForegroundColor Yellow
    code --install-extension $extension
    
    if ($LASTEXITCODE -eq 0) {
        Write-Host "✅ $extension installed successfully" -ForegroundColor Green
    } else {
        Write-Host "⚠️  $extension installation failed or not found" -ForegroundColor Red
    }
}

Write-Host "`n🎉 Extension installation complete!" -ForegroundColor Green
Write-Host "Restart VS Code to activate the extensions." -ForegroundColor Cyan