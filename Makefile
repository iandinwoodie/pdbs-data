.DEFAULT_GOAL := help

.PHONY: test
test: ## Perform self tests on the program this makefile builds.
	pytest

.PHONY: clean
clean: ## Delete all files that are normally created by running make.
	@find . -type d -name '__pycache__' -exec rm -rf {} +
	@find . -type f -name '*.py[co]' -exec rm -f {} +

.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) \
		| sort \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-16s\033[0m %s\n", $$1, $$2}'
