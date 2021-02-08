#!/usr/bin/python

import sys

for line in sys.stdin:
    movieId, rating = line.split('\t')
    RangeStr = " "

    rating = float(rating)
    if(rating <= 1):
	RangeStr = "Range 1"
    elif(rating <= 2):
	RangeStr = "Range 2"
    elif(rating <= 3):
	RangeStr = "Range 3"
    elif(rating <= 4):
	RangeStr = "Range 4"
    elif(rating <= 5):
	RangeStr = "Range 5"
    
    print(RangeStr + '\t' + str(movieId))   
