from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession

conf = SparkConf().setMaster('local').setAppName('StockSummary')
sc = SparkContext(conf = conf)

spark = SparkSession(sc)

RDD = sc.textFile("GOOGLE.csv")
RDD_split = RDD.map(lambda line: line.split(','))
RDD_groups = RDD_split.map(lambda data: (data[0].split('-')[0], float(data[4])))
df = RDD_groups.toDF(["year", "price"])
df_query = df.groupBy("year").avg("price")
RDD_df = df_query.rdd
RDD_sort = RDD_df.sortByKey()
RDD_sort.saveAsTextFile("output.txt")

