import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

#4,17,27,22 
GPIO.setup(4, GPIO.OUT)     #initialising pin
GPIO.setup(17, GPIO.OUT)    #initialising pin
GPIO.setup(27, GPIO.OUT)    #initialising pin
GPIO.setup(22, GPIO.OUT)    #initialising pin

GPIO.output(4, GPIO.HIGH)   #pin on voltage
GPIO.output(4, GPIO.LOW)    #grounded pin