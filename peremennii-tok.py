from machine import Pin, PWM
import time
#set PWM
pwm = PWM(Pin(15))
b = Pin(3, Pin.IN, Pin.PULL_UP)
pwm.freq(40)
try:

    while True:
            for i in range(0, 65535):
                if  not b.value():
                    pwm.duty_u16(i)
               
      
        
except:
        pwm.deinit()
