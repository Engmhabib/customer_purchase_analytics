from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

raw_df = spark.read.format("json").load("abfss://container@storageaccount.dfs.core.windows.net/raw/customer_transactions/")

raw_df.write.mode('overwrite').format('delta').saveAsTable('raw_transactions')
