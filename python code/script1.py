import machine
import time
pin1=machine.Pin(2,machine.Pin.OUT)

    while True:
   pin1.on()
   time.sleep(1)
   pin1.off()
   time.sleep(1)

   
    
