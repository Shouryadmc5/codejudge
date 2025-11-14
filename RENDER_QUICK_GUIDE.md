# Quick Visual Guide - Render Deployment (Clickable Steps)

## ⚡ TL;DR - Just 6 Clicks + 2 Shell Commands

### Click 1: Create Web Service
```
1. Go to https://render.com/dashboard
2. Click: New + → Web Service
3. Connect: Shouryadmc5/codejudge (GitHub repo)
```

### Click 2-4: Configure Build & Start
```
Build Command:
pip install -r requirements.txt && python manage.py collectstatic --noinput

Start Command:
gunicorn codejudge.wsgi:application

Instance: Free
```

### Click 5: Add Environment Variables
```
DJANGO_SECRET_KEY = b8fZ$3pNq7WvL1rY9x@T6uC4mS0hK2eP%gA5dQzV!jR^oL*8#P
DEBUG = False
ALLOWED_HOSTS = *
```

### Click 6: Deploy
```
Click "Create Web Service"
Wait for status: "Live" (2-5 minutes)
```

---

## 🔧 Shell Commands (Copy & Paste These)

Once service is **Live**, click **Shell** and run:

```bash
python manage.py migrate
```

Then:

```bash
python manage.py createsuperuser
```

Follow prompts (username, email, password).

---

## ✅ Verify It Works

1. Copy your Render service URL (shows at top, e.g., `https://codejudge-xyz.onrender.com`)
2. Visit it in browser
3. Click **Login** → use superuser credentials
4. See the problem list!

---

## 🆘 If Something Fails

Paste the error here and I'll fix it. Common fixes:

| Error | Fix |
|-------|-----|
| "Database error" | Run `python manage.py migrate` again in Shell |
| "404 Not Found" | Check Render URL is correct; try `/admin/` |
| "Environment variable not set" | Re-add in Render **Environment**, click Save |
| "Static files missing" | Run in Shell: `python manage.py collectstatic --noinput` |

---

## 🎯 Next: Tell me when you complete Steps 1-2, and I'll help with any errors!

Go to https://render.com/dashboard now! 🚀
