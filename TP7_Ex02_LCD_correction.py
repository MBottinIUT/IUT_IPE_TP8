# importation des librairies utiles
import requests
#import json
import pprint
# Importation des librairies propres aux images
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# Importation des libraries pour la gestion de l'écran
from lib_tft24T import TFT24T
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
import spidev

# Déclaration des numéros de broches utiles pour la gestion de l'écran
DC = 22
RST = 25
LED = 23

# Instanciation de l'objet LCD
TFT = TFT24T(spidev.SpiDev(), GPIO)

# Initialisation de l'écran
TFT.initLCD(DC, RST, LED)

# Création d'un buffer représentant la zone d'affichage de l'écran
zone_ecran = TFT.draw()

# Remplissage de l'écran en blanc
TFT.clear((255,255,255))

# Etat des stations de vélos en libre service en temps réel
URL = "https://data.explore.star.fr/explore/dataset/vls-stations-etat-tr/download/?format=json&timezone=Europe/Berlin"
# Récupération du fichier JSON depuis l'URL fournie
fichier_velos = requests.get(URL)

# Chargement de la police utilisée
police1 = ImageFont.truetype('Polices/Letters_for_Learners.ttf',36)
police2 = ImageFont.truetype('Polices/Letters_for_Learners.ttf',24)
police3 = ImageFont.truetype('Polices/Letters_for_Learners.ttf',16)

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
            nb_velos = "{} vélos".format(station["fields"]["nombrevelosdisponibles"])
            # Récupération de l'horaire de MAJ et mise en forme avant affichage
            heure_MAJ = station["fields"]["lastupdate"]
            #print(heure_MAJ)
            heure_MAJ = heure_MAJ.replace("T", " - ")
            index = heure_MAJ.index("+")
            heure_MAJ = heure_MAJ[:index]
            print("Dernière mise à jour : {}".format(heure_MAJ))
    # Affichage sur l'écran LCD
    TFT.clear((255,255,255))
    logo = Image.open('images/Logo_STAR_Rennes.jpg')
    logo = logo.rotate(-90, expand = True)
    logo.save('images/Logo_STAR_Rennes_90.jpg')
    zone_ecran.pasteimage('images/Logo_STAR_Rennes_90.jpg', (0,0))
    icone = Image.open('images/Velo_Rennes.jpg')
    icone = icone.rotate(-90, expand = True)
    icone.save('images/Velo_Rennes_90.jpg')
    zone_ecran.pasteimage('images/Velo_Rennes_90.jpg', (160,210))
    zone_ecran.textrotated((125,190), user_station, 270, font=police2, fill=(0,0,0))
    zone_ecran.textrotated((70,190), nb_velos, 270, font=police1, fill=(0,0,0))
    zone_ecran.textrotated((20,190), heure_MAJ, 270, font=police3, fill=(0,0,0))
    TFT.display()
else :
    print ("Fichier non disponible")




