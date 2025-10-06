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

- 2025-10-06 — Initial README rewrite
	- Commit/Action: Rewrite README to add structure and changelog template
	- Files affected: `README.md`
	- Summary: Reorganized the README with clear sections (Overview, Getting started, Usage, Development) and added a template for summarizing commits/actions/evolution.

--

If you'd like, I can also: add a CONTRIBUTING.md, create a short Makefile or tasks for common dev steps, or scaffold a simple changelog script to append entries automatically. Tell me which you'd prefer next.