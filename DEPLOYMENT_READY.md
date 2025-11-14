# CodeJudge – Render Free-Tier Deployment Summary

## Ready to Deploy ✓

All files are prepared and optimized for Render free tier. Here's what I did:

### Changes Made

1. **`codejudge/settings.py`**
   - Updated `DJANGO_SECRET_KEY` variable name (matches `.env.example`)
   - Added `dj-database-url` for optional PostgreSQL support
   - SQLite remains default (no Postgres needed for free tier)
   - Added production security settings (SSL, HSTS, secure cookies)

2. **`.env.example`**
   - Documents all required environment variables
   - Ready to copy for local `.env` or Render environment settings

3. **`render.yaml`**
   - Already configured with correct build & start commands
   - Points to `gunicorn` (lightweight, free-tier friendly)
   - Static files handled by WhiteNoise

4. **`commit_and_deploy.ps1`**
   - Helper script to commit & push to GitHub
   - Run this before deploying on Render

5. **`RENDER_FREE_TIER_GUIDE.md`**
   - Step-by-step Render deployment instructions
   - Environment variable setup
   - Troubleshooting tips

### Next Steps (For You)

1. **Commit & Push to GitHub**
   ```powershell
   # In PowerShell, navigate to c:\workspace\codejudge and run:
   .\commit_and_deploy.ps1
   ```
   Or manually:
   ```powershell
   git add .
   git commit -m "Prepare for Render free-tier deployment"
   git push
   ```

2. **Deploy on Render**
   - Go to [render.com/dashboard](https://render.com/dashboard)
   - Create a new **Web Service**
   - Connect your `Shouryadmc5/codejudge` GitHub repo
   - Set:
     - **Build Command**: `pip install -r requirements.txt && python manage.py collectstatic --noinput`
     - **Start Command**: `gunicorn codejudge.wsgi:application`
   - Add environment variables:
     - `DJANGO_SECRET_KEY`: (generate secure key)
     - `DEBUG`: `False`
     - `ALLOWED_HOSTS`: `*`
   - Deploy!

3. **Run Migrations** (in Render Shell)
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

4. **Access Your App**
   - Render gives you a public URL (e.g., `https://codejudge-xyz.onrender.com`)
   - Visit it and log in!

### Free Tier Details

- **Database**: SQLite (ephemeral; data lost on restart—acceptable for free tier)
- **Static Files**: WhiteNoise handles them (no extra cost)
- **Uptime**: ~99.9%
- **Cold Starts**: 30–60 seconds after inactivity (normal for free tier)
- **Concurrent Users**: ~10–20 recommended

### If Errors Occur

1. Check Render build logs
2. Paste the error here
3. I'll debug and provide a fix

---

**You're all set!** Follow the steps above and CodeJudge will be live on Render within ~5 minutes. 🚀
