#!/usr/bin/python

import sys
import re

for line in sys.stdin:
    line = re.sub( r'^\W+|\W+$', '', line )
    words = re.split(r"\W+", line)
    searchWord = sys.argv[1]     
    for word in words:
	if (word == searchWord):
        	print(line)
