## N-Gram Count Plotter

`ngram.py` is a python utility to plot a histogram of the occurrences of
n-grams computed from a given string.

e.g. For a plot of bigrams

```
./ngram.py --text 'the quick brown fox and the quick brown hare' --n 2
[('the quick', 2), ('quick brown', 2), ('brown fox', 1), ('fox and', 1), ('and the', 1), ('brown hare', 1)]
bigram count
######################################################################
++++++++++++++++++++++++++++++++++++++++++++++++++    2    the quick
++++++++++++++++++++++++++++++++++++++++++++++++++    2    quick brown
+++++++++++++++++++++++++                             1    brown fox
+++++++++++++++++++++++++                             1    fox and
+++++++++++++++++++++++++                             1    and the
+++++++++++++++++++++++++                             1    brown hare
```

For a plot of trigrams

```
./ngram.py --text 'the quick brown fox and the quick brown hare' --n 3
[('the quick brown', 2), ('quick brown fox', 1), ('brown fox and', 1), ('fox and the', 1), ('and the quick', 1), ('quick brown hare', 1)]
bigram count
###########################################################################
++++++++++++++++++++++++++++++++++++++++++++++++++    2    the quick brown
+++++++++++++++++++++++++                             1    quick brown fox
+++++++++++++++++++++++++                             1    brown fox and
+++++++++++++++++++++++++                             1    fox and the
+++++++++++++++++++++++++                             1    and the quick
+++++++++++++++++++++++++                             1    quick brown hare
```

To run `./ngram.py` in a docker container

```
make image
docker run -it -v "$PWD:$PWD" -w "$PWD" ngram /venv/runner --file "$PWD/path/to/some/file"
```

## Testing

Unit tests cover the n-gram parsing and counting logic and are invoked via `pytest`
using a make target.

```
$ make test
-----------------------------------------------------------
. venv/bin/activate ; \

pytest -rxXs --tap-stream tests/unit/NgramParser.py  --color=auto --full-trace
1..4
ok 1 tests/unit/NgramParser.py::TestPackageStructure.test_import_NgramParser
ok 2 tests/unit/NgramParser.py::TestNgramParser.test_ngram_parser_bigrams
ok 3 tests/unit/NgramParser.py::TestNgramParser.test_ngram_parser_bigrams_complex
ok 4 tests/unit/NgramParser.py::TestNgramParser.test_ngram_parser_trigrams
pytest -rxXs --cov=ngram tests/unit/NgramParser.py
================================ test session starts =================================
platform linux -- Python 3.7.3rc1, pytest-4.4.0, py-1.8.0, pluggy-0.9.0
rootdir: /home/unop/projects/bigram
plugins: tap-2.3, cov-2.6.1
collected 4 items

tests/unit/NgramParser.py ....                                                 [100%]

--------- coverage: platform linux, python 3.7.3-candidate-1 ---------
Name       Stmts   Miss  Cover
------------------------------
ngram.py      41     16    61%


============================== 4 passed in 0.03 seconds ==============================
```

## Deployment

A `Makefile` is included to install the necessary python dependencies
into a venv and run tests, etc.

```
make venv   # Setup a venv and install all prerequisites on a clean slate
make run    # Run ./ngram.py
make image  # Create a docker image with a venv to run ./ngram.py
make test   # Run NgramParser unit tests
make clean  # Clean up workspace and remove venv back to a clean slate
make all    # Do a complete end-to-end and run all make targets
            # i.e. make venv, make test, make run, make clean
```

`make venv` will attempt to install these for a debian-based system/container
if they are found to be missing.

* `pip3` (from `python3-pip` or similar)
* `venv` (from `python3-venv` or similar)
* `curl`

