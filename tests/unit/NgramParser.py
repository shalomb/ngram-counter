#!/usr/bin/env python3

# -*- coding: utf-8 -*-

# pytest -rxXs --tap-stream tests/unit/NgramParser.py  --color=auto --full-trace -k return

import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))


class TestPackageStructure(unittest.TestCase):

  def test_import_NgramParser(self):
    """
    Test that the NgramParser class is importable. This is only a structural
    test but is a common operation in all the Arrange steps for following tests
    """
    # Arrange
    from ngram import NgramParser


class TestNgramParser(unittest.TestCase):

  def test_normalize(self):
    """
    Test the normalize method
    """

    # Arrange
    from ngram import NgramParser

    input    = 'The quick brown fox and the quick blue hare.'
    expected = [ 'the', 'quick', 'brown', 'fox', 'and', 'the', 'quick',
                 'blue', 'hare' ]

    # Act & Assert
    assert NgramParser.normalize(input) == expected


  def test_ngram_parser_bigrams(self):
    """
    Test the parser's ability to handle the base/given case.
    """
    # Arrange
    from ngram import NgramParser

    input     = 'The quick brown fox and the quick blue hare.'
    n         = 2
    expected  = { 'the quick'   : 2,
                  'quick brown' : 1,
                  'brown fox'   : 1,
                  'fox and'     : 1,
                  'and the'     : 1,
                  'quick blue'  : 1,
                  'blue hare'   : 1
              }

    # Act & Assert
    assert NgramParser.parse(input, n) == expected


  def test_ngram_parser_bigrams_complex(self):
    """
    Test parser's ability to handle complex cases
    * Multi-line input containing newlines
    * Numbers as words
    * n-gram Occurrences > 2 (2 in the base case)
    """
    # Arrange
    from ngram import NgramParser

    input     = '''
      The quick brown fox jumped over the quick blue hare to catch the quick blue mouse.

      The quick blue hare dodged the charge of 2 quick brown hounds.

      Brown hounds and brown foxes are brown canines of 2 genera.
    '''

    n = 2

    expected  = { 'the quick'    : 4, 'quick blue'   : 3,
                  'quick brown'  : 2, 'brown hounds' : 2, 'blue hare'     : 2,
                  'of 2'         : 2,
                  'brown fox'    : 1, '2 genera'     : 1, '2 quick'       : 1,
                  'are brown'    : 1, 'and brown'    : 1, 'brown canines' : 1,
                  'brown foxes'  : 1, 'canines of'   : 1, 'charge of'     : 1,
                  'catch the'    : 1, 'blue mouse'   : 1, 'dodged the'    : 1,
                  'fox jumped'   : 1, 'foxes are'    : 1, 'hare dodged'   : 1,
                  'hare to'      : 1, 'hounds and'   : 1, 'hounds brown'  : 1,
                  'jumped over'  : 1, 'mouse the'    : 1, 'over the'      : 1,
                  'the charge'   : 1,
                  'to catch'     : 1,

              }

    # Act & Assert
    assert NgramParser.parse(input, n) == expected

  def test_ngram_parser_trigrams(self):
    """
    Test the parser's ability to handle n > 2 (n==3 for trigrams).
    Though not absolutely required to validate the functionality of bigrams,
    this is another data point to validate the algorithm is intact and can
    scale for n > 2.
    """

    # Arrange
    from ngram import NgramParser

    input     = 'The quick brown fox and the quick brown hare.'
    n         = 3
    expected  = { 'the quick brown'  : 2,
                  'quick brown fox'  : 1,
                  'brown fox and'    : 1,
                  'fox and the'      : 1,
                  'and the quick'    : 1,
                  'quick brown hare' : 1,
              }

    # Act & Assert
    assert NgramParser.parse(input, n) == expected

