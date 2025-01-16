#Programme pour afficher le nombre de tempete par mois au cours de l'année 2024

import os
import pandas as pd
import matplotlib.pyplot as plt

# Chemin du dossier contenant les fichiers CSV
dossier = "donnees_climat_2024"  # Remplace par le chemin exact

# Initialiser un DataFrame vide pour combiner les données
df_combine = pd.DataFrame()

# Lire tous les fichiers CSV du dossier
for fichier in os.listdir(dossier):
    if fichier.endswith('.csv'):
        chemin_fichier = os.path.join(dossier, fichier)
        df_temp = pd.read_csv(chemin_fichier, sep=';', encoding='utf-8')  # Assurez-vous du séparateur
        df_combine = pd.concat([df_combine, df_temp], ignore_index=True)

# Vérifiez les colonnes disponibles
print("Colonnes disponibles :", df_combine.columns)

# Nettoyer les colonnes (supprimer les espaces en trop)
df_combine.columns = df_combine.columns.str.strip()

# Définir les critères pour détecter une tempête
if 'RR' in df_combine.columns and 'FXIAB' in df_combine.columns and 'PMERMINAB' in df_combine.columns:
    tempetes = df_combine[
        (df_combine['RR'] > 100) |
        (df_combine['FXIAB'] > 100) |
        (df_combine['PMERMINAB'] < 980)
    ]

    # Extraire les dates et grouper par mois
    tempetes['Date'] = pd.to_datetime(tempetes['AAAAMM'], format='%Y%m')  # Adapter au format des dates
    tempetes['Mois'] = tempetes['Date'].dt.month
    tempetes_par_mois = tempetes.groupby('Mois').size()

    # Visualisation des résultats
    plt.figure(figsize=(10, 6))
    tempetes_par_mois.plot(kind='bar', color='skyblue')
    plt.title('Nombre de tempêtes par mois en 2024')
    plt.xlabel('Mois')
    plt.ylabel('Nombre de tempêtes')
    plt.xticks(range(12), ['Jan', 'Fév', 'Mar', 'Avr', 'Mai', 'Juin', 'Juil', 'Août', 'Sep', 'Oct', 'Nov', 'Déc'])
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

    # Identifier la période la plus sujette aux tempêtes
    periode_max = tempetes_par_mois.idxmax()
    print(f"La période la plus sujette aux tempêtes est : {periode_max}")
else:
    print("Les colonnes nécessaires ('RR', 'FXIAB', 'PMERMINAB') ne sont pas dans les données.")
