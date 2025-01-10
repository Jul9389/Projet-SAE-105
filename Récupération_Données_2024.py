import os
import requests

# URL de base pour récupérer les données climatologiques de 2024
BASE_URL = "https://meteo.data.gouv.fr/datasets/6569b3d7d193b4daf2b43edc"

# trie pour n'avoir que les départements de france métropolitaine
DEPARTEMENTS = [f"{i:02}" for i in range(1, 96)]

# Où les fichiers seront enregistrés
OUTPUT_DIR = "donnees_climat_2024"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def download_data_for_department(department):
    """Télécharge les données pour un département donné."""
    url = f"{BASE_URL}/{department}/data.csv"  
    output_path = os.path.join(OUTPUT_DIR, f"climat_2024_dep_{department}.csv")

    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(output_path, "wb") as file:
                file.write(response.content)
            print(f"Données pour le département {department} téléchargées avec succès.")
        else:
            print(f"Erreur {response.status_code} pour le département {department}.")
    except Exception as e:
        print(f"Erreur lors du téléchargement des données pour le département {department}: {e}")

# Boucle sur tous les départements
for dep in DEPARTEMENTS:
    download_data_for_department(dep)

print("Téléchargement terminé.")
