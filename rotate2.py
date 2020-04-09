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
GPIO.setup(37, GPIO.OUT, initial=False)
p2 = GPIO.PWM(37,50) #50HZ

p.start(0)
p2.start(0)
sleep(2)


def rotate(angle):
    p.ChangeDutyCycle(2+(angle/18))
    sleep(0.5)
    p.ChangeDutyCycle(0)

def click(angle):
    p2.ChangeDutyCycle(2+(angle/18))
    sleep(0.5)
    p2.ChangeDutyCycle(0)


click(90)
sleep(1)
click(0)
sleep(1)

rotate(90)
sleep(1)
click(90)
sleep(1)
click(0)
sleep(1)

rotate(120)
sleep(1)
click(90)
sleep(1)
click(0)


rotate(0)


p.stop()
p2.stop()
GPIO.cleanup()


