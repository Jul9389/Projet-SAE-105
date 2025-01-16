Pour notre projet, nous avons choisi celui sur les tempêtes en France métropolitaines, étant donné qu’il n’y avait pas de données nommées « tempête », nous avons donc pris en compte celles qui s’apparenteraient aux tempêtes.

1ère étape : Etablir ce que l’on considèrera comme tempête

. Indicateurs d'Intensité des Phénomènes
•	Pluviométrie (RR, RRAB) : Si les précipitations journalières (ou mensuelles) sont exceptionnellement élevées, cela peut indiquer des tempêtes. Par exemple, un cumul de pluie (RR) ou une valeur record de pluie (RRAB) dépassant les moyennes saisonnières.
•	Vents forts (FXIAB, FXYAB) : Les vitesses maximales de rafales (instantanées ou moyennes) enregistrées dans une tempête sont généralement significatives. Une vitesse élevée dans ces colonnes peut être un bon indicateur.
2. Evénements Extrêmes
•	Pression atmosphérique basse (PMERMINAB) : Une forte chute de pression au niveau de la mer est souvent associée à des tempêtes.
•	Amplitude thermique (TAMPLI) : Une grande amplitude thermique peut accompagner certains événements météorologiques intenses.
3. Valeurs Seuils
On peut identifier les tempêtes en filtrant les lignes où les valeurs dépassent certains seuils :
•	Pluie : RR > 100 mm en une journée ou RRAB très élevé.
•	Vent : FXIAB > 100 km/h.
•	Pression : PMERMINAB < 980 hPa.

4. Enregistrement des Dates
Les colonnes "DAT" (comme RRABDAT, PMERMINABDAT, FXIABDAT) donnent les dates exactes des records pour ces phénomènes. Elles permettent de localiser les jours où des tempêtes ont pu survenir.


2ème étape : Télécharger les fichiers csv des données climatologique de tous les départements de France Métropolitaine
Après avoir établi ces critères pour distinguer les possibles tempêtes dans les différents fichiers csv, nous utiliserons donc un programme qui permettra de télécharger l’ensemble des fichiers csv sur les données climatologiques de 2024 de tous les départements, pour éviter de devoir les télécharger un à un les 96 fichiers compressés que nous avons effectué l’extraction manuellement (sélectionner l’ensemble des fichiers et faire « extraire ici »)
Ce programme nous l’avons utilisé qu’une seule fois pour les télécharger, les fichiers sont tous dans un même dossier où le 2nd programme pourra les utiliser par la suite.

3ème étape : Problématique : Quelle période est plus sujette à l’apparition d’une tempête selon les données climatologique recueillis en 2024.
