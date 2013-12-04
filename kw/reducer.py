#!/usr/bin/env python

from collections import defaultdict
import sys

THRESHOLD = 0.2

keywords = defaultdict(lambda: set())

for line in sys.stdin:
    line = line.strip().split('\t')
    handle, kw = line[0], '\t'.join(line[1:])
    keywords[handle].add(kw)

for h1 in keywords:
    for h2 in keywords:
        if h1==h2: continue
        intersection = keywords[h1].intersection(keywords[h2])
        if intersection:
            score = float(len(intersection)) / len(keywords[h1])
            if (score >= THRESHOLD):
                print '%s\t%s' % (h1, h2)