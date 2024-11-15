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
    df_filtered.write.csv("data/output.csv", header=True)

    # Stopper la session Spark
    spark.stop()

if __name__ == "__main__":
    main()
