# Django Codespace Example

[![CI](https://github.com/spenserblack/django-codespace-example/actions/workflows/ci.yml/badge.svg)](https://github.com/spenserblack/django-codespace-example/actions/workflows/ci.yml)

An example of a GitHub codespace for a Django app

See [GitHub's official Django codespace template, too](https://github.com/github/codespaces-django).

## Getting Started

Click the "Code" button in the top right, and use the "Codespaces" tab to crate a new codespace.

This will automatically
- set up extensions like EditorConfig
- Install dependencies
- Perform database migrations

to let you spend more time coding and less time setting up your workspace.

Additionally, while not related to codespaces themselves, the CI will perform code quality checks
and tests for changes to the main branch and pull requests targeting the main branch.

## Development / Codespace Management

You can configure codespace prebuilds in the Repository settings tab, under "codespaces".
This will set up a workflow automatically build the devcontainer, allowing for faster start
times when creating a new codespace.
