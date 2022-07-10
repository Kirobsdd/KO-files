from machine import Pin
import time
import random




led = Pin(15, Pin.OUT)
b = Pin(13, Pin.IN, Pin.PULL_UP)
g = Pin(11, Pin.IN, Pin.PULL_UP)
try:
    
    while True:
        if not b.value():
        
            led.value(1)
        
        if not g.value():   
            led.value(0)
        
except:
    pass