import pandas as pd
import numpy as np
import pyspark

# import mysql.connector
# from pymongo import MongoClient

from datetime import datetime, date
  
# need to import to use pyspark
from pyspark.sql import Row
  
# need to import for session creation
from pyspark.sql import SparkSession
  
# creating the session
spark = SparkSession.builder.getOrCreate()
  
# schema creation by passing list
df = spark.createDataFrame([
    Row(a=1, b=4., c='GFG1', d=date(2000, 8, 1),
        e=datetime(2000, 8, 1, 12, 0)),
    
    Row(a=2, b=8., c='GFG2', d=date(2000, 6, 2), 
        e=datetime(2000, 6, 2, 12, 0)),
    
    Row(a=4, b=5., c='GFG3', d=date(2000, 5, 3),
        e=datetime(2000, 5, 3, 12, 0))
])
  
# show table
df.show()
  
# show schema
df.printSchema()
