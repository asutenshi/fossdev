create-structure:
	mkdir src tests docs
	touch README.md setup.py requirements.txt
	touch docs/DOMAIN.md
	touch src./.gitkeep tests/.gitkeep

install-dep:
	pip install -r requirements.txt

build:
	pip install -e .

test-pytest:
	python -m pytest

create-venv:
	python -m venv .venv

activate-venv:
	. ./.venv/bin/activate

test: create-venv activate-venv install-dep build test-pytest