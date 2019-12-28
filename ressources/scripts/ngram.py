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



# set nggram here
n = 1
bag = []
for token in sys.stdin:
    token = token.strip().split()
    if len(token) != 3:
        continue
    
    word=''
    for tag in TAGS:
            if tag in token[1]:
                if token[2] == '<unknown>':
                    word = '%s%s' % (term(token[0]))
                else:
                    word = '%s%s' % (term(token[2]))
    
    
    bag.append(word)

ngrams = zip(*[bag[i:] for i in range(n)])

#print [" ".join(ngram) for ngram in ngrams]

#print only the ngrams
for ngram in [" ".join(ngram) for ngram in ngrams]:
    lenght_gram = ngram.split()
    
    if len(lenght_gram) == n:
        print "_".join(lenght_gram)
    
    
    
    
    #print "_".join(ngram_list)
    # Use the zip function to help us generate n-grams
    # Concatentate the tokens into ngrams and return
    #
    #print [" ".join(ngram) for ngram in ngrams]
    
    #Assumption that the token arrive in order
    #concat until ngram quantity
    # she is beautiful
    # Ex: for ngram = 3
    # NNshe_VBis_JJbeautiful
 
        
        
                    
    
