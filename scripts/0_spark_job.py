from pyspark.sql import SparkSession

def main():
    # Initialiser une session Spark
    spark = SparkSession.builder.appName("Data Processing Job").getOrCreate()
    
    # Exemple de lecture d'un fichier CSV
    df = spark.read.csv("data/sample_data.csv", header=True, inferSchema=True)
    
    # Traitement simple : Afficher le schéma et les 5 premières lignes
    df.printSchema()
    df.show(5)
    
    # Exemple de transformation : Filtrer les valeurs non nulles
    df_filtered = df.na.drop()
    df_filtered.show(5)

    # Sauvegarder les résultats
    df_filtered.write.mode("overwrite").parquet("data/0_spark_job_output/convert_to_parquet")

    # Exemple de sql
    print("exemple de query passée sur du csv : ")
    df_filtered.createOrReplaceTempView("sql_df")
    df_result = spark.sql("SELECT * FROM sql_df WHERE salary > 50000")
    df_result.show()
    df_result.write.mode("overwrite").csv("data/0_spark_job_output/sql_result", header = True)
    

    # Stopper la session Spark
    spark.stop()

if __name__ == "__main__":
    main()
