#!/usr/bin/env python

# This script aims at removing useless words from a sentiment classification corpus.

import sys
import re
from nltk.util import ngrams

if len(sys.argv) != 2:
    sys.exit()

for line in sys.stdin:
    words = line.strip().split()
    tokens = [token for token in words if token != ""]
    output = list(ngrams(tokens, 2))
    for outp in output:
    	print outp


