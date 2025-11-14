# Quick script to commit and push to GitHub for Render deployment
# Run this in PowerShell in the codejudge folder

Write-Host "=== Committing changes for Render deployment ===" -ForegroundColor Green

git add .
if ($LASTEXITCODE -ne 0) {
    Write-Host "Git add failed. Make sure Git is installed and in PATH." -ForegroundColor Red
    exit 1
}

git commit -m "Prepare for Render free-tier deployment: update settings, add .env.example, deployment guide"
if ($LASTEXITCODE -ne 0) {
    Write-Host "Git commit failed." -ForegroundColor Red
    exit 1
}

git push
if ($LASTEXITCODE -ne 0) {
    Write-Host "Git push failed." -ForegroundColor Red
    exit 1
}

Write-Host "`n✓ All changes pushed to GitHub!" -ForegroundColor Green
Write-Host "Next: Go to Render and create a Web Service." -ForegroundColor Cyan
