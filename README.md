# EPISEN_TP1_SPARK

Ce projet est un TP pratique pour découvrir Apache Spark et comprendre ses avantages par rapport à l'utilisation de Python pour le traitement de données volumineuses. Le projet inclut des exemples pour exécuter des requêtes SQL sur des fichiers CSV, démontrer les bénéfices du partitionnement, et comparer les formats de fichiers CSV et Parquet.

## Objectifs du TP

1. Comprendre les avantages de Spark par rapport à Python pour le traitement de grandes quantités de données.
2. Exécuter des requêtes SQL avec Spark sur plusieurs fichiers CSV.
3. Découvrir les bénéfices du partitionnement pour l'optimisation des performances.
4. Comparer les formats de stockage CSV et Parquet.

## Pré-requis

- **Python 3.8+**
- **pip** (pour gérer les dépendances Python)
- **Apache Spark** installé via `pyspark` (sera installé automatiquement via `requirements.txt`)

## Étapes d'initialisation du projet

### 1. Cloner le dépôt

Commencez par cloner ce dépôt GitHub sur votre machine locale.

```
git clone <URL_DU_DEPOT>
cd EPISEN_TP1_SPARK
```

### 2. Créer et activer un environnement virtuel

Il est recommandé d’utiliser un environnement virtuel pour gérer les dépendances.

```
python3 -m venv venv
source venv/bin/activate  # Sous Windows, utilisez `venv\Scripts\activate`
```

### 3. Installer les dépendances

Installez les bibliothèques nécessaires à partir du fichier `requirements.txt`.

```
pip install -r requirements.txt
```

### 4. Structure du projet

Voici l'architecture du projet :

```
EPISEN_TP1_SPARK/
├── data/               # Dossier pour stocker les fichiers CSV et Parquet
│   └── sample_data.csv # Fichier de données d'exemple
├── notebooks/          # Dossier pour les notebooks Jupyter (si nécessaire)
├── scripts/            # Dossier contenant les scripts Spark et Python
│   ├── 0_spark_job.py        # Exemple de job Spark basique
│   └── 1_spark_vs_python.py  # Comparaison entre Spark et Pandas
├── venv/               # Environnement virtuel (non inclus dans Git)
├── .gitignore          # Fichier pour ignorer les fichiers et dossiers non suivis par Git
├── README.md           # Guide de projet
└── requirements.txt    # Fichier de dépendances
```

### 5. Exécuter les scripts

Chaque script est conçu pour illustrer un aspect spécifique de Spark. 

- **Script de base : `0_spark_job.py`**
  
  Ce script montre comment lire un fichier CSV avec Spark, appliquer des transformations et sauvegarder les résultats.

  ```
  python scripts/0_spark_job.py
  ```

- **Comparaison Spark vs Pandas : `1_spark_vs_python.py`**
  
  Ce script compare les performances entre Pandas et Spark pour une opération de jointure sur des datasets volumineux.

  ```
  python scripts/1_spark_vs_python.py
  ```

### 6. Résultats attendus

Pour chaque script, vous devriez voir des temps d'exécution qui varient selon la taille des données traitées et la technologie utilisée. En général :
  
- **Pandas** sera plus rapide pour de petites données en mémoire.
- **Spark** sera bien plus performant pour de grands ensembles de données grâce au traitement distribué.

### 7. Désactiver l'environnement virtuel

Une fois le travail terminé, vous pouvez désactiver l’environnement virtuel avec la commande :

```
deactivate
```

## Ressources supplémentaires

- [Documentation de PySpark](https://spark.apache.org/docs/latest/api/python/)
- [Tutoriel Pandas](https://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html)
