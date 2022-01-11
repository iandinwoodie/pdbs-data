.DEFAULT_GOAL := help

.PHONY: data
data: ## Generate the processed data file for this project.
	@echo "Generating data sets ..."
	python src/build_data_sets.py

.PHONY: test
test: ## Perform available tests on for this project.
	PYTHONPATH=./src python -m pytest --cov=src tests

.PHONY: clean
clean: ## Delete all files that are normally created by running make.
	@find . -type d -name '__pycache__' -exec rm -rf {} +
	@find . -type f -name '*.py[co]' -exec rm -f {} +

.PHONY: utils
utils: ## Run the registered utilities on the project.
	@echo "Running formatter ..."
	python -m black .
	@echo "Running type checker ..."
	python -m mypy --ignore-missing-imports .
	@echo "Running linter ..."
	python -m pylint src tests

.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) \
		| sort \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-16s\033[0m %s\n", $$1, $$2}'
