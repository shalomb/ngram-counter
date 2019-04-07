#!/usr/bin/env python3

# -*- coding: utf-8 -*-

import re

from ascii_graph import Pyasciigraph
from ascii_graph.colors import *
from ascii_graph.colordata import vcolor
from ascii_graph.colordata import hcolor

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


class NgramHistogram:
  """
  Given a string and n for the n-gram, draw a histogram of the occurrences.
  """

  @classmethod
  def plot(klass, str):
    """
    Plot the n-gram histogram
    """
    bigram = NgramParser.parse(str)

    # Setup the histogram
    graph = Pyasciigraph( line_length=1,
                          separator_length=4 )

    pattern = [Gre, Yel, Red, Blu]
    graph_data = vcolor(bigram.items(), pattern)

    print(list(bigram.items()))

    # Render the histogram
    for line in graph.graph('bigram count', graph_data):
      print(line)


def main():
  NgramHistogram.plot('The quick brown fox and the quick blue hare.')

if __name__ == '__main__':
  main()

