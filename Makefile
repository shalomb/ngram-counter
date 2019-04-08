default: test

.PHONY: test
test:
	$(info -----------------------------------------------------------)
	. venv/bin/activate ; \
	sh -c ' \
		pytest -rxXs --tap-stream tests/unit/NgramParser.py  --color=auto --full-trace; \
		pytest -rxXs --cov=ngram  tests/unit/NgramParser.py; \
	'

.PHONY: venv
venv:
	test -e "$(shell which pip3)" || apt install -y --no-install-recommends --no-install-suggests curl python3-pip python3-venv
	pip3 install --upgrade --user setuptools wheel virtualenv
	python3 -m venv venv
	. venv/bin/activate ;\
	pip3 install -Ur requirements.txt

.PHONY: run
run: venv/bin/activate
	$(info -----------------------------------------------------------)
	mkdir -p tmp
	curl 'https://baconipsum.com/api/?type=meat-and-filler&paras=10&format=text' -o tmp/bacon-ipsum.txt
	. venv/bin/activate ; \
	./ngram.py --file tmp/bacon-ipsum.txt

.PHONY: clean
clean:
	rm -fr ./venv/ __pycache__/ *.egg-info/ .coverage *.tap .pytest_cache tmp/bacon-ipsum.txt

.PHONY: all
all: venv test run clean

