
import os
import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd

# Chargement du fichier GeoJSON
carte_departements = gpd.read_file("departements.geojson")

# Chemin du dossier contenant les fichiers CSV
dossier = "donnees_climat_2024"

# Initialiser un DataFrame vide pour combiner les données
df_combine = pd.DataFrame()

# Lire tous les fichiers CSV du dossier
for fichier in os.listdir(dossier):
    if fichier.endswith('.csv'):
        chemin_fichier = os.path.join(dossier, fichier)
        df_temp = pd.read_csv(chemin_fichier, sep=';', encoding='utf-8')
        df_combine = pd.concat([df_combine, df_temp], ignore_index=True)

# Nettoyer les colonnes (supprimer les espaces en trop)
df_combine.columns = df_combine.columns.str.strip()

# Vérifier si les colonnes nécessaires sont présentes
if 'LAT' in df_combine.columns and 'LON' in df_combine.columns:
    # Convertir les données météo en GeoDataFrame
    df_combine['LAT'] = pd.to_numeric(df_combine['LAT'], errors='coerce')
    df_combine['LON'] = pd.to_numeric(df_combine['LON'], errors='coerce')
    gdf_meteo = gpd.GeoDataFrame(
        df_combine,
        geometry=gpd.points_from_xy(df_combine['LON'], df_combine['LAT']),
        crs="EPSG:4326"
    )

    # Associer chaque point météo à un département
    gdf_meteo = gpd.sjoin(gdf_meteo, carte_departements, how="left", predicate="intersects")

    # Vérifier si la colonne du département existe après le joint
    if 'code' in gdf_meteo.columns:  # 'code' peut varier selon le fichier GeoJSON
        gdf_meteo['CodeDepartement'] = gdf_meteo['code']
        
        # Définir les critères pour détecter une tempête
        if 'RR' in gdf_meteo.columns and 'FXIAB' in gdf_meteo.columns and 'PMERMINAB' in gdf_meteo.columns:
            tempetes = gdf_meteo[
                (gdf_meteo['RR'] > 100) |
                (gdf_meteo['FXIAB'] > 100) |
                (gdf_meteo['PMERMINAB'] < 980)
            ]

            # Compter les tempêtes par département
            tempetes_par_departement = tempetes.groupby('CodeDepartement').size()

            # Carte des départements colorée selon le nombre de tempêtes
            carte_departements = carte_departements.merge(
                tempetes_par_departement.rename('NombreTempetes'),
                left_on='code',
                right_index=True,
                how='left'
            ).fillna(0)

            plt.figure(figsize=(12, 10))
            carte_departements.plot(
                column='NombreTempetes',
                cmap='OrRd',
                legend=True,
                legend_kwds={'label': "Nombre de tempêtes"},
                edgecolor='black'
            )
            plt.title("Nombre de tempêtes par département en 2024")
            plt.axis('off')
            plt.show()
        else:
            print("Les colonnes nécessaires ('RR', 'FXIAB', 'PMERMINAB') ne sont pas dans les données.")
    else:
        print("Impossible d'associer les stations météo aux départements.")
else:
    print("Les colonnes 'LAT' et 'LON' sont manquantes dans les données météo.")
