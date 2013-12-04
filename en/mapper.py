#!/usr/bin/env python
import sys
import re

id_regex = re.compile('<IDNo agency="handle">([^<]+)</IDNo>')
en_regex = re.compile('<AuthEnty[^>]*>([^<]+)</AuthEnty>')

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
        entity = next(en_regex.finditer(line)).groups()[0]
    except StopIteration: continue
    
    print '%s\t%s' % (handle, clean(entity))