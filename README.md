# CodeJudge — Minimal Django coding judge prototype

This prototype is a simple Django app that provides:
- User registration and login (Django auth)
- Problem list and detail pages
- Code submission textarea and a simple test runner
- OpenAI integration for hints (requires `OPENAI_API_KEY`)

Security note: This project runs submitted Python code in a subprocess for demonstration only. Do not deploy this as-is to production — run user code in a hardened sandbox (container, gVisor, seccomp, etc.).

Quick start (Windows PowerShell):

```powershell
cd /workspace/codejudge
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

To seed sample problems, open the Django admin and add `Problem` entries or use the provided fixture.

OpenAI integration:
- Set the environment variable `OPENAI_API_KEY` to a valid key before running the management command below.

Generate problems via OpenAI (creates Problem objects):

```powershell
cd /workspace/codejudge
.\.venv\Scripts\Activate.ps1
python manage.py generate_problems --count 3
```

Notes:
- The project uses `utils/openai_service.py` to call OpenAI. The management command `generate_problems` will create or update problems from the model output.
- This is a prototype. Running user-submitted code is dangerous. Use proper sandboxing for production.
