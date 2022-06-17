test:
	poetry run pytest

lint:
	poetry run nox -s lint

clean:
	# Remove all .pyc and .pyo files as well as __pycache__ directories recursively starting from the current directory.
	find . | grep -E "(/__pycache__$$|\.pyc$$|\.pyo$$)" | xargs rm -rf

install:
	poetry build
	pip3.7 install ./dist/zettelwarrior-0.2.0-py3-none-any.whl

.PHONY: test lint clean

