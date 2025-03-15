jdbc_url = "jdbc:sqlserver://your_sql_server.database.windows.net:1433;database=customerDB"
jdbc_table = "dbo.customer_transactions"
jdbc_properties = {
    "user": "sql_admin",
    "password": "your_password",
    "driver": "com.microsoft.sqlserver.jdbc.SQLServerDriver"
}
from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate()
df = spark.read.table('processed_transactions')
df.write.format("jdbc").mode("overwrite").option("url", jdbc_url).option("dbtable", jdbc_table).options(**jdbc_properties).save()
