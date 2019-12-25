#!/usr/bin/env python

# This script aims at generating vocabulary file from training corpus.
from __future__ import division
import os
import sys
import re

# %%


pathFile = '/Users/jessefilho/Documents/BDMA/M2/NPL/sentimentanalysis/corpus/train-tagged/v-tagged.txt'

pos = '/Users/jessefilho/Documents/BDMA/M2/NPL/sentimentanalysis/corpus/train-tagged/pos-tagged'
neg = '/Users/jessefilho/Documents/BDMA/M2/NPL/sentimentanalysis/corpus/train-tagged/neg-tagged'

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
        # Generate ARFF file attribute section.
reg = '\W|\d|' 

for term in TERMS:
    tagged_term = term.split()
    if (tagged_term[1] == 'JJ' or tagged_term[1] == 'RB' or tagged_term[1] == 'NN' or tagged_term[1] == 'VB'):
#        res = re.search(r"[a-zA-z]+", tagged_term[0])
        res = re.match(reg, tagged_term[0])
        if res != True:
            #print(res)
            print ('@attribute', tagged_term[0],'NUMERIC')
print ( '@attribute', '*class*', '{pos,neg}')



# %%
words = []
for p in POS:
    with open(p, 'r') as f:
        lines_pos = f.read().splitlines()
        for pos_element in lines_pos:
            posList = pos_element.split()
            words.append(posList[0])
            
# %%

unique_list = []
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
                if (tagged_term[1] == 'JJ' or tagged_term[1] == 'RB' or tagged_term[1] == 'NN' or tagged_term[1] == 'VB'):
                    res = re.search(reg, tagged_term[0])
                    if not res:
                        if tagged_term[0] not in unique_list:
                            unique_list.append(tagged_term[0])
                            fq = words.count(tagged_term[0])/len(words)
                            ff = format(fq, '.8f')
                            print (tagged_term[0],ff)
        print ('pos')
# %%
# Generate ARFF file data secion.
print '@data'
unique_list = []
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
            if (tagged_term[1] == 'JJ' or tagged_term[1] == 'RB' or tagged_term[1] == 'NN' or tagged_term[1] == 'VB'):
                res = re.search(reg, tagged_term[0])
                if not res:
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
            if (tagged_term[1] == 'JJ' or tagged_term[1] == 'RB' or tagged_term[1] == 'NN' or tagged_term[1] == 'VB'):
                re.search(reg, tagged_term[0])
                if not res:
                    fq = words.count(tagged_term[0])/len(words)
                    ff = format(fq, '.8f')
                    print ff,
        print 'neg'
# %%
# Generate ARFF file data secion.

#for p in POS:
#    with open(p, 'r') as f:
#        words = f.read().split()
#        for term in TERMS:
#            tagged_term = term.split()
#            
#            #print('term',term,words.count(term), len(words), words.count(term)/len(words))
#            #print(tagged_term[0],tagged_term[1],tagged_term[2])
#            
#            #adjectives, adverbs,nouns, and verbs.
#            
#           
#            
#            if (tagged_term[1] == 'JJ' or tagged_term[1] == 'RB' or tagged_term[1] == 'NN' or tagged_term[1] == 'VB'):
#                fq = words.count(tagged_term[0])/len(words)
#                res = re.search(r"[a-zA-z]+", tagged_term[0])
#                if res != True:
#                    print("Match found")
#                    print(tagged_term[0],fq)
#                else:
#                    print(tagged_term[0],fq)
#            #print words.count(term)/len(words)
#        print ('pos')
#for n in NEG:
#    with open(n, 'r') as f:
#        words = f.read().split()
#        for term in TERMS:
#            if term in words:
#                print 1,
#            else:
#                print 0,
#        print ('neg')
        
