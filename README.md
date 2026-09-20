# Python Ecosystem Release Lab

Reproducible experiments testing Python ecosystem compatibility across upcoming Python releases, platforms, and architectures.

The repository contains small compatibility tests for important Python packages against pre-release and newly released Python versions.

Detailed analysis and interpretation of the results are published separately. This repository contains the reproducible experiments.

## Requirements

The project uses [uv](https://docs.astral.sh/uv/) for Python and dependency management.

Check your installation:

```bash
uv --version
```

## Clone the Repository

```bash
git clone https://github.com/USERNAME/python-ecosystem-release-lab.git
cd python-ecosystem-release-lab
```

Replace `USERNAME` with the GitHub account or use the repository URL from GitHub.

## Install the Required Python Version

The Python version used by the current experiment is defined in:

```text
.python-version
```

Install it with:

```bash
uv python install
```

Verify the interpreter:

```bash
uv run python --version
```

## Install Dependencies

Synchronize the project environment:

```bash
uv sync
```

This creates the local `.venv` and installs the dependencies defined by the project.

## Run the Experiments

Experiments are grouped by Python version.

For Python 3.15:

```bash
uv run python315/numpy_test.py
uv run python315/pandas_test.py
uv run python315/polars_test.py
uv run python315/scipy_test.py
uv run python315/sklearn_test.py
uv run python315/matplotlib_test.py
uv run python315/pydantic_test.py
```

Individual scripts are intentionally small and test representative operations rather than full package test suites.

## Test Wheel Availability

To check whether a package provides a usable binary wheel for the current Python version and platform:

```bash
uv pip install --only-binary=:all: --reinstall PACKAGE
```

For example:

```bash
uv pip install --only-binary=:all: --reinstall numpy
```

Using `--only-binary=:all:` prevents source builds. A failed installation therefore exposes missing usable wheels for the current Python ABI and platform.

## Results

Results for each Python release are stored alongside the experiments.

For Python 3.15:

```text
python315/RESULTS.md
```

## Project Structure

```text
python-ecosystem-release-lab/
├── python315/
│   ├── RESULTS.md
│   ├── matplotlib_test.py
│   ├── numpy_test.py
│   ├── pandas_test.py
│   ├── polars_test.py
│   ├── pydantic_test.py
│   ├── scipy_test.py
│   └── sklearn_test.py
├── .python-version
├── pyproject.toml
├── uv.lock
└── README.md
```

Future Python releases will get their own experiment directories.

## Update the Repository

Pull the latest experiments:

```bash
git pull
```

Then synchronize the environment again:

```bash
uv sync
```

If the experiment uses a newer Python version that is not installed yet:

```bash
uv python install
uv sync
```

## Development

Install the project including development dependencies:

```bash
uv sync
```

Run Ruff:

```bash
uv run ruff check .
```

Check formatting:

```bash
uv run ruff format --check .
```

