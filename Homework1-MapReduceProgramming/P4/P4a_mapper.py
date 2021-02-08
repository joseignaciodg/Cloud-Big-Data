#!/usr/bin/python

import sys
import re

for line in sys.stdin:
    line = re.sub( r'^\W+|\W+$', '', line )
    data = line.split(",")
    
    print(data[1] + '\t' + data[2])   
