from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession

conf = SparkConf().setMaster('local').setAppName('MeteoriteLanding')
sc = SparkContext(conf = conf)

spark = SparkSession(sc)

def divider(x, y):
  if(x != ''):
    if(not any(char.isalpha() for char in x)):
        return x
    else:
        if(y != ''):
           return y
        else:
           return "0"
  if(x == ''):
       return "0"

def typeMet(x, y):
  if(x[0] == '"'):
    x = x[1:len(x)]
    y = y[0:len(y) - 1]
    return x + y
  else:
    return x

RDD = sc.textFile("Meteorite_Landings.csv")
RDD_split = RDD.map(lambda line: line.split(','))
RDD_groups = RDD_split.map(lambda data: (typeMet(data[3], data[4]), divider(data[4], data[>
RDD_conversion = RDD_groups.map(lambda c: (c[0], float(c[1])))
df = RDD_conversion.toDF(["type", "mass"])
df_query = df.groupBy("type").avg("mass")
RDD_df = df_query.rdd
RDD_massAvg = RDD_df.map(lambda m: (m[0], m[1]))
RDD_sort = RDD_massAvg.sortByKey()
RDD_sort.saveAsTextFile("output.txt")

 
