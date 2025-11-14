from django.conf import settings
from django.db import models


class Problem(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    starter_code = models.TextField(blank=True)
    tests = models.TextField(help_text='Python test code that will be appended and executed (use assert), e.g. assert add(1,2)==3')

    def __str__(self):
        return self.title


class Submission(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    code = models.TextField()
    passed = models.BooleanField(null=True)
    output = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Submission {self.pk} by {self.user} on {self.problem}"
