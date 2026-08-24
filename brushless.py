#coding:utf-8
from gpiozero import PWMOutputDevice
import time

PIN = 12 #broch data sur pin 32 

motor = PWMOutputDevice(PIN, frequency=50)
print("Low speed")
motor.value = .05
time.sleep(4)

print("half speed")
motor.value = 0.075
time.sleep(4)


print("Full power")
motor.value = .1
time.sleep(4)

print("half speed")
motor.value = 0.075
time.sleep(4)

print("Low speed")
motor.value = .05
time.sleep(4)



motor.value = 0

print("Stop")