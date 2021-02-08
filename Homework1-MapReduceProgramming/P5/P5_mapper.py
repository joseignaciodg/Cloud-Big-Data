#!/usr/bin/python

import sys
import re

for line in sys.stdin:
    line = re.sub( r'^\W+|\W+$', '', line )
    data = line.split(",")

    classtype = data[3]
    if(not any(char.isalpha() for char in data[4])):
	mass =  data[4]
    else:
	mass = data[5]

    if(mass != ""):
	print(classtype + '\t' + mass)   
