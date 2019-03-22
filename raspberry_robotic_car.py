import RPi.GPIO as GPIO
import time



GPIO.output(4, GPIO.HIGH)                                                           #pin on voltage
GPIO.output(4, GPIO.LOW)                                                            #grounded pin

class robot:
    def __init__(self):
        pin = {"left":4, "ryght":17, "forward":27, "backward":22}                   #pins in the use
        for key in pin:
            GPIO.setup(pin.pop(key), GPIO.OUT)                                      #initializing pin
            GPIO.output(pin.pop(key), GPIO.LOW)                                     #switching pins off
            print(f"initializing pin {key}")

    def on(self, part):
        return GPIO.output(self.pin[part], GPIO.HIGH)                               #turn on name of pin

    def off(self, part):
        return GPIO.output(self.pin[part], GPIO.LOW)                                #turn off name of pin

    def switch(self, part):                                                         #switch logic value of pin
        if GPIO.input(self.pin[part]):
            return GPIO.output(self.pin[part], GPIO.LOW)
        else:
            return GPIO.output(self.pin[part], GPIO.HIGH)

