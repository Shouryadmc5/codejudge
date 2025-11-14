# CodeJudge - Django Online Judge Platform
# Ready for Deployment on Render

## Local Setup

```bash
cd c:\workspace\codejudge
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Production Deployment on Render

### Prerequisites:
1. Install Git: https://git-scm.com/download/win
2. Create GitHub Account: https://github.com
3. Create Render Account: https://render.com

### Step 1: Push to GitHub

```bash
# Navigate to project
cd c:\workspace\codejudge

# Initialize git (one time)
git init
git config user.name "Your Name"
git config user.email "your.email@example.com"

# Add all files
git add .

# Create initial commit
git commit -m "Initial commit: CodeJudge - Django Judge Platform"

# Add remote (replace with your GitHub repo URL)
git remote add origin https://github.com/YOUR_USERNAME/codejudge.git

# Push to GitHub
git branch -M main
git push -u origin main
```

### Step 2: Deploy on Render

1. Go to https://render.com
2. Sign up with GitHub
3. Click "New +" → "Web Service"
4. Select your `codejudge` repository
5. Configure:
   - **Name:** codejudge
   - **Environment:** Python
   - **Build Command:** `pip install -r requirements.txt && python manage.py collectstatic --noinput`
   - **Start Command:** `gunicorn codejudge.wsgi:application`
   - **Instance Type:** Free
6. Click "Create Web Service"

### Step 3: Set Environment Variables

In Render Dashboard → Environment:

```
DJANGO_SECRET=<generate-random-key>
DEBUG=False
```

Generate secret key (run locally):
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### Step 4: Initialize Database on Render

Go to Render Dashboard → Shell and run:
```bash
python manage.py migrate
python manage.py createsuperuser
```

### Done! 🎉

Your app will be live at: `https://codejudge.onrender.com`

## Features Ready for Production:
✅ Bootstrap 5 UI
✅ User Authentication
✅ Code Submission & Testing
✅ Problem Management
✅ Submission Results Display
✅ Static Files Served by WhiteNoise
✅ Gunicorn Production Server

## Files Ready for Deployment:
- ✓ render.yaml
- ✓ requirements.txt
- ✓ .gitignore
- ✓ settings.py (production config)
- ✓ All templates with Bootstrap styling
