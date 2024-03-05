
# Working with Poetry for project dependencies

This guide provides an overview of how to use Poetry for managing the dependencies of the project.

## Prerequisites

Before you start, ensure you have Python installed on your system. Poetry supports Python 3.7 and newer versions.

## Installing Poetry

To install Poetry, run the following command in your terminal:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

This command downloads and executes the Poetry installation script.

### Installing Dependencies

Navigate to the project directory and install project dependencies as follows:

1. **Install All Dependencies**:

   ```bash
   poetry install
   ```

   This command installs all the dependencies listed in `pyproject.toml`.

### Updating Dependencies

To update your project's dependencies to their latest versions, use:

```bash
poetry update
```

This command updates all dependencies to the latest compatible versions and updates the `poetry.lock` file to reflect these changes.

## Setting the Python Interpreter to Poetry's Virtual Environment

Poetry creates a virtual environment for your project to manage dependencies separately from your global Python installation. To configure your IDE (e.g., Visual Studio Code) to use the Poetry-managed virtual environment:

1. **Find the Virtual Environment**: First, find the path to the virtual environment created by Poetry with:

   ```bash
   poetry env info --path
   ```

2. **Configure Your IDE**: In your IDE's settings, set the Python interpreter to the path provided by the above command. This ensures that your IDE uses the correct Python version and has access to all the dependencies installed by Poetry.
