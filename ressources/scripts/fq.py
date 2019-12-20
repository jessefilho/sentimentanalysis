#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 15:59:25 2019

@author: jessefilho
"""
"""
RUN with the follow command
$ python2.7 ../ressources/scripts/fq.py train/v-words.txt
"""

import os
import sys

from future import division
from collections import defaultdict

# %%


pathFile = '/Users/jessefilho/Documents/BDMA/M2/NPL/sentimentanalysis/corpus/train/v-words.txt'

pos = '/Users/jessefilho/Documents/BDMA/M2/NPL/sentimentanalysis/corpus/train/pos-words'
neg = '/Users/jessefilho/Documents/BDMA/M2/NPL/sentimentanalysis/corpus/train/neg-words'

TERMS = []

# Read terms from the vocabulary file indicated by the first parameter.
with open(pathFile, 'r') as f:
    TERMS = f.read().splitlines()
    
    
 
# Read all positive document file names
POS = []
for f in os.listdir(pos):
    if f.endswith(".txt"):
        POS.append('%s/%s' % (pos, f))

# Read all negative document file names
NEG = []
for f in os.listdir(neg):
    if f.endswith(".txt"):
        NEG.append('%s/%s' % (neg, f))


# %%
# Generate ARFF file data secion.

for p in POS:
    with open(p, 'r') as f:
        words = f.read().split()
        for term in TERMS:
            #print('term',term,words.count(term), len(words), words.count(term)/len(words))
            print(term,words.count(term)/len(words))
            #print words.count(term)/len(words)
        print ('pos')
#for n in NEG:
#    with open(n, 'r') as f:
#        words = f.read().split()
#        for term in TERMS:
#            if term in words:
#                print 1,
#            else:
#                print 0,
#        print ('neg')
        
