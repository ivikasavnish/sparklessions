from pyspark.sql import SparkSession

# Create my_spark
my_spark = SparkSession.builder.getOrCreate()

# Print my_spark
print(my_spark)
# Print the tables in the catalog
print(spark.catalog.listTables())
