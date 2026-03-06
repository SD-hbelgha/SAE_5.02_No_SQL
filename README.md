# 📊 SAÉ 5.02 : Migration NoSQL - Analyse des Crimes et Délits (2012-2021)

Ce repository contient l'ensemble des travaux réalisés dans le cadre de la **SAÉ 5.02 : Migration d'une Base de Données Relationnelle vers un Modèle Graphe**. 

---

## 👥 Équipe
- **Hicham Belghachem**
- **Aël Bourasset**
- **Titouan Hibon**

🎥 **[Voir la vidéo de démonstration du projet sur YouTube](https://youtu.be/8ODOPMT4wlo?si=IXIA29tEx1ImswW7)**

---

## 🎯 Objectifs du Projet
1. **Nettoyer et modéliser** un jeu de données brut complexe (fichiers Excel multiples) recensant les délits de la Police et de la Gendarmerie de 2012 à 2021.
2. **Enrichir les données** avec des statistiques démographiques de l'INSEE pour obtenir des analyses per capita (taux pour 1000 habitants).
3. **Créer une base relationnelle (SQLite)** et en démontrer les limites pour l'analyse de réseaux complexes.
4. **Migrer vers Neo4j (NoSQL Graphe)** pour explorer les données de manière plus intuitive et performante via des requêtes Cypher.
5. **Produire des analyses métiers** (Top des infractions, zones sous tension, etc.).

---

## 📂 Architecture du Dépôt

Le projet suit une logique **ETL (Extract, Transform, Load)** complète :

### 1. Données Brutes & Nettoyage (`Jeu_crimes/` & `Jeu_enrichissement/`)
* `crimes-et-delits...xlsx` : Le jeu de données brut fourni par le Ministère.
* `population_departements_ORIGINE.xlsx` : Jeu de données de l'INSEE pour l'enrichissement démographique.
* `Script_traitement_XLSX.py` : Script Python utilisant Pandas pour "aplatir" et nettoyer l'Excel complexe des crimes.
* `Script_traitement_population.py` : Script Python pour formater les données de population.

### 2. Modèle Relationnel (SQL)
* `MCD.jpg` : Modèle Conceptuel des Données détaillant la structure SQL.
* `Requetes_creation_tables.sql` : Script DDL pour la création des tables.
* `BDD_SQL.db` : Base de données SQLite générée, contenant l'ensemble des données nettoyées prêtes à être migrées.

### 3. Migration Graphe (Neo4j)
* `Noeuds&Relations.png` : Schéma de la nouvelle architecture orientée graphe.
* `Script_SQLITE_TO_NEO4J.ipynb` : **Cœur de la migration**. Notebook Jupyter qui se connecte à SQLite, extrait les données en CSV dimensionnels, et génère les requêtes `LOAD CSV` et `MERGE` en langage Cypher pour peupler Neo4j.

### 4. Analyses et Livrables
* `Analyses_NEO4J.pdf` : Recueil des requêtes Cypher et de leurs résultats (Top 10 des crimes, départements les plus touchés, calcul du taux de criminalité pour 1000 habitants).
* `Presentation_Rapport.pdf` : Rapport final expliquant la démarche, les choix techniques, la comparaison SQL vs NoSQL et les recommandations métiers.

---

## 🛠️ Comment reproduire le projet ?

### Prérequis
* Python avec `pandas` et `sqlite3`
* DB Browser for SQLite (ou équivalent)
* Neo4j Desktop (Testé sur la version 1.5.9 / neo4j 4.x/5.x)
* Jupyter Notebook

### Étapes
1. **Préparation des données** : Exécutez les deux scripts Python dans `Jeu_crimes` et `Jeu_enrichissement` pour générer les CSV normalisés.
2. **Base Relationnelle** : Exécutez `Requetes_creation_tables.sql` dans votre SGBD SQLite, puis importez les CSV générés dans les tables correspondantes pour obtenir `BDD_SQL.db`.
3. **Migration** : Ouvrez `Script_SQLITE_TO_NEO4J.ipynb`. Ce script va lire `BDD_SQL.db`, générer des CSV adaptés pour Neo4j dans un dossier d'export.
4. **Import Neo4j** : Placez les CSV générés par le Notebook dans le dossier `import` de votre SGBD Neo4j et exécutez les requêtes Cypher présentes dans le Notebook ou le rapport pour instancier les Nœuds et Relations.
5. **Exploration** : Référez-vous à `Analyses_NEO4J.pdf` pour lancer des requêtes d'analyse métier sur votre base graphe !

---
