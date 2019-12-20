#!/usr/bin/env python

# This script aims at generating vocabulary file from training corpus.
from __future__ import division
import os
import sys


if len(sys.argv) < 3:
    sys.exit()

TERMS = []

# Read terms from the vocabulary file indicated by the first parameter.
with open(sys.argv[1], 'r') as f:
    TERMS = f.read().splitlines()

# Read all positive document file names
POS = []
for f in os.listdir(sys.argv[2]):
    if f.endswith(".txt"):
        POS.append('%s/%s' % (sys.argv[2], f))

# Read all negative document file names
NEG = []
for f in os.listdir(sys.argv[3]):
    if f.endswith(".txt"):
        NEG.append('%s/%s' % (sys.argv[3], f))

# Generate ARFF file attribute section.
print '@relation movie-review'
for term in TERMS:
    print '@attribute', term, 'NUMERIC'
print '@attribute', '*class*', '{pos,neg}'
print

# Generate ARFF file data secion.
print '@data'
for p in POS:
    with open(p, 'r') as f:
        words = f.read().split()
        for term in TERMS:
            print words.count(term),
        print 'pos'
for n in NEG:
    with open(n, 'r') as f:
        words = f.read().split()
        for term in TERMS:
            print words.count(term),
        print 'neg'
