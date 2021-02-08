#!/usr/bin/python

import sys
import re

for line in sys.stdin:
    line = re.sub( r'^\W+|\W+$', '', line )
    url = line.split(" ")
    print(url[6] + '\t1')    
