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

def rotate():
    # begin =datetime.datetime.now()
    while True:
        angle=input("input angle")
        p.ChangeDutyCycle(2+(angle/18))
        sleep(0.5)
        p.ChangeDutyCycle(0)
        # end = datetime.datetime.now()
        # if (end-begin).seconds >5:
        #     return


p.stop()
GPIO.cleanup()
