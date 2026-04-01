VENV = .venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip

# 1
make_venv:
	python3 -m venv $(VENV)

install_dep: make_venv
	$(PIP) install -r requirements.txt

install: install_dep
	$(PIP) install -e .

start_file:
	$(PYTHON) src/app.py

test: install start_file

# 2
check-requirements: make_venv
	$(PYTHON) tools/check_requirements.py
