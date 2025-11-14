@echo off
REM ============================================================
REM CodeJudge - Complete Git & Deployment Setup Script
REM ============================================================
REM
REM This script will:
REM 1. Initialize git repository
REM 2. Configure git user
REM 3. Add all files
REM 4. Create initial commit
REM 5. Display GitHub instructions
REM
REM PREREQUISITE: Git must be installed and in system PATH
REM Download from: https://git-scm.com/download/win
REM
REM ============================================================

setlocal enabledelayedexpansion

echo.
echo ============================================================
echo CodeJudge - Git Setup and Deployment
echo ============================================================
echo.

REM Check if git is installed
where git >nul 2>&1
if errorlevel 1 (
    echo.
    echo ERROR: Git is not installed or not in system PATH!
    echo.
    echo To fix this:
    echo 1. Download Git from: https://git-scm.com/download/win
    echo 2. Run the installer
    echo 3. During installation, check "Add Git to PATH"
    echo 4. Restart your terminal
    echo 5. Run this script again
    echo.
    pause
    exit /b 1
)

echo [Step 1/5] Checking git installation...
git --version
echo.

echo [Step 2/5] Configuring git user (global)...
git config --global user.name "CodeJudge Developer"
git config --global user.email "codejudge@dev.local"
echo User configured successfully
echo.

echo [Step 3/5] Initializing git repository...
if exist .git (
    echo Git repository already exists. Skipping init.
) else (
    git init
    echo Repository initialized
)
echo.

echo [Step 4/5] Adding all project files...
git add .
echo Files staged for commit
echo.

echo [Step 5/5] Creating initial commit...
git commit -m "Initial commit: CodeJudge - Django Online Judge Platform"
if errorlevel 1 (
    echo [Note] Some files may already be committed or nothing changed
)
echo.

echo.
echo ============================================================
echo SUCCESS! Git setup complete!
echo ============================================================
echo.
echo NEXT STEPS - Push to GitHub:
echo.
echo 1. Create a NEW GitHub repository at:
echo    https://github.com/new
echo    Name: codejudge
echo    Description: Django Online Judge Platform
echo    Click "Create repository"
echo.
echo 2. In this terminal, run these commands:
echo.
echo    git remote add origin https://github.com/YOUR_USERNAME/codejudge.git
echo    git branch -M main
echo    git push -u origin main
echo.
echo 3. Enter your GitHub credentials when prompted
echo.
echo 4. After push succeeds, go to Render.com:
echo    - Sign up with GitHub
echo    - Create new Web Service
echo    - Select this repository
echo    - Render will deploy automatically!
echo.
echo Your live URL will be: https://codejudge.onrender.com
echo.
echo ============================================================
echo.
pause
