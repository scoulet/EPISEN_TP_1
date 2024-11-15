import pandas as pd
import time
from pyspark.sql import SparkSession

# Créer une session Spark
spark = SparkSession.builder.appName("Performance Comparison").getOrCreate()

# Générer un grand DataFrame en Pandas
df_large = pd.DataFrame({
    'Value': range(1, 10000000)
})

# Calculer la somme en utilisant Pandas
start_time = time.time()
sum_pandas = df_large['Value'].sum()
print("Somme avec Pandas:", sum_pandas)
print("Temps avec Pandas:", time.time() - start_time, "secondes")

# Charger les données en Spark et calculer la somme
df_spark = spark.createDataFrame(df_large)
start_time = time.time()
sum_spark = df_spark.groupBy().sum("Value").collect()[0][0]
print("Somme avec Spark:", sum_spark)
print("Temps avec Spark:", time.time() - start_time, "secondes")

# Arrêter la session Spark
spark.stop()