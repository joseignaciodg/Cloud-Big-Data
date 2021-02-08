from pyspark import SparkConf, SparkContext
import string
import sys

conf = SparkConf().setMaster('local').setAppName('DistributedGrep')
sc = SparkContext(conf = conf)
RDD = sc.textFile("input.txt")
word = sys.argv[1]
linesWithWord = RDD.filter(lambda line: word in line)
linesWithWord.saveAsTextFile("output.txt")
