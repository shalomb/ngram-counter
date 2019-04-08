[![Build Status](https://travis-ci.org/shalomb/ngram-counter.svg?branch=master)](https://travis-ci.org/shalomb/ngram-counter)

## N-Gram Count Plotter

`ngram-plot.py` is a python utility to plot a histogram of the occurrences of
n-grams computed from a given string.

e.g. For a plot of bigrams

```
./ngram-plot.py --text 'the quick brown fox and the quick brown hare' --n 2
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
./ngram-plot.py --text 'the quick brown fox and the quick brown hare' --n 3
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

To pass in a file as input

```
./ngram-plot.py --file /path/to/some/file
```

To run `./ngram-plot.py` in a docker container

```
make image
docker run --rm -it ngram /venv/runner /etc/motd
```

To supply a file on the docker host
```
docker run -it -v "$PWD:$PWD" -w "$PWD" ngram /venv/runner --file "$PWD/path/to/some/file"
```

## Testing

Unit tests cover the n-gram parsing and counting logic and are invoked via `pytest`
using a make target.

```
 $ make test
-----------------------------------------------------------
. venv/bin/activate ; \
sh -c ' \
        pytest -rxXs --tap-stream tests/unit/*.py  --color=auto --full-trace; \
        pytest -rxXs --cov=ngram  tests/unit/*.py; \
'
1..6
ok 1 tests/unit/NgramHistogram.py::TestPackageStructure.test_import_NgramHistogram
ok 2 tests/unit/NgramHistogram.py::TestNgramHistogram.test_ngram_Histogram
ok 3 tests/unit/NgramParser.py::TestPackageStructure.test_import_NgramParser
ok 4 tests/unit/NgramParser.py::TestNgramParser.test_ngram_parser_bigrams
ok 5 tests/unit/NgramParser.py::TestNgramParser.test_ngram_parser_bigrams_complex
ok 6 tests/unit/NgramParser.py::TestNgramParser.test_ngram_parser_trigrams
================================= test session starts =================================
platform linux -- Python 3.7.3rc1, pytest-4.4.0, py-1.8.0, pluggy-0.9.0
rootdir: /home/unop/projects/bigram
plugins: tap-2.3, cov-2.6.1
collected 6 items

tests/unit/NgramHistogram.py ..                                                 [ 33%]
tests/unit/NgramParser.py ....                                                  [100%]

================================== warnings summary ===================================
tests/unit/NgramHistogram.py::TestNgramHistogram::test_ngram_Histogram
...


--------- coverage: platform linux, python 3.7.3-candidate-1 ---------
Name                      Stmts   Miss  Cover
---------------------------------------------
ngram/NgramHistogram.py      14      0   100%
ngram/NgramParser.py         15      0   100%
ngram/__init__.py             2      0   100%
---------------------------------------------
TOTAL                        31      0   100%

======================== 6 passed, 1 warnings in 0.04 seconds =========================
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

