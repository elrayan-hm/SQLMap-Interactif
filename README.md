# SQLMap-Interactif
Ce script Python permet d'interagir avec SQLMap pour automatiser la détection et l'exploitation des failles SQLi sur un site Web cible. Il facilite la récupération des bases de données, des tables et des colonnes, ainsi que l'exfiltration des données.

🚀 Fonctionnalités
📌 Détection des bases de données vulnérables
📌 Récupération des tables d'une base spécifique
📌 Extraction des colonnes d'une table
📌 Dump des données d'une table

📌 Prérequis
Avant d'exécuter ce script, assure-toi d'avoir :
Python 3 installé
SQLMap installé

📥 Installation de SQLMap
Si SQLMap n'est pas encore installé, exécute ces commandes :
# Cloner SQLMap
`git clone --depth 1 https://github.com/sqlmapproject/sqlmap.git`

# Vérifier que SQLMap fonctionne
`python sqlmap/sqlmap.py --version`

📂 Installation du script
Clone ce projet dans ton système :
`git clone https://github.com/ton-utilisateur/sqlmap-interactif.git`
`cd sqlmap-interactif`

🔥 Utilisation
Lance le script en exécutant :
`python SQLX1.py` to check SQLi vulnerability and check available databases and their columns
`python SQLX2.py` to dump data

Ensuite, entre l'URL cible lorsque demandé.
📌 Menu interactif
Le script affichera un menu permettant d'effectuer différentes actions :
1️⃣ Lister les bases de données disponibles
2️⃣ Lister les tables d'une base spécifique
![zz](https://github.com/user-attachments/assets/144c41fe-e371-451b-bb68-34a34ba6bfd2)

3️⃣ Lister les colonnes d'une table (à implémenter)
4️⃣ Dumper les données d'une table (à implémenter)
5️⃣ Quitter

⚠️ Avertissement
Ce script est à des fins éducatives uniquement ! ⚠️ Ne l'utilise que sur des sites Web dont tu as l'autorisation. Toute utilisation illégale est sous ta responsabilité.
