#!/usr/bin/env python
import sys
import re

id_regex = re.compile('<IDNo agency="handle">([^<]+)</IDNo>')
kw_regex = re.compile('<keyword[^>]*>([^<]+)</keyword>')

for line in sys.stdin:
    line = line.strip()
    if not line: continue
    
    try:
        handle = next(id_regex.finditer(line)).groups()[0]
    except StopIteration: continue
    
    keywords = kw_regex.findall(line)
    
    for kw in keywords:
        print '%s\t%s' % (handle, kw)
