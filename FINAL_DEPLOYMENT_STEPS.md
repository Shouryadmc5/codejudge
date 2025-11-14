# 📋 MANUAL GITHUB SETUP REQUIRED

Your Git is ready but the GitHub repository doesn't exist yet.

## ⚠️ ACTION REQUIRED:

### Step 1: Create Repository on GitHub

1. Go to: https://github.com/new
2. Fill in:
   - **Repository name:** codejudge
   - **Description:** Django Online Judge Platform
   - **Visibility:** Public (recommended for portfolios)
   - **Initialize with:** DO NOT check anything (we have files ready)
3. Click **"Create repository"**

### Step 2: Push Your Code

After creating the repository, run in PowerShell:

```powershell
$env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")

git remote add origin https://github.com/shouryadmc5/codejudge.git
git branch -M main
git push -u origin main
```

GitHub may ask you to authenticate:
- If browser opens: Complete authentication there
- If asks for token: Use Personal Access Token (create at https://github.com/settings/tokens)

### Step 3: Verify Push

Check your GitHub at: https://github.com/shouryadmc5/codejudge

You should see all 36 files uploaded!

---

## 🚀 THEN: Deploy on Render

Once pushed to GitHub:

1. Go to: https://render.com
2. Sign up with GitHub (authorize if needed)
3. Click **"New +"** → **"Web Service"**
4. Select **"codejudge"** repository
5. Configuration (should auto-fill from render.yaml):
   - **Build Command:** `pip install -r requirements.txt && python manage.py collectstatic --noinput`
   - **Start Command:** `gunicorn codejudge.wsgi:application`
6. Click **"Create Web Service"**

---

## 🔑 Environment Variables (Set After Deploy Starts)

In Render Dashboard → **Environment**:

```
DJANGO_SECRET = <generate-key>
DEBUG = False
```

Generate secret key:
```powershell
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

---

## 📦 Initialize Database on Render

After deployment starts, go to **Shell**:

```bash
python manage.py migrate
python manage.py createsuperuser
```

---

## ✅ DONE!

Your live URL: https://codejudge.onrender.com

Share with students! 🎉
