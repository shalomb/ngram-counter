#!/usr/bin/env python3

# -*- coding: utf-8 -*-

# pytest -rxXs --tap-stream tests/unit/NgramParser.py  --color=auto --full-trace -k return

import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))


class TestPackageStructure(unittest.TestCase):

  def test_import_NgramParser(self):
    # Arrange
    from bigram import NgramParser


class TestNgramParser(unittest.TestCase):

  def test_ngram_parser(self):
    # Arrange
    from bigram import NgramParser

    input     = 'The quick brown fox and the quick blue hare.'
    expected  = { 'the quick'   : 2,
                  'quick brown' : 1,
                  'brown fox'   : 1,
                  'fox and'     : 1,
                  'and the'     : 1,
                  'quick blue'  : 1,
                  'blue hare'   : 1
              }

    # Act & Assert
    assert NgramParser.parse(input, n=2) == expected

