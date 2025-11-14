import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'codejudge.settings')
django.setup()

from judge.models import Problem

# Create sample problems
problems = [
    {
        'title': 'Add Two Numbers',
        'slug': 'add-two-numbers',
        'description': 'Write a function that adds two numbers and returns the sum.',
        'starter_code': 'def add(a, b):\n    pass',
        'tests': 'assert user_solution.add(1, 2) == 3\nassert user_solution.add(5, 7) == 12\nassert user_solution.add(-1, 1) == 0'
    },
    {
        'title': 'Reverse a String',
        'slug': 'reverse-string',
        'description': 'Write a function that reverses a string.',
        'starter_code': 'def reverse_string(s):\n    pass',
        'tests': 'assert user_solution.reverse_string("hello") == "olleh"\nassert user_solution.reverse_string("abc") == "cba"\nassert user_solution.reverse_string("") == ""'
    },
    {
        'title': 'Check if Prime',
        'slug': 'check-prime',
        'description': 'Write a function that checks if a number is prime.',
        'starter_code': 'def is_prime(n):\n    pass',
        'tests': 'assert user_solution.is_prime(2) == True\nassert user_solution.is_prime(17) == True\nassert user_solution.is_prime(4) == False\nassert user_solution.is_prime(1) == False'
    }
]

for p in problems:
    Problem.objects.get_or_create(
        slug=p['slug'],
        defaults={
            'title': p['title'],
            'description': p['description'],
            'starter_code': p['starter_code'],
            'tests': p['tests']
        }
    )

print("Problems created successfully!")
