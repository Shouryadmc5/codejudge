import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'codejudge.settings')
django.setup()

from judge.models import Problem, Submission
from django.contrib.auth.models import User
from utils.runner import run_submission

# Get the problem
problem = Problem.objects.get(slug='add-two-numbers')

# Get or create a test user
user, created = User.objects.get_or_create(
    username='testuser',
    defaults={'email': 'test@example.com'}
)

# The correct solution code
solution_code = '''def add(a, b):
    return a + b
'''

# Create a submission
submission = Submission.objects.create(
    problem=problem,
    user=user,
    code=solution_code
)

# Run the tests
result = run_submission(problem, solution_code)

# Update the submission with results
submission.passed = result['passed']
submission.output = result.get('output', '')
submission.save()

# Print results
print(f"\n{'='*50}")
print(f"Problem: {problem.title}")
print(f"{'='*50}")
print(f"Passed: {submission.passed}")
print(f"\nOutput:")
print(submission.output)
print(f"\nCode submitted:")
print(submission.code)
print(f"{'='*50}\n")
