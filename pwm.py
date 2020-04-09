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
p.start(0)

def run(dc,second):
    sleep(1)
    a= datetime.datetime.now()
    while True:
        p.start(dc)
        sleep(0.02)
        p.ChangeDutyCycle(0)
        sleep(0.2)
        b= datetime.datetime.now()
        if (b-a).seconds>second:
            return


run(0,5)
run(2.5,5)
run(5,5)
run(7.5,5)
run(10,5)
run(12.5,5)