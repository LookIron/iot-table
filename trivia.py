#!/usr/bin/env python
 #-*- coding: utf-8 -*-
from gtts import gTTS
import RPi.GPIO as GPIO
import os
import random
import sys
import time
import pygame
import Adafruit_MPR121.MPR121 as MPR121



#as3:/usr/local/lib/python2.7/site-packages
# cat sitecustomize.py
# encoding=utf8  
 

#Setup
reload(sys)  
sys.setdefaultencoding('utf8')
GPIO.setmode(GPIO.BCM)
GPIO.setup(25,GPIO.IN)

#Callbacks
def volverController(channel):
    # /home/pi/Downloads/Trivia/controller.py    
    print "VOLVER A CONTROLLER"

    

#Interrupciones
GPIO.add_event_detect(25, GPIO.RISING, callback = volverController)


seleccionTema = ""
respuestaCorrecta = "¡Tu respuesta es correcta!"
respuestaIncorrecta = "¡Tu respuesta es incorrecta!"
categoriasSelect= "Selecione la categoría a continuación"
respuestaSelect="Selecione una de las opciones entre a y d"
##intInicio =""
##intFinal=""
jugador1=1
jugador2=2
jugador3=3
turnoJugador1="El turno es del jugador 1"
turnoJugador2="El turno es del jugador 2"
turnoJugador3="El turno es del jugador 3"

##############################################################################
# Create MPR121 instance.
cap = MPR121.MPR121()

if not cap.begin():
    print 'Error initializing MPR121.  Check your wiring!'
    sys.exit(1)
cap._i2c_retry(cap._device.write8,0x5E,0x00)
cap.set_thresholds(1,2)
cap._i2c_retry(cap._device.write8,0x5E,0x8F)

print('Press Ctrl-C to quit.')
last_touched = cap.touched()


def funcionRespuesta(opcion):
    
        res=""
        if opcion==0:
                res="a"
        elif opcion==1:
                res="b"
        elif opcion==2:
                res="c"
        elif opcion==3:
                res="d"

        return res

def funcionRespuestaJugadorDos(opcion):
        res=""
        if opcion==4:
                res="a"
        elif opcion==5:
                res="b"
        elif opcion==6:
                res="c"
        elif opcion==7:
                res="d"

        return res

def funcionRespuestaJugadorTres(opcion):
        res=""
        if opcion==8:
                res="a"
        elif opcion==9:
                res="b"
        elif opcion==10:
                res="c"
        elif opcion==11:
                res="d"

        return res

def funcionSeleccionJugadorUno(opcion):
       
                
        res=""
        if opcion==0:
                res="1"
        elif opcion==1:
                res="2"
                
        elif opcion==2:
                res="3"
        elif opcion==3:
                res="4"

        return res


def funcionSeleccionJugadorDos(opcion):
        
                
        res=""
        if opcion==4:
                res="1"
        elif opcion==5:
                res="2"
                
        elif opcion==6:
                res="3"
        elif opcion==7:
                res="4"

        return res

def funcionSeleccionJugadorTres(opcion):
        
                
        res=""
        if opcion==8:
                res="1"
        elif opcion==9:
                res="2"
                
        elif opcion==10:
                res="3"
        elif opcion==11:
                res="4"

        return res
    
def run():
    ##################################################################################
    #abre el directorio files
    os.chdir('./files')
    #carga el archivo texto inicial en la variable fichero
    fichero = open('texto.txt', 'r')
    #while True:
     #Recorremos las opciones para que el usuario seleciones


    cont=1

    while True:

            if cont==jugador1:
                    tts = gTTS(text=turnoJugador1, lang='es')
                    tts.save("turnoJugador1.mp3")
                    os.system('mplayer '+ "turnoJugador1.mp3")
            if cont==jugador2:
                    tts = gTTS(text=turnoJugador2, lang='es')
                    tts.save("turnoJugador2.mp3")
                    os.system('mplayer '+ "turnoJugador2.mp3")
            if cont==jugador3:
                    tts = gTTS(text=turnoJugador3, lang='es')
                    tts.save("turnoJugador3.mp3")
                    os.system('mplayer '+ "turnoJugador3.mp3")
            
            tts = gTTS(text=categoriasSelect, lang='es')
            tts.save("categoriasSelect.mp3")
            os.system('mplayer '+ "categoriasSelect.mp3")
            
            for s in fichero.readlines():
                    print(s)
                    tts = gTTS(text=s, lang='es')
                    tts.save("cateforias.mp3")
                    os.system('mplayer '+ "cateforias.mp3")
            
            tts = gTTS(text=seleccionTema, lang='es')
            tts.save("seleccionTema.mp3")
            os.system('mplayer '+ "seleccionTema.mp3")

            
