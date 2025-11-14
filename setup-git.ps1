#!/usr/bin/env pwsh
# ============================================================
# CodeJudge - Git & Deployment Setup (PowerShell)
# ============================================================
#
# This script will:
# 1. Initialize git repository
# 2. Configure git user
# 3. Add all files
# 4. Create initial commit
# 5. Display GitHub instructions
#
# PREREQUISITE: Git must be installed
# Download from: https://git-scm.com/download/win
#
# ============================================================

Write-Host ""
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "CodeJudge - Git Setup and Deployment" -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host ""

# Check if git is installed
$gitCheck = git --version 2>$null
if ($LASTEXITCODE -ne 0) {
    Write-Host ""
    Write-Host "ERROR: Git is not installed or not in system PATH!" -ForegroundColor Red
    Write-Host ""
    Write-Host "To fix this:" -ForegroundColor Yellow
    Write-Host "1. Download Git from: https://git-scm.com/download/win"
    Write-Host "2. Run the installer"
    Write-Host "3. During installation, check 'Add Git to PATH'"
    Write-Host "4. Restart your PowerShell terminal"
    Write-Host "5. Run this script again"
    Write-Host ""
    Read-Host "Press Enter to exit"
    exit 1
}

Write-Host "[Step 1/5] Checking git installation..." -ForegroundColor Green
Write-Host $gitCheck
Write-Host ""

Write-Host "[Step 2/5] Configuring git user (global)..." -ForegroundColor Green
git config --global user.name "CodeJudge Developer"
git config --global user.email "codejudge@dev.local"
Write-Host "User configured successfully" -ForegroundColor Cyan
Write-Host ""

Write-Host "[Step 3/5] Initializing git repository..." -ForegroundColor Green
if (Test-Path ".git") {
    Write-Host "Git repository already exists. Skipping init." -ForegroundColor Yellow
} else {
    git init
    Write-Host "Repository initialized" -ForegroundColor Cyan
}
Write-Host ""

Write-Host "[Step 4/5] Adding all project files..." -ForegroundColor Green
git add .
Write-Host "Files staged for commit" -ForegroundColor Cyan
Write-Host ""

Write-Host "[Step 5/5] Creating initial commit..." -ForegroundColor Green
git commit -m "Initial commit: CodeJudge - Django Online Judge Platform"
Write-Host ""

Write-Host ""
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "SUCCESS! Git setup complete!" -ForegroundColor Green
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host ""

Write-Host "NEXT STEPS - Push to GitHub:" -ForegroundColor Yellow
Write-Host ""
Write-Host "1. Create a NEW GitHub repository at:" -ForegroundColor Cyan
Write-Host "   https://github.com/new"
Write-Host "   Name: codejudge"
Write-Host "   Description: Django Online Judge Platform"
Write-Host "   Click 'Create repository'"
Write-Host ""

Write-Host "2. In this terminal, run these commands:" -ForegroundColor Cyan
Write-Host ""
Write-Host "   git remote add origin https://github.com/YOUR_USERNAME/codejudge.git" -ForegroundColor White -BackgroundColor Black
Write-Host "   git branch -M main" -ForegroundColor White -BackgroundColor Black
Write-Host "   git push -u origin main" -ForegroundColor White -BackgroundColor Black
Write-Host ""

Write-Host "3. Enter your GitHub credentials when prompted" -ForegroundColor Cyan
Write-Host ""

Write-Host "4. After push succeeds, go to Render.com:" -ForegroundColor Cyan
Write-Host "   - Sign up with GitHub"
Write-Host "   - Create new Web Service"
Write-Host "   - Select this repository"
Write-Host "   - Render will deploy automatically!"
Write-Host ""

Write-Host "Your live URL will be: https://codejudge.onrender.com" -ForegroundColor Green
Write-Host ""
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host ""

Read-Host "Press Enter to exit"
