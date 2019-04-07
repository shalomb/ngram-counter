default: test

.PHONY: test
test:
	. venv/bin/activate ; \
	$(info -----------------------------------------------------------)
	pytest -rxXs --tap-stream tests/unit/NgramParser.py  --color=auto --full-trace
	pytest -rxXs --cov=bigram tests/unit/NgramParser.py

.PHONY: venv
venv:
	pip3 install --upgrade --user pip setuptools wheel virtualenv
	python3 -m venv venv
	. venv/bin/activate ;\
	pip3 install -Ur requirements.txt

.PHONY: run
run: venv/bin/activate
	. venv/bin/activate ; \
	$(info -----------------------------------------------------------)
	./bigram.py

.PHONY: clean
clean:
	rm -fr ./venv/ __pycache__/ *.egg-info/ .coverage *.tap .pytest_cache

.PHONY: all
all: venv test run clean

