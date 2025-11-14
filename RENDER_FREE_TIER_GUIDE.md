# Render Free-Tier Deployment Guide for CodeJudge

This guide walks you through deploying CodeJudge on **Render's free tier**.

## Why Free Tier Works

- **SQLite database**: No PostgreSQL needed; stored on the instance.
- **Gunicorn**: Lightweight WSGI server included in `requirements.txt`.
- **WhiteNoise**: Serves static files without extra CDN cost.
- **Single dyno**: Render free tier includes one web service with CPU/memory limits.

**Limitations**: 
- App goes to sleep after 15 minutes of inactivity (normal free tier behavior).
- Data loss if instance restarts unless you add a managed PostgreSQL (paid).

---

## Prerequisites

1. **GitHub account** with repository `Shouryadmc5/codejudge` pushed.
2. **Render account** (sign up at [render.com](https://render.com), link GitHub).

---

## Step 1: Create a Web Service on Render

1. Go to [render.com/dashboard](https://render.com/dashboard).
2. Click **New +** → **Web Service**.
3. **Connect Repository**: Select `Shouryadmc5/codejudge` from your GitHub repos.
   - (First time: authorize Render to access your GitHub account.)
4. Click **Connect**.

---

## Step 2: Configure Build & Start Commands

On the Web Service creation form, fill in:

| Field | Value |
|-------|-------|
| **Name** | `codejudge` (or your choice) |
| **Environment** | `Python 3` |
| **Build Command** | `pip install -r requirements.txt && python manage.py collectstatic --noinput` |
| **Start Command** | `gunicorn codejudge.wsgi:application` |
| **Region** | Closest to you (e.g., US) |
| **Plan** | **Free** (or Starter) |

Leave other fields as defaults. Click **Create Web Service**.

---

## Step 3: Add Environment Variables

1. In the Render service dashboard, scroll to **Environment**.
2. Click **Add Environment Variable** and add each of the following:

| Key | Value | Notes |
|-----|-------|-------|
| `DJANGO_SECRET_KEY` | (see below) | Generate a secure key; never commit it. |
| `DEBUG` | `False` | Always `False` in production. |
| `ALLOWED_HOSTS` | `*` | Render will assign your URL automatically. |

### Generate a Secure `DJANGO_SECRET_KEY`

Run this locally and copy the output:

```bash
python -c "import secrets, string; print(''.join(secrets.choice(string.ascii_letters + string.digits + '!@#$%^&*(-_=+)') for _ in range(50)))"
```

Paste the result into the `DJANGO_SECRET_KEY` environment variable on Render.

---

## Step 4: Deploy & Wait

1. Click **Deploy** (or Render may auto-deploy after env vars are saved).
2. Watch the build logs in the **Logs** tab.
   - Build takes ~2–5 minutes.
   - If successful, you'll see:
     ```
     Build successful
     Starting service
     ```
   - If it fails, copy the error message and share it so I can debug.

---

## Step 5: Run Migrations & Create Superuser

Once the service is running (status shows "Live"), open the **Shell** tab and run:

```bash
python manage.py migrate
python manage.py createsuperuser
```

Follow the prompts to create an admin account (username, email, password).

---

## Step 6: Access Your App

1. Render assigns you a public URL (e.g., `https://codejudge-xyz.onrender.com`).
2. Visit that URL in your browser.
3. Log in with your superuser credentials (or create a user first).
4. Start solving problems!

---

## Troubleshooting

### Build Fails: "pip install" error
- Check `requirements.txt` for syntax or version conflicts.
- If a package is missing, let me know and I'll add it.

### Build Succeeds but App Won't Start
- Check the **Logs** tab for runtime errors.
- Common causes:
  - `SECRET_KEY` not set → paste the env var again.
  - Migrations not run → use the Shell tab to run `python manage.py migrate`.
  - Static files issue → usually fixed by `collectstatic` in build command.

### App Runs but Shows 404 or "Not Found"
- Confirm the URL is correct (Render assigned it in the dashboard).
- Try `/admin/` to see if Django is working.

### Database Lost After Restart
- Free tier SQLite is ephemeral; data is lost on redeploy or restart.
- **To keep data permanently**: upgrade to a managed PostgreSQL (paid).
- For now, re-seed sample problems after each restart (if needed).

---

## Free-Tier Performance Notes

- **Cold starts**: App may take 30–60 seconds to wake up after inactivity.
- **Concurrent users**: Recommended ~10 simultaneously on free tier.
- **Uptime**: ~99.9% (maintenance windows excluded).

---

## Next Steps

1. Follow the steps above to deploy on Render.
2. If you hit any errors, share the build/runtime logs and I'll help fix them.
3. Once live, you can invite others to use CodeJudge!

---

## Manual Git Setup (if needed)

If you haven't committed `.env.example` and other recent changes:

```powershell
git add .
git commit -m "Deploy to Render free tier"
git push origin main
```

Then refresh the Render dashboard and redeploy.

---

**Questions?** Paste build logs or runtime errors here, and I'll debug them for you.
