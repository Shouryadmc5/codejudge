import os
import sys
import tempfile
import textwrap
import subprocess

try:
    import resource
except Exception:
    resource = None


def run_submission(problem, user_code, timeout=5):
    """Run the user's code together with the problem tests.

    Implementation details:
    - Creates a temporary directory containing `solution.py` and `harness.py`.
    - `harness.py` will import `solution` and then execute the `tests` defined on the `Problem` model.
    - Runs `python harness.py` in a subprocess with a timeout and returns pass/fail and output.

    SECURITY: This is only a simple demo runner. Running arbitrary code is dangerous. Use an isolated sandbox in production.
    """
    tmpdir = tempfile.mkdtemp(prefix='codejudge_')
    sol_path = os.path.join(tmpdir, 'solution.py')
    harness_path = os.path.join(tmpdir, 'harness.py')

    with open(sol_path, 'w', encoding='utf-8') as f:
        f.write(user_code)

    tests_code = textwrap.indent(problem.tests or '', ' ' * 8)
    harness = textwrap.dedent(f"""
    import sys
    try:
        import solution as user_solution
    except Exception as e:
        print('ERROR importing user solution:', e)
        raise

    # begin tests
    try:
{tests_code}
    except AssertionError as e:
        print('ASSERTION ERROR:', e)
        raise
    except Exception as e:
        print('ERROR during tests:', e)
        raise

    print('ALL TESTS PASSED')
""")

    with open(harness_path, 'w', encoding='utf-8') as f:
        f.write(harness)

    # Run harness in a subprocess using the same Python executable
    cmd = [sys.executable, harness_path]
    try:
        # On Unix we can optionally set resource limits
        preexec = None
        if resource is not None:
            def _limit():
                # 50 MB address space, 2s CPU time (soft), use cautiously
                try:
                    resource.setrlimit(resource.RLIMIT_AS, (50 * 1024 * 1024, resource.RLIM_INFINITY))
                except Exception:
                    pass
                try:
                    resource.setrlimit(resource.RLIMIT_CPU, (timeout, timeout + 1))
                except Exception:
                    pass
            preexec = _limit

        completed = subprocess.run(
            cmd,
            cwd=tmpdir,
            capture_output=True,
            text=True,
            timeout=timeout,
            preexec_fn=preexec,
        )
        output = (completed.stdout or '') + '\n' + (completed.stderr or '')
        passed = completed.returncode == 0
    except subprocess.TimeoutExpired:
        output = f'Timeout after {timeout}s\n'
        passed = False

    return {'passed': passed, 'output': output}
