.PHONY: install-develop
install-develop:
	pip install -e .

.PHONY: test
test:
	pytest

.PHONY: lint
lint:
	flake8
