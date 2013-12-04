#!/usr/bin/env python
import sys
import re
import datetime

id_regex = re.compile('<IDNo agency="handle">([^<]+)</IDNo>')
tm_regex = re.compile('<timePrd event="(start|end)" date="([0-9]{4})-([0-9]{2})-([0-9]{2})">')

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
    
    dates = {}
    for match in tm_regex.finditer(line):
        t, y, m, d = match.groups()
        y, m, d = int(y), int(m), int(d)
        # get the date as an integer (number of days since 1/1/1)
        date = datetime.date(y, m, d).toordinal()
        dates[t] = date
    
    if 'start' in dates and 'end' in dates:
        print '%s\t%s\t%s' % (handle, dates['start'], dates['end'])