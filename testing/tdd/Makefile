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

test: install-dep build test-pytest