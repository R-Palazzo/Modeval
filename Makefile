.PHONY: install-develop
install-develop:
	pip install -e .
	pip install pytest flake8

.PHONY: test
test:
	pytest

.PHONY: lint
lint:
	flake8
