#!/usr/bin/env python3

# -*- coding: utf-8 -*-

import re

class NgramParser:
  """
  Ngram parser utility class
  """

  @classmethod
  def normalize(klass, str):
    """
    Normalize the string to be fed into the parser
    """

    normalized = str.lower()
    normalized = re.sub('[^\w\s]', '', normalized)

    return normalized

  @classmethod
  def parse(klass, str):
    """
    Parse a string and decompose it into ngrams
    """

    # Split string by spaces assuming spaces are delimiters
    tokens = klass.normalize(str).split(' ')

    # Compute ngrams
    ngrams = [ ' '.join(pairs) for pairs in
                zip(*[tokens[i:] for i in [0, 1]])
             ]

    # Count the occurences of each ngram
    counts = {}
    for item in ngrams:
      counts.update({ item: counts[item] + 1 if item in counts else 1 }) # Ugh

    return counts



def main():
  bigram = NgramParser.parse('The quick brown fox and the quick blue hare.')


if __name__ == '__main__':
  main()

