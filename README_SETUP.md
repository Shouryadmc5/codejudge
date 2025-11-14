# 🧠 CodeJudge - Online Code Judge Platform

A Django-based online judge where users can solve coding problems, submit solutions, and get instant feedback.

## ✨ Features

- 📚 **Problem Library** - Multiple coding challenges
- 👤 **User Authentication** - Register, login, track submissions
- ✏️ **Code Submission** - Write and submit solutions
- ✅ **Automated Testing** - Run test cases on submissions
- 💡 **AI Hints** - Get helpful hints powered by OpenAI
- 🎨 **Modern UI** - Built with Bootstrap 5
- 📊 **Submission History** - View all your attempts and results

## 🚀 Quick Start (Local)

### Prerequisites
- Python 3.8+
- pip

### Installation

```bash
# Clone or navigate to project
cd c:\workspace\codejudge

# Create virtual environment
python -m venv .venv

# Activate virtual environment
.\.venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create superuser (admin)
python manage.py createsuperuser

# Start development server
python manage.py runserver
```

Visit: http://localhost:8000

## 📋 Seed Sample Problems

```bash
python seed_problems.py
```

Creates 3 sample problems:
1. Add Two Numbers
2. Reverse a String
3. Check if Prime

## 🧪 Test a Solution

Run the automated test for the "Add Two Numbers" problem:

```bash
python run_solution.py
```

## 🌐 Deployment on Render (Free)

### Step 1: Install Git
Download from: https://git-scm.com/download/win

### Step 2: Push to GitHub

```bash
cd c:\workspace\codejudge
git init
git add .
git commit -m "Deploy CodeJudge"
git remote add origin https://github.com/YOUR_USERNAME/codejudge.git
git branch -M main
git push -u origin main
```

### Step 3: Deploy on Render

1. Go to https://render.com
2. Connect GitHub account
3. Select `codejudge` repository
4. Use this configuration:
   - **Build Command:** `pip install -r requirements.txt && python manage.py collectstatic --noinput`
   - **Start Command:** `gunicorn codejudge.wsgi:application`

### Step 4: Set Environment Variables

```
DJANGO_SECRET=<your-secret-key>
DEBUG=False
```

Generate secret key:
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### Step 5: Run Migrations on Render

Go to Render Dashboard → Shell:
```bash
python manage.py migrate
python manage.py createsuperuser
```

**Your app is now live!** 🎉

## 📁 Project Structure

```
codejudge/
├── codejudge/           # Django project settings
│   ├── settings.py      # Production-ready configuration
│   ├── urls.py
│   └── wsgi.py
├── judge/               # Main app
│   ├── models.py        # Problem, Submission models
│   ├── views.py         # View logic
│   ├── forms.py         # Django forms
│   └── urls.py
├── templates/           # HTML templates (Bootstrap 5)
├── utils/
│   ├── runner.py        # Code execution engine
│   └── openai_service.py # AI hints
├── render.yaml          # Render deployment config
├── requirements.txt     # Python dependencies
└── manage.py
```

## 🔧 Key Technologies

- **Backend:** Django 5.2
- **Frontend:** Bootstrap 5, HTML, CSS
- **Database:** SQLite (local), PostgreSQL (Render)
- **Server:** Gunicorn + WhiteNoise
- **AI:** OpenAI API (for hints)
- **Code Execution:** Subprocess with timeout

## ⚠️ Security Notes

- The code runner executes user submissions in a subprocess with timeout protection
- For production with untrusted code, use proper sandboxing (Docker, gVisor, seccomp)
- Set `DEBUG=False` in production
- Use strong `DJANGO_SECRET` key
- Configure `ALLOWED_HOSTS` appropriately

## 📝 API Endpoints

### Authentication
- `GET /` - Problem list
- `POST /register/` - User registration
- `POST /accounts/login/` - User login
- `GET /accounts/logout/` - User logout

### Problems & Submissions
- `GET /judge/problem/<slug>/` - View problem
- `POST /judge/problem/<slug>/` - Submit solution
- `GET /judge/submission/<id>/` - View submission result

## 🤝 Contributing

Feel free to fork and submit pull requests!

## 📄 License

This project is open source.

---

**Made for students learning competitive programming & DSA** 🚀
