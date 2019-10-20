#importation des librairies utiles
import json
import pprint

#Ouverture du fichier json avec le bon encodage pour lire les accents
json_data=open('Current_weather.json', encoding = "ISO-8859-1")
#Lecture des données du fichier json
response = json.load(json_data)
#Fermeture du fichier json
json_data.close()

#Affichage brut mais structuré des données
??

#Extraction de l'information de description
??

#Affichage de la description
??
