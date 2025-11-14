import os
import json
import re
from typing import Optional

try:
    import openai
except Exception:
    openai = None

OPENAI_KEY = os.environ.get('OPENAI_API_KEY')
if openai and OPENAI_KEY:
    openai.api_key = OPENAI_KEY


def _extract_json(text: str) -> Optional[dict]:
    """Try to extract JSON object from text response."""
    # find first { ... } block
    m = re.search(r"\{.*\}", text, re.S)
    if not m:
        return None
    try:
        return json.loads(m.group(0))
    except Exception:
        return None


def generate_problem(max_tokens=800):
    """Call OpenAI to generate a single coding problem in JSON.

    JSON keys: title, slug, description, starter_code, tests
    `tests` should be valid Python code using assert statements that import/ call functions from the starter code.
    """
    if openai is None:
        raise RuntimeError('openai library not available')
    if OPENAI_KEY is None:
        raise RuntimeError('OPENAI_API_KEY not set')

    prompt = (
        "Create a single Python coding problem suitable for students. "
        "Return only a JSON object with keys: title, slug, description, starter_code, tests. "
        "- `starter_code` should include a function signature (no tests). "
        "- `tests` should contain Python assert statements that will be executed (using the function from starter_code). "
        "Make tests concise and deterministic. Keep description short. Use only ascii characters."
    )

    resp = openai.ChatCompletion.create(
        model='gpt-4o-mini',
        messages=[{"role": "user", "content": prompt}],
        max_tokens=max_tokens,
        temperature=0.2,
    )
    text = resp['choices'][0]['message']['content']
    data = _extract_json(text)
    if data is None:
        # fallback: try to evaluate the full text as JSON
        try:
            data = json.loads(text)
        except Exception as e:
            raise RuntimeError('Could not parse OpenAI response as JSON') from e
    return data


def get_hint(problem, max_tokens=300):
    """Ask OpenAI for a short hint about how to approach the problem."""
    if openai is None or OPENAI_KEY is None:
        return None

    prompt = (
        f"You are a programming tutor. Provide a short hint (2-4 sentences) to help a student solve the following problem:\n\n"
        f"Title: {problem.title}\n\nDescription:\n{problem.description}\n\nStarter code:\n{problem.starter_code}\n\n"
        "Do not reveal full solution. Keep it concise."
    )
    resp = openai.ChatCompletion.create(
        model='gpt-4o-mini',
        messages=[{"role": "user", "content": prompt}],
        max_tokens=max_tokens,
        temperature=0.3,
    )
    return resp['choices'][0]['message']['content'].strip()
