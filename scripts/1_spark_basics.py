from pyspark.sql import SparkSession
from pyspark.sql.functions import lit, col, when, sum, variance

# Initialiser une session Spark. Cela crée une interface à un cluster Spark.
spark = SparkSession.builder \
    .master("local[*]") \
    .appName("PySpark_Local") \
    .getOrCreate()


# Configurer le niveau de journalisation de Spark
spark.sparkContext.setLogLevel("ERROR")  # Remplacez "ERROR" par "WARN" ou "INFO" selon votre préférence

# Désactiver les logs de Spark
import os
os.environ['PYSPARK_LOG'] = 'OFF'


path = "/Users/SIMON/episen_tp1_spark/data/1_spark_basics_output"

# Créer un DataFrame simple
data = [("James", "Smith", "USA", 1, 200), 
        ("Michael", "Rose", "FR", 2, 4000), 
        ("Robert", "Williams", "FR", 3, 50), 
        ("Maria", "Jones", "USA", 4, 200)]

columns = ["Prénom", "Nom", "Pays", "ID", "value"]

df = spark.createDataFrame(data).toDF(*columns)

df2 = df.withColumnRenamed("Prénom", "Prenom")
df3 = df2.withColumn("Date", lit("NULL"))
print("df3 :")
df3.show()

df4 = df3.withColumn("Date", when(col("Date")=="NULL", "01-01-1970"))
print("df4 :")
df4.show()

print("exemple of select : ")
df4.where(col("ID")=="4").show()

df4.write.partitionBy("Pays").mode("overwrite").format("parquet").save(path)
print("saved !")

print("example of groupby : ")
df4.groupBy("value").count().show()

print("show : ")
#spark.read.parquet(path).where() # à changer

df.createOrReplaceTempView("personnes")
result = spark.sql("SELECT * FROM personnes WHERE ID = 4")


result.show()