# Repository Instructions

## Dependency And Vulnerability Work

This repository defines Docker files, so dependency remediation and vulnerability verification must be container-first.

- Do not run host-side package-manager commands that install or update dependencies, including `poetry update`, `poetry install`, `pip install`, `uv sync`, or `uvx poetry update`, unless the user explicitly approves host-environment mutation.
- Regenerate `poetry.lock`, run audits, and run dependency checks inside Docker or docker compose.
- If a tool such as `pip-audit` is required, install or execute it inside a disposable container context, not in the Kbuntu host Python or uv environment.
- Before running any dependency command, state whether it mutates the host or only the container.
- If Docker cannot be used, stop and report the blocker instead of falling back to host mutation.
