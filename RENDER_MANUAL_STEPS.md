# Render Deployment - Complete Step-by-Step Guide

## IMPORTANT: What You Need to Do Manually

I (the assistant) cannot directly access your Render account, so you'll need to perform these steps manually in the Render dashboard. However, I'll provide exact commands for everything else.

---

## Step 1: Create Web Service (Manual - Render Dashboard)

1. Go to: https://render.com/dashboard
2. Click: **New +** → **Web Service**
3. Select repository: `Shouryadmc5/codejudge` (connect GitHub if needed)
4. Fill in these fields:

| Field | Value |
|-------|-------|
| Name | `codejudge` |
| Environment | `Python 3` |
| Build Command | `pip install -r requirements.txt && python manage.py collectstatic --noinput` |
| Start Command | `gunicorn codejudge.wsgi:application` |
| Instance Type | **Free** |
| Region | US (or closest to you) |

5. Click **Create Web Service**
6. **Wait for build to complete** (2-5 minutes)

---

## Step 2: Add Environment Variables (Manual - Render Dashboard)

Once the Web Service is created:

1. In Render dashboard, go to your `codejudge` service
2. Click: **Environment** (left sidebar)
3. Add each variable by clicking **Add Environment Variable**:

```
DJANGO_SECRET_KEY = b8fZ$3pNq7WvL1rY9x@T6uC4mS0hK2eP%gA5dQzV!jR^oL*8#P
DEBUG = False
ALLOWED_HOSTS = *
```

4. Click **Save** (Render will auto-redeploy)
5. **Wait for deployment to complete**

---

## Step 3: Run Migrations (After Deployment - Use Render Shell)

Once your service is **Live** (status shows green):

1. In Render dashboard, click your `codejudge` service
2. Click: **Shell** (top right, near Logs)
3. Copy and paste this command:

```bash
python manage.py migrate
```

**Expected output:**
```
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, judge, sessions
Running migrations:
  Applying ... OK
```

---

## Step 4: Create Superuser (Use Render Shell)

In the same Render Shell, run:

```bash
python manage.py createsuperuser
```

**Follow the prompts:**
- Username: (enter your admin username, e.g., `admin`)
- Email: (enter an email)
- Password: (enter a secure password; will be hidden)
- Password (again): (confirm)

**Example:**
```
Username: admin
Email: admin@codejudge.com
Password: 
Password (confirm): 
Superuser created successfully.
```

---

## Step 5: Verify Site is Live

1. In Render dashboard, find your service's public URL (top of page, e.g., `https://codejudge-xyz.onrender.com`)
2. Click it or paste in browser
3. You should see the CodeJudge homepage
4. Click **Login** or go to `/admin/`
5. Log in with the superuser credentials you just created

**If you see errors:**
- Check Render **Logs** for runtime errors
- Common issues:
  - Environment variables not saved → re-add them
  - Migration failed → run `python manage.py migrate` again in Shell
  - Static files issue → run `python manage.py collectstatic --noinput` in Shell

---

## Step 6: Start Using CodeJudge

1. Create a regular user (non-admin):
   - Go to `/admin/` → Users → Add User
   - OR invite others to sign up directly

2. Add sample problems (optional):
   - In Render Shell, run:
     ```bash
     python seed_problems.py
     ```
   - This adds 3 test problems: "Add Two Numbers", "Reverse a String", "Check if Prime"

3. Test a submission:
   - Log in as a user
   - Go to Problems
   - Click any problem
   - Submit a solution
   - See results!

---

## Troubleshooting

### Build Fails
- Check **Logs** tab for errors
- Common: missing package, version conflict
- If stuck, share the error and I'll help fix it

### App Runs but Shows 404
- Confirm you're using the correct Render URL
- Try adding `/admin/` to the end
- Check **Logs** for Django errors

### Environment Variables Not Working
- Go to **Environment** and verify all 3 variables are set
- Click **Save** (this triggers a redeploy)
- Wait for deployment to complete

### Database/Migration Errors
- Go to Render Shell and run:
  ```bash
  python manage.py migrate --noinput
  ```
- If still stuck, share the error

---

## Summary

Once you complete the manual steps (1 & 2), I can help you troubleshoot any errors that come up. The site should be live within ~10 minutes total.

**Next action:** Go to Render dashboard and start Step 1 above! 🚀
