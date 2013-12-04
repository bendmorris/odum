#!/usr/bin/env python

from collections import defaultdict
import sys


times = {}

for line in sys.stdin:
    line = line.strip().split('\t')
    handle, start_time, end_time = line
    start_time, end_time = int(start_time), int(end_time)
    times[handle] = (start_time, end_time)

for h1 in times:
    s1, e1 = times[h1]
    for h2 in times:
        if h1==h2: continue
        s2, e2 = times[h2]
        # check for overlap:
        #   1) event 2 started during event 1,
        #   2) event 2 ended during event 1,
        #   3) event 2 started before and ended after event 1
        if s1 <= s2 <= e1 or s1 <= e2 <= e1 or s2 <= s1 and e2 >= e1:
            print '%s\t%s' % (h1, h2)
