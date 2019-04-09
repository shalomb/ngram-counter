#!/usr/bin/env python3

# -*- coding: utf-8 -*-

import re

class NgramParser:

  """
  Utility class for parsing a string and constructing a dictionary representing
  the n-gram
  """

  @classmethod
  def normalize(klass, str, delimiter=' '):
    """
    Normalize a given string to a list of lower case delimiter delimited words
    """

    # Strip out leading/trailing space and then convert to lower case
    normalized = str.strip().lower()

    # strip out non-word, non-space chars
    normalized = re.sub('[^\w\s]', '', normalized)

    # Condense remaining duplicate non-word (whitespace, newlines) characters
    # to a single space character
    normalized = re.sub('\W+', ' ', normalized)

    return normalized.split(delimiter)

  @classmethod
  def parse(klass, str, n=2):
    """
    Return a dictionary of n-grams and the number of times they have been counted
    for a given string and n (where n=2 for digrams, n=3 for trigrams, etc)
    """

    # Derive tokens from string delimited by spaces
    tokens = klass.normalize(str=str, delimiter=' ')

    # Generate an ngrams list by zipping up elements of n lists each formed by
    # taking a tail slice of the tokens list with an increasing starting index
    ngrams = [ ' '.join(items) for items in
                zip(*[tokens[i:] for i in range(n)])
             ]

    # Create a dictionary from items in the ngrams set representing each of the
    # ngrams as keys and values being the number of times the item is counted
    return { item: ngrams.count(item) for item in set(ngrams) }


