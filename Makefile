setup:
	python3 -m venv venv

install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	#python -m pytest -vv tests/*.py

lint:
	#hadolint Dockerfile #uncomment to explore linting Dockerfiles
	pylint app.py

all: install lint test
