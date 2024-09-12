import pandas as pd

chemin_fichier = 'C:\\ent\\Objets_art_egyptien_nouvel_empire.csv'
df_objets_choisis = pd.read_csv(chemin_fichier)

# Suppression
df_objets_choisis = df_objets_choisis.dropna(subset=['objectBeginDate', 'objectEndDate'])

# Conversion des colonnes de date
df_objets_choisis['objectBeginDate'] = df_objets_choisis['objectBeginDate'].astype(int)
df_objets_choisis['objectEndDate'] = df_objets_choisis['objectEndDate'].astype(int)

# Conversion 
df_objets_choisis = df_objets_choisis.astype({
    'objectID': 'int',
    'title': 'string',
    'period': 'string',
    'dynasty': 'string',
    'reign': 'string',
    'objectDate': 'string',
    'medium': 'string',
    'dimensions': 'string',
    'classification': 'string',
    'country': 'string',
    'region': 'string',  
    'city': 'string',  
    'tags': 'string'
})

df_objets_choisis.to_csv('C:\\ent\\Objets_art_egyptien_nouvel_empire.csv', index=False)
