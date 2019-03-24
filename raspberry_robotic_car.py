from gpiozero import LED as pin
import time
import getch

class robot:
    def __init__(self):
        self.LEFT = pin(19)
        self.RIGHT = pin(16)
        self.FORWARD = pin(26)
        self.BACKWARD = pin(20)
        functions = {self.LEFT, self.RIGHT, self.FORWARD, self.BACKWARD}
        for function in functions:                                          # by defaut are pins on input high == on 
            function.on()                                                   # to switch on means switch off

    def left(self, switch=True, status=None):                               # left switch and check right can not be on
        if status != None:
            switch = False
            if status == "on" and self.RIGHT.is_active == True :
                self.LEFT.off()
            if status == "off":
                self.LEFT.on()
        if switch:
            if self.LEFT.is_active and self.RIGHT.is_active == True :
                self.LEFT.off()
            else: self.LEFT.on()
    
    def right(self, switch=True, status=None):                              # right switch and check left can not be on
        if status != None:
            switch = False
            if status == "on" and self.LEFT.is_active == True :
                self.RIGHT.off()
            if status == "off":
                self.RIGHT.on()
        if switch:
            if self.RIGHT.is_active and self.LEFT.is_active == True :
                self.RIGHT.off()
            else: self.RIGHT.on()

    def forward(self, switch=True, status=None):                            # forward switch and check backward can not be on
        if status != None:
            switch = False
            if status == "on" and self.BACKWARD.is_active == True :
                self.FORWARD.off()
            if status == "off":
                self.FORWARD.on()
        if switch:
            if self.FORWARD.is_active and self.BACKWARD.is_active == True :
                self.FORWARD.off()
            else: self.FORWARD.on()

    def backward(self, switch=True, status=None):                           # backward switch and chack forward can not be on
        if status != None:
            switch = False
            if status == "on" and self.FORWARD.is_active == True :
                self.BACKWARD.off()
            if status == "off":
                self.BACKWARD.on()
        if switch:
            if self.BACKWARD.is_active and self.FORWARD.is_active == True :
                self.BACKWARD.off()
            else: self.BACKWARD.on()

def navigate(robot):                                        #moves by steps
    def key(robot, cont):
        if cont == "d":
            robot.right()
            time.sleep(1)
            robot.right()
    
        if cont == "a":
            robot.left()
            time.sleep(1)
            robot.left()

        if cont == "w":
            robot.forward()
            time.sleep(1)
            robot.forward()
        
        if cont == "s":
            robot.backward()
            time.sleep(1)
            robot.backward()

    while True:
        print("to stop input function press 'e'\n")
        cont = getch.getch()
        key(robot, cont)
        if cont == "e":
            break