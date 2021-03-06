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
    print '@attribute', term,'NUMERIC'
print '@attribute', '*class*', '{pos,neg}'
print

# Generate ARFF file data secion.
print '@data'
for p in POS:
    with open(p, 'r') as f:
        words = f.read().split()
        for term in TERMS:
            if term in words:
                if term[:2] == 'JJ':
                    ff = float(words.count(term) * 100/len(words))
                elif term[:2] == 'VB':
                    ff = float(words.count(term) * 80/len(words))
                elif term[:2] == 'RB':
                    ff = float(words.count(term) * 40/len(words))
                else :
                    ff = float(words.count(term)/len(words))
                ff = ff *10
                print "%.2f" % ff,
                
            else:
                print 0.0,
            
        print 'pos'
for n in NEG:
    with open(n, 'r') as f:
        words = f.read().split()
        for term in TERMS:
            if term in words:
                if term[:2] == 'JJ':
                    ff = float(words.count(term) * 100/len(words))
                elif term[:2] == 'VB':
                    ff = float(words.count(term) * 80/len(words))
                elif term[:2] == 'RB':
                    ff = float(words.count(term) * 40/len(words))
                else :
                    ff = float(words.count(term)/len(words))
                ff = ff *10
                print "%.2f" % ff,
            else:
                print 0.0,
        print 'neg'
