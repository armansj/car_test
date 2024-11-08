from machine import Pin, PWM
import time

in1 = Pin(15, Pin.OUT)
in2 = Pin(14, Pin.OUT)
ena = PWM(Pin(13))  
ena.freq(1000)      

def motor_forward(speed):
    in1.value(1)
    in2.value(0)
    ena.duty_u16(int(speed * 65535))  
def motor_reverse(speed):
    in1.value(0)
    in2.value(1)
    ena.duty_u16(int(speed * 65535))  

def motor_stop():
    in1.value(0)
    in2.value(0)
    ena.duty_u16(0)

try:
    while True:
        print("Increasing Speed")
        for speed in [0.2,0.4,0.4]:  
            motor_forward(speed)
            print(f"Motor running at {int(speed*100)}% speed")
            time.sleep(3) 
        
        print("Decreasing Speed")
        for speed in [0.2, 0.1,0.05,0.01]:  
            motor_forward(speed)
            print(f"Motor running at {int(speed*100)}% speed")
            time.sleep(3)  
        
        print("Reversing Direction at 100% Speed")
        motor_reverse(0.4)
        time.sleep(3)
        
        print("Motor Stop")
        motor_stop()
        time.sleep(3)

except KeyboardInterrupt:
    motor_stop()
    print("Program stopped")
