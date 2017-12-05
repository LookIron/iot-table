#!/usr/bin/env python
 #-*- coding: utf-8 -*-

#Para que arranque apenas se encienda la rasp
#http://www.kami.es/2016/ejecutar-script-al-inicio-raspberry-pi/

import RPi.GPIO as GPIO
from gtts import gTTS
import time
import os
import sys
from subprocess import Popen, PIPE

try:

    reload(sys)  
    sys.setdefaultencoding('utf8')
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(22, GPIO.IN)



    jugar="Hola a todos, ¡bienvenidos!. Si deseas escuchar tu música escanea el código QR"

          
    seq=0
    while True:
        i=GPIO.input(22)
        if i==0:
            print "No intruders", i
           
            time.sleep(1)
            seq=0
        elif i==1:
            print "intruder detected ", i
            seq+=1
            if seq==5:
                seq=0
                tts = gTTS(text=jugar, lang='es')
                tts.save("jugar.mp3")
                os.system('mplayer '+ "jugar.mp3")

                ##condicion
                musica=Popen(["sudo","python","/home/pi/Desktop/program/musica.py","&"],stdout=PIPE, stderr=PIPE)
                #print musica.communicate()[0]

                os.system ("/usr/bin/python /home/pi/Desktop/program/controller.py")
                os.system("clear")
                GPIO.cleanup()
                 
            
            time.sleep(1)
except KeyboardInterrupt:  
    # here you put any code you want to run before the program   
    # exits when you press CTRL+C  
    print "\n", counter # print value of counter  
  
except:  
    # this catches ALL other exceptions including errors.  
    # You won't get any error messages for debugging  
    # so only use it once your code is working  
    print "Other error or exception occurred!"  
  
finally:  
    GPIO.cleanup() # this ensures a clean exit 

