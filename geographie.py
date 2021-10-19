# importation des librairies utiles
import requests
import pprint

# Demander à l'utilisateur un pays
pays = input("Pour quel pays souhaitez-vous des informations ?")

# Récupération des infos via restcountries.eu
url = ?????????????????????????????????????????
reponse = requests.request("GET", url)

# Décodage des données du pays au format JSON
donnees_json = reponse.json()
# Affichage brut mais structuré des données
pprint.pprint(donnees_json)
