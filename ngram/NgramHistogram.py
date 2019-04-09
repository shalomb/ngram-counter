#!/usr/bin/env python3

# -*- coding: utf-8 -*-

from ngram import NgramParser

from ascii_graph import Pyasciigraph
from ascii_graph.colors import *
from ascii_graph.colordata import vcolor
from ascii_graph.colordata import hcolor

class NgramHistogram:
  """
  Given a string and n for the n-gram, draw a histogram of the occurrences.
  """

  @classmethod
  def plot(klass, str, n, action='print'):
    """
    Plot the n-gram histogram
    """
    bigram = NgramParser.parse(str, n)

    # Setup the histogram
    graph = Pyasciigraph( line_length=1,
                          separator_length=4,
                          graphsymbol='+')

    pattern = [Gre, Yel, Red, Blu]
    graph_data = vcolor(bigram.items(), pattern)

    # Yield the histogram
    for line in graph.graph('bigram count', graph_data):
      yield(line)

