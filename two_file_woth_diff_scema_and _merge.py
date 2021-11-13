from pyspark.sql import *
from pyspark.sql import functions as F
from pyspark.sql.types import *
spark = SparkSession.builder.master("local").appName("testing").getOrCreate()
sc = spark.sparkContext
