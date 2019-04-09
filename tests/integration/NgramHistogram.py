#!/usr/bin/env python3

# -*- coding: utf-8 -*-

# pytest -rxXs --tap-stream tests/unit/NgramHistogram.py  --color=auto --full-trace -k return

import os
import sys
import unittest
import re
from functools import reduce

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))

class TestPackageStructure(unittest.TestCase):

  def test_import_NgramHistogram(self):
    """
    Test that the NgramHistogram class is importable. This is only a structural
    test but is a common operation in all the Arrange steps for following tests
    """
    # Arrange
    from ngram import NgramHistogram


class TestNgramHistogram(unittest.TestCase):

  def test_ngram_Histogram(self):
    """
    Test the histogram's ability to handle the base/given case.
    """
    # Arrange
    from ngram import NgramHistogram

    input = 'The quick brown fox and the quick blue hare.'
    n     = 2

    outputs   = [ 'bigram count', '##',
                  '2    the quick',
                  '1    quick brown',
                  '1    brown fox',
                  '1    fox and',
                  '1    and the',
                  '1    quick blue',
                  '1    blue hare',
                ]

    # Act
    # This is equivalent of invoking
    # ./ngram-plot.py --text "$some_text" --n "$n"
    graph = NgramHistogram.plot( str=input, n=n )

    # Assert
    # Strip out ANSI escape sequences for the colouring, they get in the
    # way of testing.
    output = [ re.sub( '.+?m', '', i) for i in list(graph) ]

    # For each item in outputs, ensure at least one line of the graph output
    # matches (partially). Note, this is at least O(n**2).
    for expected in outputs:
      assert reduce( (lambda x,y: x or y),
                     [ bool(re.search(expected, line)) for line in output ] )

if __name__ == '__main__':
  TestNgramHistogram().test_ngram_Histogram()


