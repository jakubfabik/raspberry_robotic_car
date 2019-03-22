from gpiozero import LED as pin
import time

class robot:
    def __init__(self):
        self.LEFT = pin(19)
        self.RIGHT = pin(16)
        self.FORWARD = pin(26)
        self.BACKWARD = pin(20)
        functions = {self.LEFT, self.RIGHT, self.FORWARD, self.BACKWARD}
        for function in functions:
            function.on()

    def left(self, switch=True, status=None):
        if status != None:
            switch = False
            if status == "on":
                self.LEFT.off()
            if status == "off":
                self.LEFT.on()
        if switch:
            if self.LEFT.is_active:
                self.LEFT.off()
            else: self.LEFT.on()
    
    def right(self, switch=True, status=None):
        if status != None:
            switch = False
            if status == "on":
                self.RIGHT.off()
            if status == "off":
                self.RIGHT.on()
        if switch:
            if self.RIGHT.is_active:
                self.RIGHT.off()
            else: self.RIGHT.on()

    def forward(self, switch=True, status=None):
        if status != None:
            switch = False
            if status == "on":
                self.FORWARD.off()
            if status == "off":
                self.FORWARD.on()
        if switch:
            if self.FORWARD.is_active:
                self.FORWARD.off()
            else: self.FORWARD.on()

    def backward(self, switch=True, status=None):
        if status != None:
            switch = False
            if status == "on":
                self.BACKWARD.off()
            if status == "off":
                self.BACKWARD.on()
        if switch:
            if self.BACKWARD.is_active:
                self.BACKWARD.off()
            else: self.BACKWARD.on()