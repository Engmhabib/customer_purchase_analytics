from pyspark.sql.functions import col, sum, avg, countDistinct, to_date
from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate()
raw_df = spark.read.table('raw_transactions')
clean_df = raw_df.dropDuplicates(['transaction_id']).dropna(subset=['customer_id', 'purchase_amount']).withColumn('purchase_date', to_date(col('transaction_timestamp')))
agg_df = clean_df.groupBy('customer_id', 'purchase_date').agg(sum('purchase_amount').alias('total_spend'), avg('purchase_amount').alias('avg_basket_size'), countDistinct('transaction_id').alias('num_transactions'))
agg_df.write.mode('overwrite').format('delta').saveAsTable('processed_transactions')
