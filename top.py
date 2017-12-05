import RPi.GPIO as GPIO
import time
import sys
import time
import os

import Adafruit_MPR121.MPR121 as MPR121
import threading
import random
from random import randrange
from gtts import gTTS

reload(sys)  
sys.setdefaultencoding('utf8')

GPIO.setmode(GPIO.BCM)


#Callbacks
def volverController(channel):
    # /home/pi/Downloads/Trivia/controller.py
    os.system("clear")
    GPIO.cleanup()
    os.system ("/usr/bin/python /home/pi/Desktop/program/controller.py")
    

#Interrupciones
#GPIO.add_event_detect(24, GPIO.RISING, callback = volverController)

#Variables
empieza="tres dos uno a jugar"
ganador="gano el jugador"
empate12="Hay empate entre el jugador 1 y 2"
empate13="Hay empate entre el jugador 1 y 3"
empate23="Hay empate entre el jugador 2 y 3 "
empate3="Hay empate entre todos los jugadores"

#pinesDisponibles =5,6,12,13,16,19,21,20,4,17,18,27 ---22,23

f=[]
puntaje1=0
puntaje2=0
puntaje3=0
pin=[5,6,12,13,16,19,21,20,4,17,18,27]
stop=True;

class MyThread ( threading.Thread ):

##   def __init__(selt):
##       super(MyThread, self).__init__()
##       self._stop_event = threading.Event()
##       
##   def stop (self):
##       self._stop_event.set()
##       
##   def stopped(self):
##       self._stop_event.is_set()
       
   def run ( self ):

    
      cap = MPR121.MPR121()
      if not cap.begin():
        print('Error initializing MPR121.  Check your wiring!')
        sys.exit(1)
      cap._i2c_retry(cap._device.write8,0x5E,0x00)
      cap.set_thresholds(1,2)
      cap._i2c_retry(cap._device.write8,0x5E,0x8F)


      last_touched = cap.touched()
      global puntaje1
      global puntaje2
      global puntaje3
      global f

      #cont =0
      while stop:
         
        current_touched = cap.touched()
   
        
        for i in range(12):
            # Each pin is represented by a bit in the touched value.  A value of 1
            # means the pin is being touched, and 0 means it is not being touched.
            pin_bit = 1 << i
            # First check if transitioned from not touched to touched.
            if current_touched & pin_bit and not last_touched & pin_bit:
                #print('{0} touched!'.format(i))
                if f[i] is True:
                   
                   f[i]=False
                   GPIO.output(pin[i],GPIO.LOW)
                   if i<4:
                      puntaje1+=1
                      print puntaje1
                   elif i<8:
                      puntaje2+=1
                      print puntaje2
                   else:
                      puntaje3+=1
                      print puntaje3
            # Next check if transitioned from touched to not touched.
            #if not current_touched & pin_bit and last_touched & pin_bit:
                #print('{0} released!'.format(i))
        # Update last state and wait a short period before repeating.
        last_touched = current_touched
        time.sleep(0.1)

        #cont+=1
def llenar_f():
    global f
    f=[]
    for i in range(12):
          f.append(bool(random.getrandbits(1)))

def setGPIO_as_output():
    for i in range(12):
       GPIO.setup(pin[i],GPIO.OUT)

def run():
    llenar_f()
    setGPIO_as_output()
    MyThread().start()
    tts = gTTS(text=empieza, lang='es')
    tts.save("empieza.mp3")
    os.system('mplayer '+ "empieza.mp3")
    
    ronda=1
    while ronda<20:
        global f

        llenar_f()
       
        for i in range(12):       
            GPIO.output(pin[i],GPIO.LOW)           
           
        for i in range(12):

            if f[i] is True:
                GPIO.output(pin[i],GPIO.HIGH)
                #print x        
       
        time.sleep(randrange(1,3))
        ronda+=1
    
    
    for i in range(12):
        GPIO.output(pin[i],GPIO.LOW)
    
    print('juego terminado')
    
    global stop
    stop=False    
    #MyThread()._Thread_stop()
    
    if puntaje1>puntaje2 and puntaje1>puntaje3:
       print('ganador jugador 1')
       g1=ganador+" 1"
       tts = gTTS(text=g1, lang='es')
       tts.save("g1.mp3")
       os.system('mplayer '+ "g1.mp3")
    
    elif puntaje2>puntaje3 and puntaje2>puntaje1:
       print('ganador jugador 2')
       g2=ganador+" 2"
       tts = gTTS(text=g2, lang='es')
       tts.save("g2.mp3")
       os.system('mplayer '+ "g2.mp3")
    
    elif puntaje3>puntaje2 and puntaje3>puntaje1:
       print('ganador jugador 3')
       g3=ganador+" 3"
       tts = gTTS(text=g3, lang='es')
       tts.save("g3.mp3")
       os.system('mplayer '+ "g3.mp3")
    
    elif puntaje1==puntaje2 and puntaje1==puntaje3:
       print('empate de los 3')
       tts = gTTS(text=empate3, lang='es')
       tts.save("empate3.mp3")
       os.system('mplayer '+ "empate3.mp3")
    
    elif puntaje1==puntaje2:
       print('empate jugador 1 y 2')
       tts = gTTS(text=empate12, lang='es')
       tts.save("empate12.mp3")
       os.system('mplayer '+ "empate12.mp3")
    
    elif puntaje1==puntaje3:
       print('empate jugador 1 y 3')
       tts = gTTS(text=empate13, lang='es')
       tts.save("empate13.mp3")
       os.system('mplayer '+ "empate13.mp3")
    
    elif puntaje2==puntaje3:
       print('empate jugador 2 y 3')
       tts = gTTS(text=empate23, lang='es')
       tts.save("empate23.mp3")
       os.system('mplayer '+ "empate23.mp3")
    
    
    os.system("clear")
    GPIO.cleanup()
    os.system ("/usr/bin/python /home/pi/Desktop/program/controller.py")
     
