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

try:
    while True:
        angle = float(input("input angle you want"))
        p.ChangeDutyCycle(2+(angle/18))
        sleep(0.5)
        p.ChangeDutyCycle(0)

finally:
    p.stop()
    GPIO.cleanup()


