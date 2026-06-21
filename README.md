# Python CI/CD Learning Project

Welcome to your Python CI/CD learning repository! This project demonstrates the core structure and configuration files required to set up Continuous Integration (CI) for a Python project.

## Project Structure

Here is the directory structure we created:

```text
ETL_Devops/
│
├── .github/
│   └── workflows/
│       └── ci.yml             # GitHub Actions configuration file (CI Pipeline)
│
├── src/
│   └── math_ops.py            # Simple source code module containing logic
│
├── tests/
│   └── test_math_ops.py       # Automated unit tests using pytest
│
├── requirements.txt           # Python dependencies required for the project
└── README.md                  # This documentation file
```

---

## 1. The Core Files Explained

### 📄 `src/math_ops.py`
This represents your production codebase. It contains simple operations (`add` and `subtract`) that we want to automatically test and lint whenever we change our code.

### 📄 `tests/test_math_ops.py`
Contains the unit tests designed to run against your source code. Writing tests is a prerequisite for CI/CD, as the CI pipeline runs these tests automatically to ensure code updates don't break existing features.

### 📄 `requirements.txt`
Declares the dependencies your application needs. In a CI environment, we use this file to install packages like `pytest` (for running tests) and `flake8` (for checking code style/linting) before running the pipeline jobs.

### 📄 `.github/workflows/ci.yml`
This is your **GitHub Actions CI Pipeline configuration**. GitHub automatically detects this file and runs it on the events specified (e.g., whenever you `push` code or submit a `pull request` to the main branch).

It does the following:
1. Spins up a fresh environment running Linux (`ubuntu-latest`).
2. Tests your code against multiple Python versions (`3.9`, `3.10`, `3.11`) concurrently using a matrix strategy.
3. Checks out your repository code.
4. Installs the dependencies specified in `requirements.txt`.
5. Runs **flake8** to lint your code (verifying style guidelines and checking for syntax errors).
6. Runs **pytest** to verify all unit tests pass successfully.

---

## 2. Running Locally

Before pushing code to GitHub, it is best practice to run tests and linting locally to make sure your CI pipeline won't fail.

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Run Linting
Check your code style using `flake8`:
```bash
flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
```

### Step 3: Run Tests
Run your unit tests using `pytest`:
```bash
pytest
```
