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
    return klass.normalize(str)


def main():
  bigram = NgramParser.parse('The quick brown fox and the quick blue hare.')


if __name__ == '__main__':
  main()

