import os
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Problem, Submission
from .forms import RegisterForm, SubmissionForm
from utils.runner import run_submission
from utils.openai_service import get_hint


def problem_list(request):
    problems = Problem.objects.all()
    return render(request, 'judge/problem_list.html', {'problems': problems})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('judge:problem_list')
    else:
        form = RegisterForm()
    return render(request, 'judge/register.html', {'form': form})


def problem_detail(request, slug):
    problem = get_object_or_404(Problem, slug=slug)
    hint = None
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('login')
        form = SubmissionForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            sub = Submission.objects.create(problem=problem, user=request.user, code=code)
            result = run_submission(problem, code)
            sub.passed = result['passed']
            sub.output = result.get('output','')
            sub.save()
            return redirect('judge:submission_result', pk=sub.pk)
    else:
        form = SubmissionForm(initial={'code': problem.starter_code})
    if request.user.is_authenticated:
        try:
            hint = get_hint(problem)
        except Exception:
            hint = None
    return render(request, 'judge/problem_detail.html', {'problem': problem, 'form': form, 'hint': hint})


def submission_result(request, pk):
    sub = get_object_or_404(Submission, pk=pk)
    return render(request, 'judge/submission_result.html', {'sub': sub})
