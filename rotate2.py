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


def rotateA(angle):
    p.ChangeDutyCycle(2+(angle/18))
    sleep(0.2)
    p.ChangeDutyCycle(0)

def clickA(angle):
    p2.ChangeDutyCycle(2+(angle/18))
    sleep(0.2)
    p2.ChangeDutyCycle(0)


def operateA(angle):
    rotateA(angle)
    sleep(1)
    clickA(90)
    sleep(1)
    clickA(0)
    sleep(1)


def rotateB(angle):
    return

def clickB(angle):
    return
    
def operateB(angle):
    return


# num1
operateA(130)

#num2
# operateB(90)

# resetB
# operateB(0)

#num3
operateA(40)

#resetA
operateA(0)

#num4 第一关
# operateB(50)

#第一关打完
#sleep(15)


#点三下
# clickB(116)
# clickB(116)
# clickB(116)

#resetB
# operateB(0)

#打boss
operateA(84)

# sleep(15)

#resetA
operateA(0)

#点三下
# clickB(116)
# clickB(116)
# clickB(116)

#resetB
# operateB(0)

p.stop()
p2.stop()
GPIO.cleanup()


