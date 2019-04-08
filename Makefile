default: test

.PHONY: test
test:
	$(info -----------------------------------------------------------)
	. venv/bin/activate ; \
	sh -c ' \
		pytest -rxXs --tap-stream tests/unit/*.py  --color=auto --full-trace; \
		pytest -rxXs --cov=ngram  tests/unit/*.py; \
	'

.PHONY: image
image:
	docker build -t ngram .

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
	curl 'https://baconipsum.com/api/?type=meat-and-filler&paras=2&format=text' -o tmp/bacon-ipsum.txt
	. venv/bin/activate ; \
	./ngram-plot.py --file tmp/bacon-ipsum.txt --n 2

.PHONY: clean
clean:
	rm -fr ./venv/ __pycache__/ *.egg-info/ .coverage *.tap .pytest_cache tmp/bacon-ipsum.txt

.PHONY: all
all: venv test run clean

