SHELL=/bin/bash
PATH := .venv/bin:$(PATH)
EXTRA?=dev
export TEST?=./tests
VENV_ACTIVATE := . .venv/bin/activate

install:
	@set -e; \
	if [ ! -d .venv ]; then \
		python3 -m venv .venv; \
	fi; \
	$(VENV_ACTIVATE); \
	python3 -m pip install uv setuptools wheel; \
	python3 -m uv pip compile pyproject.toml -o requirements.txt --extra $(EXTRA); \
	python3 -m uv pip install -r requirements.txt;

unit:
	@python -B -m pytest -l --rootdir=. $${TEST};
