# importation des librairies utiles
import requests
import pprint

# Récupération des prévisions météo des prochains jours via OpenWeatherMap
clef_API_OWP = "--------------------------------"
url = "https://api.openweathermap.org/data/2.5/onecall?lat=??????????&lon=??????????&lang=fr&units=metric&appid="+clef_API_OWP
reponse = requests.request("GET", url)

# Décodage des données météo du jour au format JSON
previsions_json = reponse.json()
# Affichage brut mais structuré des données
pprint.pprint(previsions_json)


    
