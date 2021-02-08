from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster('local').setAppName('CountURLAccessFrequency')
sc = SparkContext(conf = conf)
RDD = sc.textFile("access_log")
RDD_split = RDD.map(lambda line: line.split())
RDD_url = RDD_split.map(lambda u: u[6])
RDD_url_counter = RDD_url.map(lambda u: (u, 1))
RDD_group = RDD_url_counter.reduceByKey(lambda u,num: u+num)
RDD_group.saveAsTextFile("output.txt")
  
