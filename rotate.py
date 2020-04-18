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

sleep(1)


def rotateA(angle):
    p.ChangeDutyCycle(2+(angle/18))
    sleep(0.4)
    p.ChangeDutyCycle(0)

i=3
while i>0:
    rotateA(90)

    i =i-1

p.stop()

GPIO.cleanup()


