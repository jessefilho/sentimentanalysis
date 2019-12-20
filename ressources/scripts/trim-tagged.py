#!/usr/bin/env python

# This script aims at removing useless words from a sentiment classification corpus.

import sys

TAGS = ['JJ', 'NN', 'RB', 'VB']

ALNUM = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'

# To replace special characters to '_' because Weka does not like them.
def term(token):
    term = ''
    for c in token:
        if not c in ALNUM:
            term += '_'
        else:
            term += c
    return term


for token in sys.stdin:
    token = token.strip().split()
    if len(token) != 3:
        continue
    for tag in TAGS:
        if tag in token[1]:
            if token[2] == '<unknown>':
                print '%s%s' % (tag, term(token[0]))
            else:
                print '%s%s' % (tag, term(token[2]))
