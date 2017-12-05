##https://pypi.python.org/pypi/deezer-python/
##https://pypi.python.org/pypi/python-firebase/1.2
import random
import pygame
import requests
from firebase import firebase
import urllib2
from datetime import datetime
from datetime import timedelta
from shutil import copyfile
import time

firebase = firebase.FirebaseApplication('https://mesa-interactiva.firebaseio.com/', None)

pygame.init()

RECORD_SECONDS = 30

def reproductor(archivo):
    pygame.mixer.music.load(archivo)
    pygame.mixer.music.set_volume(0.30)
    pygame.mixer.music.play()
    descargador()


def descargador():
    array = firebase.get('/mesas/0/artistas/', None)
    while array is None:
        array = firebase.get('/mesas/0/artistas/', None)
        print("Esperando por una cancion")
        time.sleep(5)
    randomArtistas = random.randrange(len(array))
    print(randomArtistas)
    artista=firebase.get('/mesas/0/artistas/', randomArtistas.__str__())["artista"]
    artistaJsonData = requests.get('https://api.deezer.com/search?q=' + artista).json()["data"]

    maximoCanciones=len(artistaJsonData)
    if maximoCanciones == 0:
        maximoCanciones = 1
    randomJson = random.randrange(maximoCanciones);

    while len(artistaJsonData) == 0:
        randomArtistas = random.randrange(len(array))
        artista = firebase.get('/mesas/0/artistas/', randomArtistas.__str__())["artista"]
        artistaJsonData = requests.get('https://api.deezer.com/search?q=' + artista).json()["data"]

        maximoCanciones = len(artistaJsonData)
        if maximoCanciones==0:
            maximoCanciones=1
        randomJson = random.randrange(maximoCanciones);
        print("me loopeo " + len(artistaJsonData).__str__())


    URL = artistaJsonData[randomJson]['preview']



    # Open the file stream and write file
    filename = 'python.mp3'
    f = file(filename, 'wb')
    url = urllib2.urlopen(URL)
    # Basically a timer
    t_start = datetime.now()
    t_end = datetime.now()
    t_end_old = t_end
    # Record in chunks until
    print "Recording..."
    while t_end - t_start < timedelta(seconds=RECORD_SECONDS):
        f.write(url.read(1024))
        t_end = datetime.now()
    f.close()

    pygame.mixer.music.stop()
    print("omomomo")
    copyfile('python.mp3', 'temporal.mp3')
    filenameTemporal='temporal.mp3'
    time.sleep(3)
    reproductor(filenameTemporal)


descargador()

