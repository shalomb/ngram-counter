#!/usr/bin/env python3

# -*- coding: utf-8 -*-

import argparse

from ngram import NgramParser
from ngram import NgramHistogram


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

  for line in NgramHistogram.plot( str=str, n=n ):
    print(line)

if __name__ == '__main__':
  main()

