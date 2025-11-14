@echo off
REM CodeJudge Deployment Automation Script
REM Run this after installing Git

echo.
echo ======================================
echo CodeJudge - Automated Deployment
echo ======================================
echo.

REM Check if git is installed
git --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Git is not installed or not in PATH
    echo Please install Git from: https://git-scm.com/download/win
    echo Make sure to check "Add Git to PATH" during installation
    pause
    exit /b 1
)

echo [1/5] Configuring Git...
git config --global user.name "CodeJudge Developer"
git config --global user.email "codejudge@local.dev"

echo [2/5] Initializing repository...
git init

echo [3/5] Adding all files...
git add .

echo [4/5] Creating initial commit...
git commit -m "Initial commit: CodeJudge - Online Judge Platform"

echo.
echo ======================================
echo Git Setup Complete!
echo ======================================
echo.
echo Next Steps:
echo.
echo 1. Create a GitHub repository at: https://github.com/new
echo    Name it: codejudge
echo.
echo 2. Run these commands to link and push:
echo    git remote add origin https://github.com/YOUR_USERNAME/codejudge.git
echo    git branch -M main
echo    git push -u origin main
echo.
echo 3. Go to https://render.com and deploy
echo    (See DEPLOYMENT_GUIDE.md for detailed instructions)
echo.
pause
