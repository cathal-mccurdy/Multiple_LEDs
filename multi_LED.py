import RPi.GPIO as GPIO
import time
#imports libraies needed

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)

def on_off(pin,w_t):
    GPIO.output(pin,True)
    time.sleep(w_t)
    GPIO.output(pin,False)
    time.sleep(w_t)
    #this defines the new function on_off and asks for two paramenters pin and w_t(wait time)

while True:
    on_off(7,.1)
    on_off(11,.1)
    on_off(12,.1)
    on_off(13,.1)
    #this implements the on_off function using all the pins we have set up
