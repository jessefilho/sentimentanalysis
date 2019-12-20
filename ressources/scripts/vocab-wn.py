#!/usr/bin/env python

# This script aims at generating vocabulary file from training corpus
# without NN tagged words.

import sys

if len(sys.argv) < 3:
    sys.exit()

TERMS = {}

# Read POS terms from the file indicated by the first parameter.
with open(sys.argv[1], 'r') as f:
    terms = f.read().splitlines()
for term in terms:
    if term[0] == 'N':
        continue
    if TERMS.has_key(term):
        TERMS[term][0] += 1
    else:
        TERMS[term] = [0, 0]
        TERMS[term][0] = 1

# Read NEG terms from the file indicated by the second parameter.
with open(sys.argv[2], 'r') as f:
    terms = f.read().splitlines()
for term in terms:
    if term[0] == 'N':
        continue
    if TERMS.has_key(term):
        TERMS[term][1] += 1
    else:
        TERMS[term] = [0, 0]
        TERMS[term][1] = 1

for term in TERMS:
    p = int(TERMS[term][0])
    n = int(TERMS[term][1])
    d = abs(p - n) * 1.0
    if p > n:
        d = d / p
    if n > p:
        d = d / n
    if len(sys.argv) > 3:
        if d < float(sys.argv[3]):
            continue
        if len(sys.argv) > 4:
            if p < float(sys.argv[4]) and n < float(sys.argv[4]):
                continue
    print term
