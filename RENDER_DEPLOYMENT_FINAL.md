# 🚀 CODEJUDGE DEPLOYMENT ON RENDER - FINAL STEPS

## ✅ Step 1: Code Pushed to GitHub
Your repository: https://github.com/Shouryadmc5/codejudge

All 47 files uploaded successfully! ✓

---

## 🎯 Step 2: Deploy on Render (FOLLOW THESE STEPS)

### 2.1 Go to Render.com
https://render.com

### 2.2 Sign Up / Log In
- Click "Sign up with GitHub"
- Authorize Render to access your GitHub
- OR log in if you already have an account

### 2.3 Create Web Service
1. Click **"New +"** button (top right)
2. Select **"Web Service"**
3. In the list, find and select: **codejudge**
4. Click "Connect"

### 2.4 Configure Deployment

Fill in these fields:

| Field | Value |
|-------|-------|
| **Name** | codejudge |
| **Environment** | Python |
| **Build Command** | `pip install -r requirements.txt && python manage.py collectstatic --noinput` |
| **Start Command** | `gunicorn codejudge.wsgi:application` |
| **Instance Type** | Free |

5. Click **"Create Web Service"**

### 2.5 Set Environment Variables

While deployment is starting (you'll see logs), go to:
**Environment** tab (left sidebar)

Add these variables:

**Variable 1:**
- Name: `DJANGO_SECRET`
- Value: Copy from PowerShell:
```powershell
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

**Variable 2:**
- Name: `DEBUG`
- Value: `False`

Click "Save"

### 2.6 Run Database Migrations

Once the web service is running (you'll see a green checkmark):

1. Click on your service
2. Go to **"Shell"** tab
3. Run these commands:

```bash
python manage.py migrate
python manage.py createsuperuser
```

Follow the prompts to create an admin account.

---

## 🎉 YOUR APP IS LIVE!

Your URL will be:
```
https://codejudge.onrender.com
```

(Note: First request may take 30 seconds as free tier spins up)

---

## 📊 Access Your App

### Public URL:
https://codejudge.onrender.com

### Admin Panel:
https://codejudge.onrender.com/admin
(Use the superuser account you created)

### Problems Page:
https://codejudge.onrender.com/judge/problem/add-two-numbers/

---

## 🔧 If Deployment Fails

Check the **Logs** tab on Render:
- Look for error messages
- Common issues: missing environment variables, migration errors

**Solution:** Add missing env vars and restart the service

---

## 📱 Share With Students!

Your live CodeJudge link:
```
https://codejudge.onrender.com
```

They can:
✅ Register and create accounts
✅ View all problems
✅ Submit code solutions
✅ Get instant feedback
✅ View submission history

---

## 💡 Production Checklist

✓ Git installed and code pushed
✓ Render.yaml configured
✓ settings.py production-ready
✓ WhiteNoise static files configured
✓ Gunicorn production server ready
✓ Database migrations prepared
✓ Environment variables template ready

**Everything is configured for production!** 🚀

---

## 🆘 Need Help?

- **Render Docs:** https://render.com/docs
- **Django Docs:** https://docs.djangoproject.com
- **Error in logs?** Check the Render Shell for migration or import errors
