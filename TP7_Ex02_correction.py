# importation des librairies utiles
import requests
#import json
import pprint

# Etat des stations de vélos en libre service en temps réel
URL = "https://data.explore.star.fr/explore/dataset/vls-stations-etat-tr/download/?format=json&timezone=Europe/Berlin"
# Récupération du fichier JSON depuis l'URL fournie
fichier_velos = requests.get(URL)

# Teste si l'on a bien reçu le fichier ou s'il existe (code 404 sinon)
if fichier_velos.status_code == 200 :
    print ("Fichier bien reçu")
    #etat_velos = json.loads(fichier_velos.text)
    etat_velos = fichier_velos.json()
    #pprint.pprint(etat_velos)
    # Parcours le fichier pour afficher tous les noms des stations
    print("LISTE DES STATIONS DISPONIBLES :")
    print("--------------------------------")
    for station in etat_velos :
        print (station["fields"]["nom"])
    # Demande à l'utilisateur le nom de sa station
    print(" ")
    user_station = input("Quelle station de vélos vous intéresse ? : ")
    print(" ")
    # Recherche le nombre de vélos dispo pour cette station
    for station in etat_velos :
        # Teste si le champ "fields" contient le nom de la station recherchée
        if station["fields"]["nom"] == user_station :
            # Affichage des informations
            print ("Station {} :".format(user_station))
            print("Vélos en libre service potentiels : {}".format(station["fields"]["nombreemplacementsactuels"]))
            print("Vélos en libre service disponibles : {}".format(station["fields"]["nombrevelosdisponibles"]))
            # Récupération de l'horaire de MAJ et mise en forme avant affichage
            heure_MAJ = station["fields"]["lastupdate"]
            #print(heure_MAJ)
            heure_MAJ = heure_MAJ.replace("T", " - ")
            index = heure_MAJ.index("+")
            heure_MAJ = heure_MAJ[:index]
            print("Dernière mise à jour : {}".format(heure_MAJ))
else :
    print ("Fichier non disponible")




