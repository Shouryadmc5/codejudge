from django.core.management.base import BaseCommand
from judge.models import Problem
from utils.openai_service import generate_problem


class Command(BaseCommand):
    help = 'Generate problems using OpenAI and save to the database'

    def add_arguments(self, parser):
        parser.add_argument('--count', type=int, default=1, help='Number of problems to generate')

    def handle(self, *args, **options):
        count = options['count']
        for i in range(count):
            self.stdout.write(f'Generating problem {i+1}/{count}...')
            try:
                data = generate_problem()
            except Exception as e:
                self.stderr.write(f'Error generating problem: {e}')
                return

            # Ensure required keys exist
            title = data.get('title') or data.get('name') or 'Untitled Problem'
            slug = data.get('slug') or title.lower().replace(' ', '-')
            description = data.get('description','')
            starter_code = data.get('starter_code','')
            tests = data.get('tests','')

            # Avoid duplicates by slug
            obj, created = Problem.objects.update_or_create(slug=slug, defaults={
                'title': title,
                'description': description,
                'starter_code': starter_code,
                'tests': tests,
            })
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created problem: {obj.title}'))
            else:
                self.stdout.write(self.style.WARNING(f'Updated problem: {obj.title}'))
