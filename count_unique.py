#!/usr/bin/env python3

# Copyright (c) 2013 Gerald Senarclens de Grancy <oss@senarclens.eu>
# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. It is provided for educational
# purposes and is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.

"""
This program counts how many times each word in a given text file occurs.

The result is printed to the terminal.
"""

import argparse
import sys
import string
from collections import namedtuple


def main():
    """
    Entry Point if started as designated program.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("infile", help="Text file to be analyzed.")
    args = parser.parse_args()
    with open(args.infile, encoding="utf-8") as f:
        text = f.read()
    words = text.split()
    unique_words(words)


def unique_words(words):
    """
    Return a dictionary of unique words and the number of their occurence.

    Two words are considered the same only when they have exactly the same
    characters. However, the characters are not compared case sensitive.
    Eg. 'vaLuE' is considered the same as 'Value'.
    Also, some of the words still contain punctuation marks which have to be
    removed before comparison.

    `words` - a list of words
    """
    counter = {}
    for word in words:
        clean = word.strip(string.punctuation).lower()
        if clean in counter:
            counter[clean] += 1
        elif clean:
            counter[clean] = 1
    return counter


def count_unique_sorted(words):
    """
    Return a list of named tuples containing the frequency of each word.

    The first element of each named tuple is 'word' and the second 'count'.
    The list has to contain the tuples in the same order as they occur in the
    argument.

    `words` - a list of words
    """
    Pair = namedtuple('Pair', ['word', 'count'])
    tuple_list = []
    for key, value in unique_words(words).items():
        tuple_list.append(Pair(key, value))
    return tuple_list



if __name__ == "__main__":
    sys.exit(main())
