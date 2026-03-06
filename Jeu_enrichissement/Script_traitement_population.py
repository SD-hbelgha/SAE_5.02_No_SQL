import pandas as pd
import re

chemin_fichier = "c:/SAE_NO_SQL/BDD_POPULATION/POPULATION.xlsx"
all_data = []

feuilles = pd.read_excel(chemin_fichier, sheet_name=None, skiprows=4)

for nom_feuille, df in feuilles.items():
    
    # recup de l'année direct dans le nom de l'onglet
    annee = int(re.search(r'\d{4}', nom_feuille).group())
    
    # renommage des colonnes utiles
    df = df.rename(columns={
        'Unnamed: 0': 'Code département', 
        'Total': 'Population totale'
    })
    
    # nettoyage basique des lignes
    df = df[df['Code département'].notna()].copy()
    df['Code département'] = df['Code département'].astype(str).str.strip()
    df = df[~df['Code département'].str.startswith('Source')]
    
    # on vire les lignes de totaux globaux (la france entière, etc.)
    exclusions = ['France métropolitaine', 'DOM', 'France métropolitaine et DOM']
    df = df[~df['Code département'].isin(exclusions)]
    
    df['Année'] = annee
    
    # passage en entier pour virer les ".0"
    df['Population totale'] = df['Population totale'].astype('Int64')
    
    # on garde que ce dont on a besoin
    df_final = df[['Code département', 'Année', 'Population totale']]
    all_data.append(df_final)

# assemblage final et tri
df_result = pd.concat(all_data, ignore_index=True)
df_result = df_result.sort_values(by=['Année', 'Code département']).reset_index(drop=True)

# export en csv (sep=';' pour être tranquille avec excel)
df_result.to_csv('population_departements.csv', index=False, sep=';')
print("Fichier population_departements.csv fait")