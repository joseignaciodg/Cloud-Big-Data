from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession

conf = SparkConf().setMaster('local').setAppName('StockSummary')
sc = SparkContext(conf = conf)

spark = SparkSession(sc)

def rating(x):
 if(x <= 1):
   return "Range 1"
 elif(x <= 2):
   return "Range 2"
 elif(x <= 3):
   return "Range 3"
 elif(x <= 4):
   return "Range 4"
 else:
   return "Range 5"

RDD = sc.textFile("ratings.csv")
RDD_split = RDD.map(lambda line: line.split(','))
RDD_groups = RDD_split.map(lambda data: (data[1], float(data[2])))
df = RDD_groups.toDF(["movieId", "rate"])
df_query = df.groupBy("movieId").avg("rate")
RDD_df = df_query.rdd
RDD_rating = RDD_df.map(lambda m: (m[0], rating(float(m[1]))))
RDD_sort = RDD_rating.sortByKey()
RDD_sort.saveAsTextFile("output.txt")
 
