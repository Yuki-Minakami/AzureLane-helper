#!/usr/bin/python
# -*- coding: UTF-8 -*-
import datetime
import RPi.GPIO as GPIO
import time
import signal
import atexit
from time import sleep
 
atexit.register(GPIO.cleanup)  
 
servopin = 35
GPIO.setmode(GPIO.BOARD)
GPIO.setup(servopin, GPIO.OUT, initial=False)
p = GPIO.PWM(servopin,50) #50HZ
#p.start(0)

a= datetime.datetime.now()
while True:
    p.start(12.5)
    sleep(0.02)
    p.ChangeDutyCycle(0)
    sleep(0.2)
    b= datetime.datetime.now()
    if (b-a).seconds>5:
	break

while True:
    p.start(5)
    sleep(0.02)
    p.ChangeDutyCycle(0)
    sleep(0.2)
  