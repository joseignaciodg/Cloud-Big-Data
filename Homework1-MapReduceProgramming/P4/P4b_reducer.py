#!/usr/bin/python

import sys
import re

previous = None
sum = 0
movieId = []

for line in sys.stdin:
    line = re.sub(r'^\W+|\W+$', '', line)
    key, value = line.split('\t')
    
    if key != previous:
        if previous is not None:
            print previous + '\t' + str(movieId)
        previous = key
        movieId = [value]
    if value != movieId[-1]:
	movieId.append(value)

print previous + '\t' + str(movieId)
