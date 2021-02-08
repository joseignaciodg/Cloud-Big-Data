#!/usr/bin/python

import sys
import re

for line in sys.stdin:
    line = re.sub( r'^\W+|\W+$', '', line )
    data = line.split(",")
    
    date = data[0] 
    year = date.split("-")
    print(year[0] + '\t' + data[4])   
