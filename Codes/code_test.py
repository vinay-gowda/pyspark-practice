from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("MyFirstPySparkApp")
    .master("local[*]")
    .getOrCreate()
)

data = [
    ("Alice", 25),
    ("Bob", 30),
    ("Charlie", 28)
]

df = spark.createDataFrame(data, ["Name", "Age"])

print("My first PySpark DataFrame:")
df.show()

print("Spark version:", spark.version)

spark.stop()
