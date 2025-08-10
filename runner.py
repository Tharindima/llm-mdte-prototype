"""
runner.py

Writes generated tests to a tests/ folder and invokes pytest,
returns tuple: (returncode, stdout, stderr)
"""

import subprocess
import os
from pathlib import Path

def write_tests_and_run(project_root: str, generated_tests: str):
    root = Path(project_root)
    tests_dir = root / "tests"
    tests_dir.mkdir(parents=True, exist_ok=True)
    test_file = tests_dir / "test_generated.py"
    test_file.write_text(generated_tests)

    # run pytest
    proc = subprocess.Popen(
        ["python", "-m", "pytest", "-q", "--disable-warnings", "--maxfail=1"],
        cwd=str(root),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    out, err = proc.communicate()
    return proc.returncode, out, err

if __name__ == "__main__":
    # example usage
    project_root = "."
    # assume generator produced something and that sample_app is a package
