# AIAgentApp

A simple LLM-powered command-line application built while following the Boot.dev "Build an AI Agent in Python" tutorial. The course authors and maintainers include Lane Wagner, Waseem, Allan, Dan, and Matt. See the original course for details: https://www.boot.dev/courses/build-ai-agent-python

## Overview

This project demonstrates how to create an agentic coding tool that can read, update, and run Python code using the Gemini API (or another LLM provider). It is intended as a learning project and a minimal, extendable base for experiments.

## Contents

- main.py — application entrypoint
- pyproject.toml — project metadata and dependencies
- uv.lock — lock file

(Adjust this list if you add or remove files.)

## Getting started

1. Install dependencies (see `pyproject.toml`).
2. Configure any required API keys or environment variables for your LLM provider (e.g., Gemini).
3. Run the application:

		python main.py

## Usage

Describe how to use the CLI here, for example:

- Read code: explain command
- Update code: explain command
- Run code: explain command

Add concrete examples when you add commands to the program.

## Development

- Python: specify version used (e.g., 3.11+)
- Virtualenv or venv recommended
- Tests: add test instructions when tests are added

## Commit / Action / Evolution Log

Use this section to summarize important commits, actions, or evolutionary steps in the project. Each entry should include a date, a short title, and a brief description of why the change was made.

Example template entry:

- YYYY-MM-DD — Title of change
	- Commit/Action: short git commit message or action performed
	- Files affected: list of files changed
	- Summary: one-paragraph description of the change and why it was made

Start adding entries below as you make progress.

### Changelog

- Create project
    - Add uv package
    - Create environment with uv 
    ```bash 
    uv venv
    ```
    - activate environment
    ```bash
    source .venv/bin/activate
    ```
    - Create Gemini API key and add to .env file
    - Add call to load_dotenv() in main.py to load api key
    - Import Gemini library
    - Tested first call with hardcoded prompt
    - Deleted hardcoded prompt for prompt in argv[1] and added usage message if no prompt provided