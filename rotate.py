#!/usr/bin/python
# -*- coding: UTF-8 -*-
import datetime
import RPi.GPIO as GPIO
import time
import signal
import atexit
from time import sleep
 
GPIO.setmode(GPIO.BOARD)


GPIO.setup(35, GPIO.OUT, initial=False)
p = GPIO.PWM(35,50) #50HZ
p.start(0)
sleep(2)

print("rotate 0 to 180")
duty=2
while duty<=12:
    p.ChangeDutyCycle(duty)
    sleep(0.3)
    p.ChangeDutyCycle(0)
    sleep(0.7)
    duty=duty+1


print("back to 90")
p.ChangeDutyCycle(7)
sleep(0.5)
p.ChangeDutyCycle(0)
sleep(1.5)

print("back to 0")
p.ChangeDutyCycle(2)
sleep(0.5)
p.ChangeDutyCycle(0)

p.stop()
GPIO.cleanup()


