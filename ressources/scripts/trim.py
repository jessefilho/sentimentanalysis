#!/usr/bin/env python

# This script aims at removing useless words from a sentiment classification corpus.

import sys

if len(sys.argv) != 2:
    sys.exit()

# The first parameter (sys.argv[1]) should be the file name of stop words.
# All stop words will be loaded to the list stopwords.
stopwords = []
with open(sys.argv[1], 'r') as f:
    stopwords = f.read().splitlines()

# Alphabet in English.
ALPHA = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

# This function will determine whether a word should be considered as a term.
# Any other useful criteria could be added.
def term(word):
    if len(word) == 1:
        return False
    if word[0] not in ALPHA:
        return False
    while word[-1] not in ALPHA:
        word = word[:-1]
        if not len(word):
            return False
    if '\'' in word:
        return False
    return word

for line in sys.stdin:
    words = line.strip().split()
    for word in words:
        if word in stopwords:
            continue
        word = term(word)
        if not word:
            continue
        print word
