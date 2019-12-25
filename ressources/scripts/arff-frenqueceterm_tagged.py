#!/usr/bin/env python

# This script aims at generating vocabulary file from training corpus.
from __future__ import division
import os
import sys
import re
from decimal import *

getcontext().prec = 3
if len(sys.argv) < 3:
    sys.exit()

TERMS = []

reg = '\W+'

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
# intilize a null list 
unique_list = []
count=0
for term in TERMS:
    tagged_term = term.split()
    if (tagged_term[1] == 'JJ' or tagged_term[1] == 'RB' or tagged_term[1] == 'NN' or tagged_term[1] == 'VB'):
#        res = re.search(r"[a-zA-z]+", tagged_term[0])
        res = re.search(reg, tagged_term[0])
        if not res:
            if tagged_term[0] not in unique_list:
                unique_list.append(tagged_term[0])
                count = count + 1
                print '@attribute', tagged_term[0],'NUMERIC'
print '@attribute', '*class*', '{pos,neg}'
print

# Generate ARFF file data secion.

print '@data', count

count=0
words = []
for p in POS:
    with open(p, 'r') as f:
        lines_pos = f.read().splitlines()
        # get only the words
        for pos_element in lines_pos:
            posList = pos_element.split()
            if (posList[1] == 'JJ' or posList[1] == 'RB' or posList[1] == 'NN' or posList[1] == 'VB'):
                res = re.search(reg, posList[0])
                if not res:
                    # get only the words
                    words.append(posList[0])
                    
        for term in TERMS:
            tagged_term = term.split()
            if tagged_term[0] in words:
                count = count + 1
                fq = words.count(tagged_term[0])/len(words)
                ff = format(fq, '.8f')
                print ff,
                
        print 'pos'

unique_list = []
words = []
for n in NEG:
    with open(n, 'r') as f:
        lines_pos = f.read().splitlines()
        # get only the words
        for pos_element in lines_pos:
            posList = pos_element.split()
            if (posList[1] == 'JJ' or posList[1] == 'RB' or posList[1] == 'NN' or posList[1] == 'VB'):
                res = re.search(reg, posList[0])
                if not res:
                    # get only the words
                    words.append(posList[0])
                    
        for term in TERMS:
            tagged_term = term.split()
            if tagged_term[0] in words:
                fq = words.count(tagged_term[0])/len(words)
                count = count + 1
                ff = format(fq, '.8f')
                print ff,
        print 'neg'


print count