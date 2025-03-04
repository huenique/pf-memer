.PHONY: lint

lint:
	ruff check --select I --fix && ruff format
