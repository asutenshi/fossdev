typecheck:
	$(PYTHON) -m mypy src/

lint:
	$(PYTHON) -m flake8 src/

format:
	$(PYTHON) -m black src/