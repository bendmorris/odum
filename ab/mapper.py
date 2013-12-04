#!/usr/bin/env python
import sys
import re

id_regex = re.compile('<IDNo agency="handle">([^<]+)</IDNo>')
ab_regex = re.compile('<abstract>([^<]+)</abstract>')

bad_chars = ''.join(c for c in map(chr, range(256)) if not c.isalnum())
def clean(word):
    '''Removes non-alphanumeric characters from word and converts to lower 
    case.'''
    return word.translate(None, bad_chars).lower()

for line in sys.stdin:
    line = line.strip()
    if not line: continue
    
    try:
        handle = next(id_regex.finditer(line)).groups()[0]
    except StopIteration: continue
    
    try:
        abstract = next(ab_regex.finditer(line)).groups()[0]
    except StopIteration: continue
    
    keywords = (clean(word) for word in abstract.split())
    
    for kw in keywords:
        if len(kw) >= 5:
            print '%s\t%s' % (handle, kw)
