import requests
import pandas as pd

# La liste des départements
lien_departements = "https://collectionapi.metmuseum.org/public/collection/v1/departments"
rq = requests.get(lien_departements)
data_departments = rq.json()
df_departments = pd.DataFrame(data_departments["departments"])
#print(df_departments)

# Extraction des données d'art égyptien
id_art_egypte = 10
lien_objets = f"https://collectionapi.metmuseum.org/public/collection/v1/objects?departmentIds={id_art_egypte}"
req_objets = requests.get(lien_objets)
objets_json = req_objets.json()
df_objets = pd.json_normalize(objets_json, 'objectIDs')

#Pendant le nouvel empire
debut_periode = -1550
fin_periode = -1070

objets = requests.get("https://collectionapi.metmuseum.org/public/collection/v1/search?departmentId=10&dateBegin=-1500&dateEnd=-1050&q=%22%22")
objets_id = objets.json()

res = []

for id in objets_id["objectIDs"]:
    res = res + [requests.get("https://collectionapi.metmuseum.org/public/collection/v1/objects/"+str(id)).json()]

df_objets_choisis= pd.json_normalize(res)
#Choix de travail
colonnes_utiles = ['objectID', 'title', 'period', 'dynasty', 'reign', 
                   'objectDate', 'objectBeginDate', 'objectEndDate', 'medium', 
                   'dimensions', 'classification', 'country','region','city', 'tags']
df_objets_choisis = df_objets_choisis[colonnes_utiles]
df_objets_choisis.to_csv('Objets_art_egyptien_nouvel_empire.csv', index=False)