##            valo=""
##            valo=0
##            temaPregunta=funcionSeleccionJugadorTres(valo)
##            print temaPregunta + "-----------------------------"
            


            #Recordar cada jugador debe poder escoger su tema
            continuar = 0
            valorZ=""
            while continuar==0:
                    current_touched = cap.touched()
                  
                    if jugador1==cont:
                         
                            for i in range(4):
                                
                                     
                                     # Each pin is represented by a bit in the touched value.  A value of 1
                                     # means the pin is being touched, and 0 means it is not being touched.
                                     pin_bit = 1 << i
                                     # First check if transitioned from not touched to touched.
                                     if current_touched & pin_bit and not last_touched & pin_bit:
                                             valo=0
                                             valo='{0}'.format(i)
                                             valorZ=funcionSeleccionJugadorUno(int(valo))
                                             continuar=1
                            last_touched = current_touched
                            time.sleep(0.1)
            
                    if jugador2==cont:
                            for i in range(4,8):
                                    # Each pin is represented by a bit in the touched value.  A value of 1
                                    # means the pin is being touched, and 0 means it is not being touched.
                                    pin_bit = 1 << i
                                    # First check if transitioned from not touched to touched.
                                    if current_touched & pin_bit and not last_touched & pin_bit:
                                            valo=0
                                            valo='{0}'.format(i)
                                            valorZ=funcionSeleccionJugadorDos(int(valo))
                                            continuar=1
                            last_touched = current_touched
                            time.sleep(0.1)

                    if jugador3==cont:
                                            
                            for i in range(8,12):
                                    # Each pin is represented by a bit in the touched value.  A value of 1
                                    # means the pin is being touched, and 0 means it is not being touched.
                                    pin_bit = 1 << i
                                    # First check if transitioned from not touched to touched.
                                    if current_touched & pin_bit and not last_touched & pin_bit:
                                            valo=0
                                            valo='{0}'.format(i)
                                            valorZ=funcionSeleccionJugadorTres(int(valo))
                                            continuar=1
                                                                    
                            last_touched = current_touched
                            time.sleep(0.1)
                            
         
            
            #temaPregunta = raw_input(seleccionTema)
            
            cadena = valorZ+".txt";
            ficheroSeleccion = open(cadena,'r')
            numero = random.randrange(11)
            
            for linea in ficheroSeleccion:
                    lineaSep = linea.split(' ')
                    #print(lineaSep)	
                    if lineaSep[0] == str(numero):
                            #fichero.tell() me permite saber la linea actual del recorrido
                            p = linea[2:len(linea)]
                            print(p)
                            tts = gTTS(text=p, lang='es')
                            tts.save("pregunta.mp3")
                            os.system('mplayer '+ "pregunta.mp3")
                            a = ficheroSeleccion.next()
                            print(a)
                            tts = gTTS(text=a, lang='es')
                            tts.save("opcion1.mp3")
                            os.system('mplayer '+ "opcion1.mp3")
                            b = ficheroSeleccion.next()
                            print(b)
                            tts = gTTS(text=b, lang='es')
                            tts.save("opcion2.mp3")
                            os.system('mplayer '+ "opcion2.mp3") 
                            c = ficheroSeleccion.next()
                            print(c)
                            tts = gTTS(text=c, lang='es')
                            tts.save("opcion3.mp3")
                            os.system('mplayer '+ "opcion3.mp3") 
                            d = ficheroSeleccion.next()
                            print(d)
                            tts = gTTS(text=d, lang='es')
                            tts.save("opcion4.mp3")
                            os.system('mplayer '+ "opcion4.mp3")
                            answer = ficheroSeleccion.next()
                            #print(answer)
                            #Aqui selecciono las preguntas
                            #tts = gTTS(text=respuestaSelect, lang='es')
                            #tts.save("respuestaSelect.mp3")
                            #os.system('mplayer '+ "respuestaSelect.mp3")

                            
                            #respuesta = raw_input("Respuesta: ")
                            valorR=""
                            continuar = 0
                            while continuar==0:
                                    current_touched = cap.touched()
                                    if jugador1==cont:
                                            for i in range(4):
                                                    # Each pin is represented by a bit in the touched value.  A value of 1
                                                    # means the pin is being touched, and 0 means it is not being touched.
                                                    pin_bit = 1 << i
                                                    # First check if transitioned from not touched to touched.
                                                    if current_touched & pin_bit and not last_touched & pin_bit:
                                                            #print '{0} touched!'.format(i)
                                                            t= '{0}'.format(i)
                                                            valorR = funcionRespuesta(int(t))
                                                            print valorR
                                                            
                                                            continuar=1
                                                           # print temaPregunta
                                            last_touched = current_touched
                                            time.sleep(0.1)
            
                                    if jugador2==cont:
                                            for i in range(4,8):
                                                    # Each pin is represented by a bit in the touched value.  A value of 1
                                                    # means the pin is being touched, and 0 means it is not being touched.
                                                    pin_bit = 1 << i
                                                    # First check if transitioned from not touched to touched.
                                                    if current_touched & pin_bit and not last_touched & pin_bit:
                                                            #print '{0} touched!'.format(i)
                                                            t= '{0}'.format(i)
                                                            valorR = funcionRespuestaJugadorDos(int(t))
                                                            print valorR
                                                            continuar=1
                                                           # print temaPregunta
                                            last_touched = current_touched
                                            time.sleep(0.1)

                                    if jugador3==cont:
                                            
                                            for i in range(8,12):
                                                    # Each pin is represented by a bit in the touched value.  A value of 1
                                                    # means the pin is being touched, and 0 means it is not being touched.
                                                    pin_bit = 1 << i
                                                    # First check if transitioned from not touched to touched.
                                                    if current_touched & pin_bit and not last_touched & pin_bit:
                                                            #print '{0} touched!'.format(i)
                                                            t= '{0}'.format(i)
                                                            valorR = funcionRespuestaJugadorTres(int(t))
                                                            print valorR
                                                            continuar=1
                                                            #print temaPregunta
                                            last_touched = current_touched
                                            time.sleep(0.1)
                            
                            if answer.strip() == valorR.strip():
                                    print (respuestaCorrecta)
                                    tts = gTTS(text=respuestaCorrecta, lang='es')
                                    tts.save("correct.mp3")
                                    os.system('mplayer '+ "correct.mp3")
                            else:
                                    print (respuestaIncorrecta)
                                    tts = gTTS(text=respuestaIncorrecta, lang='es')
                                    tts.save("uncorrect.mp3")
                                    os.system('mplayer '+ "uncorrect.mp3")
            
            if cont==3:
                    cont=0
            cont=cont+1

    fichero.close()
