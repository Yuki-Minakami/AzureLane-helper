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

GPIO.setup(37, GPIO.OUT, initial=False)
p2 = GPIO.PWM(37,50) #50HZ
p2.start(0)

def rotate(dc,second):
    sleep(0.5)
    a= datetime.datetime.now()
    while True:
        p.start(dc)
        sleep(0.02)
        p.ChangeDutyCycle(0)
        b= datetime.datetime.now()
        if (b-a).seconds>second:
            return

def click(dc,second):
    sleep(0.2)
    a= datetime.datetime.now()
    while True:
        p2.start(dc)
        sleep(0.02)
        p2.ChangeDutyCycle(0)
        b= datetime.datetime.now()
        if (b-a).seconds>second:
            return


rotate(12.5,1)

click(12.5,0.5)
click(7.5,0.5)

rotate(2.5,0.5)

GPIO.cleanup()


