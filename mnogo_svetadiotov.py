from machine import Pin
import time

button = Pin(12, Pin.IN, Pin.PULL_UP)
pins = [16, 17, 18, 19, 20, 21, 22, 26, 27, 28]
def showLed():
    for pin in pins:
        led = Pin(pin + 1, Pin.OUT)
        if not button.value():
            led.value(1)
            time.sleep_ms(100)
            led.value(0)
            
    
while True:
    showLed()
    
