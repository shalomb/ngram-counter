#!/usr/bin/env python3

# -*- coding: utf-8 -*-

# pytest -rxXs --tap-stream tests/unit/NgramHistogram.py  --color=auto --full-trace -k return

import os
import sys
import unittest

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

    input     = 'The quick brown fox and the quick blue hare.'
    n         = 2

    # Act & Assert
    NgramHistogram.plot( str=input, n=n )


