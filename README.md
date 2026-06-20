# CI GitHub Actions Demo

This repository was created as part of a GitHub Actions homework assignment.

The goal of this project is to practice creating GitHub Actions workflows for basic CI tasks, running Python tests, using scheduled workflows, and running matrix builds.

## Project Files

* `main.py` - contains a simple Python function.
* `test_main.py` - contains unit tests using the Python `unittest` framework.
* `.github/workflows/` - contains the GitHub Actions workflow files.

## Workflows Implemented

### Task 1: Basic GitHub Actions Workflow

A basic workflow that runs when code is pushed to the repository.

The workflow checks out the code and prints:

```text
Hello, CI with GitHub Actions!
```

### Task 2: Running Python Tests

A workflow that sets up Python 3.9 and runs unit tests using `unittest`.

The workflow steps are:

1. Check out the code.
2. Set up Python 3.9.
3. Install dependencies.
4. Run the tests.

### Task 3: Scheduled Workflow

A scheduled workflow that runs every day at midnight UTC using cron syntax:

```text
0 0 * * *
```

The workflow prints:

```text
Scheduled build completed successfully!
```

### Task 4: Matrix Builds

A matrix workflow that runs the Python unit tests on multiple Python versions:

* Python 3.7
* Python 3.8
* Python 3.9
* Python 3.10

The workflow uses `ubuntu-22.04` to support Python 3.7 and uses `fail-fast: false` so all matrix jobs can run even if one version fails.

## How to View Workflow Results

Workflow runs can be viewed in the **Actions** tab of this GitHub repository.

All workflows were tested successfully before submission.

## Bonus Task: Self-Hosted Runner

For the optional bonus task, I configured a self-hosted GitHub Actions runner.

A self-hosted runner allows GitHub Actions workflows to run on my own machine instead of using a GitHub-hosted runner such as `ubuntu-latest`.

### Setup Process

1. Opened the GitHub repository.
2. Went to **Settings → Actions → Runners**.
3. Clicked **New self-hosted runner**.
4. Selected the operating system and architecture.
5. Followed the commands provided by GitHub to download and configure the runner.
6. Started the runner from the terminal.
7. Created a workflow that uses:

```yaml
runs-on: [self-hosted, linux, x64]
```

### Workflow Result

The self-hosted runner workflow was executed manually using `workflow_dispatch`.

The workflow successfully ran on my local machine and printed a confirmation message in the GitHub Actions logs.

