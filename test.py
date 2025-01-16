import os
import requests
import pandas as pd

# URL de base pour les données climatologiques de 2024
BASE_URL = "https://object.files.data.gouv.fr/meteofrance/data/synchro_ftp/BASE/MENS"

# Liste des départements français métropolitains (1 à 95)
DEPARTEMENTS = [f"{i:02}" for i in range(1, 96)]

# Dossier de destination pour les fichiers téléchargés
OUTPUT_DIR = "donnees_climat_2024"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def get_urls():
    """Récupère les URLs des fichiers disponibles pour chaque département."""
    urls = []
    for dep in DEPARTEMENTS:
        url = f"{BASE_URL}/MENSQ_{dep}_latest-2024-2025.csv.gz"
        urls.append(url)
    return urls

def download_data_for_department(url, department):
    """Télécharge les données pour un département donné via une URL."""
    output_path = os.path.join(OUTPUT_DIR, f"climat_2024_dep_{department}.csv.gz")

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

# Récupérer toutes les URLs
urls = get_urls()

# Télécharger les données pour chaque département
for dep, url in zip(DEPARTEMENTS, urls):
    download_data_for_department(url, dep)

print("Téléchargement terminé.")

