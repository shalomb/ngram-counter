#!/usr/bin/env python3

# -*- coding: utf-8 -*-

import re
import argparse

from ascii_graph import Pyasciigraph
from ascii_graph.colors import *
from ascii_graph.colordata import vcolor
from ascii_graph.colordata import hcolor

class NgramParser:

  """
  Utility class for parsing a string and constructing a dictionary representing
  the n-gram
  """

  @classmethod
  def normalize(klass, str):
    """
    Normalize a given string to a list of lower case space separated words
    """

    # Strip out leading/trailing space and then convert to lower case
    normalized = str.strip().lower()

    # strip out non-word, non-space chars
    normalized = re.sub('[^\w\s]', '', normalized)

    # Remove consequitive duplicate horizontal whitespace to single spaces char
    normalized = re.sub('\W+', ' ', normalized)

    return normalized

  @classmethod
  def parse(klass, str, n=2):
    """
    Return a dictionary of n-grams and the number of times they have been counted
    for a given string and n (where n=2 for digrams, n=3 for trigrams, etc)
    """

    # Split string by spaces assuming spaces are delimiters
    tokens = klass.normalize(str).split(' ')

    # Generate an ngrams list by zipping up elements of n lists each formed by
    # taking a tail slice of the tokens list with an increasing starting index
    ngrams = [ ' '.join(items) for items in
                zip(*[tokens[i:] for i in range(n)])
             ]

    # Create a dictionary from items in the ngrams list representing each of
    # the ngrams as keys and whose values are the number of times the item is seen
    counts = {}
    for item in ngrams:
      counts.update({ item: counts[item] + 1 if item in counts else 1 }) # Ugh

    return counts


class NgramHistogram:
  """
  Given a string and n for the n-gram, draw a histogram of the occurrences.
  """

  @classmethod
  def plot(klass, str, n):
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

    print(list(bigram.items()))

    # Render the histogram
    for line in graph.graph('bigram count', graph_data):
      print(line)


def cli_args():
  parser = argparse.ArgumentParser(description='n-gram histogram plotter')

  parser.add_argument('--file',     action = 'store',
      help='File containing text to parse for n-grams')

  parser.add_argument('--text',     action = 'store',
      help='Text to parse for n-grams')

  parser.add_argument('--n',     action = 'store',
      help='The n in n-gram. 2 for bigram, 3 for trigram, 4 for quadgram, etc')

  return parser.parse_args()


def main():
  args = cli_args()

  if args.file:
    with open(args.file) as file:
      str = file.read()
  else:
    str = args.text   if args.text else 'The quick brown fox and the quick blue hare.'

  n   = int(args.n) if args.n    else 2   # n=2 for bigrams, n=3 for trigrams, etc

  NgramHistogram.plot( str=str, n=n )

if __name__ == '__main__':
  main()

