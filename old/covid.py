import pip
import uuid
import sys
import os
import subprocess
from pyspark.sql import SparkSession
from pyspark import SparkContext, SparkConf
import pyspark.sql.functions
import pyspark.sql
from pyspark.sql.functions import udf
import pyspark.sql.functions as F
from pyspark.sql.types import *
from pyspark.sql.functions import desc
from pyspark.sql.functions import *
from pyspark.sql.functions import size
import pyspark.sql.functions as func
from datetime import datetime, timedelta
import datetime 
import pandas as pd
spark = SparkSession.builder.appName("NTTtest").getOrCreate() 
df = spark.read.option("header","true").option("inferSchema","true").csv('/user/sanyi/owid-covid-data.csv') 
df2 = df.filter(col("location") == "Hungary")
df2 = df2[['date','location','new_cases', 'new_tests']]
df3 = df2.withColumn('CTratio', df2.new_cases/(df2.new_tests))

df3.orderBy('date',ascending=False).show()

pandas_df = df3.toPandas()
pandas_df
pandas_df.to_csv(r'outspark.csv')

