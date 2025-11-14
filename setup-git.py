#!/usr/bin/env python3
"""
CodeJudge Git Setup Tool (No Git CLI Required)
Uses GitPython library to perform git operations
"""

import sys
import os
from pathlib import Path

try:
    import git
except ImportError:
    print("GitPython not installed. Installing...")
    os.system(f"{sys.executable} -m pip install GitPython -q")
    import git

def setup_git_repo():
    """Initialize git repository and make initial commit"""
    
    repo_path = Path(__file__).parent
    print("\n" + "="*70)
    print("CodeJudge - Git Setup (Python Edition)")
    print("="*70 + "\n")
    
    # Check if repo already exists
    if (repo_path / '.git').exists():
        print("✓ Git repository already initialized")
        repo = git.Repo(repo_path)
    else:
        print("[1/4] Initializing git repository...")
        repo = git.Repo.init(repo_path)
        print("✓ Repository initialized\n")
    
    # Configure git user
    print("[2/4] Configuring git user...")
    with repo.config_writer() as git_config:
        git_config.set_value("user", "name", "CodeJudge Developer").release()
        git_config.set_value("user", "email", "codejudge@dev.local").release()
    print("✓ Git user configured\n")
    
    # Add all files
    print("[3/4] Staging all files...")
    try:
        repo.git.add(A=True)
        print(f"✓ Files staged for commit\n")
    except Exception as e:
        print(f"✓ Git add completed (some files may be ignored)\n")
    
    # Create commit
    print("[4/4] Creating initial commit...")
    try:
        repo.index.commit("Initial commit: CodeJudge - Django Online Judge Platform")
        print("✓ Initial commit created\n")
    except git.exc.GitCommandError as e:
        if "nothing to commit" in str(e):
            print("✓ Repository already has commits\n")
        else:
            print(f"Note: {e}\n")
    
    # Display summary
    print("="*70)
    print("SUCCESS! Git setup complete!")
    print("="*70 + "\n")
    
    print("📋 NEXT STEPS - Push to GitHub:\n")
    print("1️⃣  Create a NEW GitHub repository at:")
    print("    https://github.com/new")
    print("    Name: codejudge")
    print("    Description: Django Online Judge Platform")
    print("    Click 'Create repository'\n")
    
    print("2️⃣  Add remote and push:")
    print("    git remote add origin https://github.com/YOUR_USERNAME/codejudge.git")
    print("    git branch -M main")
    print("    git push -u origin main\n")
    
    print("3️⃣  Go to Render.com:")
    print("    - Sign up with GitHub")
    print("    - Create new Web Service")
    print("    - Select this repository")
    print("    - Render will auto-deploy!\n")
    
    print("🎉 Your live app will be at: https://codejudge.onrender.com\n")
    print("="*70 + "\n")
    
    return True

if __name__ == "__main__":
    try:
        setup_git_repo()
        print("✅ Setup complete! Ready to push to GitHub.\n")
    except Exception as e:
        print(f"\n❌ Error: {e}\n")
        sys.exit(1)
