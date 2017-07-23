.PHONY: clean-pyc clean-build help
halabasterelp:
	@perl -nle'print $& if m{^[a-zA-Z_-]+:.*?## .*$$}' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-25s\033[0m %s\n", $$1, $$2}'

clean: clean-build clean-pyc

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr *.egg-info

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

lint: ## check style with flake8
	python3 runtests.py --lintonly

test: ## run tests quickly with the default Python
	python3 runtests.py --nolint

test-all: ## run tests on every Python version with tox
	tox

coverage: ## check code coverage quickly with the default Python
	python3 runtests.py --nolint --coverage

release: clean ## package and upload a release
	echo 'Important notes'
	echo 'Update the Changelog version and date in README.rst'
	echo 'Bump version'
	echo 'Update git version/tag'
	python3 setup.py sdist bdist_wheel
	twine upload dist/*

sdist: clean ## package
	python3 setup.py sdist bdist_wheel
	ls -l dist
