#!/usr/bin/env python

from collections import defaultdict
import sys


entities = defaultdict(lambda: None)

for line in sys.stdin:
    line = line.strip().split('\t')
    handle, entity = line[0], '\t'.join(line[1:])
    entities[handle] = entity

for h1 in entities:
    e1 = entities[h1]
    for h2 in entities:
        if h1==h2: continue
        e2 = entities[h2]
        if e1 == e2:
            print '%s\t%s' % (h1, h2)
