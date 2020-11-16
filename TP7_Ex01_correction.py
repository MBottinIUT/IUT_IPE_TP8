# importation des librairies utiles
import requests
import pprint

# Etat des stations de vélos en libre service en temps réel
URL = "https://data.explore.star.fr/explore/dataset/vls-stations-etat-tr/download/?format=json&timezone=Europe/Berlin"
# Récupération du fichier JSON depuis l'URL fournie
fichier_velos = requests.get(URL)

# Teste si l'on a bien reçu le fichier ou s'il existe (code 404 sinon)
if fichier_velos.status_code == 200 :
    print ("Fichier bien reçu")
    etat_velos = fichier_velos.json()
    # Parcours le fichier pour afficher tous les noms des stations
    print("LISTE DES STATIONS DISPONIBLES :")
    print("--------------------------------")
    print(" ")
    # Affichage le nombre de vélos dispo pour chaque station
    try :
        for station in etat_velos :
            # Affichage des informations
            print(" ")
            print ("Station {} :".format(station["fields"]["nom"]))
            print("Vélos en libre service potentiels : {}".format(station["fields"]["nombreemplacementsactuels"]))
            print("Vélos en libre service disponibles : {}".format(station["fields"]["nombrevelosdisponibles"]))
            # Récupération de l'horaire de MAJ et mise en forme avant affichage
            heure_MAJ = station["fields"]["lastupdate"]
            heure_MAJ = heure_MAJ.replace("T", " - ")
            index = heure_MAJ.index("+")
            heure_MAJ = heure_MAJ[:index]
            print("Dernière mise à jour : {}".format(heure_MAJ))
    except :
        print ("données non disponibles")
        pass    
else :
    print ("Fichier non disponible")




