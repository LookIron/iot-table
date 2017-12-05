#!/usr/bin/env python
 #-*- coding: utf-8 -*-

import RPi.GPIO as GPIO
from gtts import gTTS
import time
import os
import sys

import trivia
import top

GPIO.setmode(GPIO.BCM)

reload(sys)
sys.setdefaultencoding('utf8')

def run():
    #GPIO.setmode(GPIO.BOARD)

    # pin 25= Juego trivia
    # pin 24 = juego Top
    
    padPin = 25
    GPIO.setup(padPin, GPIO.IN)
    print "welcome to controller"
    padPin2 = 24
    GPIO.setup(padPin2, GPIO.IN)

    ##redes="Si deseas escuchar tu música escanea el código QR"
    opciones="Tenemos dos juegos para ti, selecciona el boton de interrogación para Trivias, y el martillo para wack a mole"

    
    ocupada=0

    ##Parte para la música
    ##tts = gTTS(text=redes, lang='es')
    ##tts.save("redes.mp3")
    ##os.system('mplayer '+ "redes.mp3")


    ##Seleccioón del juego
    tts = gTTS(text=opciones, lang='es')
    tts.save("opciones.mp3")
    os.system('mplayer '+ "opciones.mp3")

     
    while True:
        
        padPressed =  GPIO.input(padPin)
        padPressed2 =  GPIO.input(padPin2)
     
        if padPressed:
            print "Trivia"
            trivia.run()
            #os.system ("/usr/bin/python /home/pi/Desktop/program/trivia.py")
            #os.system("clear")
            GPIO.cleanup()
         
        if padPressed2:
            print "Top"
            top.run()
            #os.system ("/usr/bin/python /home/pi/Desktop/program/top.py")
            #os.system("clear")
            GPIO.cleanup()

