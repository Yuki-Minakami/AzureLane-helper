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

def rotate(angle):
    p.ChangeDutyCycle(2+(angle/18))
    sleep(0.5)
    p.ChangeDutyCycle(0)

rotate(0)
sleep(1)
rotate(90)
sleep(1)
rotate(180)
sleep(1)
rotate(0)

p.stop()
GPIO.cleanup()


