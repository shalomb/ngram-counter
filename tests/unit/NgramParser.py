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
    input   = 'The quick brown fox and the quick blue hare.'
    output  = [ 'the quick', 'quick brown', 'brown fox', 'fox and', 'and the',
                'the quick', 'quick blue', 'blue hare' ]

    # Act & Assert
    assert NgramParser.parse(input) == output

