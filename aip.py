#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests 
import sys

import RPi.GPIO as GPIO

GPIO.setmode (GPIO.BOARD) 



# client_id 为官网获取的AK， client_secret 为官网获取的SK
# host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=vyRzDgxyEmIXKQtKnN1Fh4zB&client_secret=SjLaMh0ZYS8Fdi8geZYa9ox1hOfnwRY8'
# response = requests.get(host)
# print(response.json()["access_token"])

access_token = '24.29bec222eae4365134068309b11ae653.2592000.1588994253.282335-19301522'

# imgPath = sys.argv[1] 

import requests
import base64

def click(phase):
    GPIO.setup(35, GPIO.OUT)
    p = GPIO.PWM(35,50)	
    p.start(5.0)				
    p.stop()
    GPIO.cleanup()
    return True

def reset():
    GPIO.setup(35, GPIO.OUT)
    p = GPIO.PWM(35,50)	
    p.start(5.0)				
    p.stop()
    GPIO.cleanup()
    return True

def rotate(phase):
    GPIO.setup(7, GPIO.OUT)

    if phase == "phase1":
        p = GPIO.PWM(7,50)		
        p.start(5.0)				
        p.stop()
        GPIO.cleanup()
        click(phase)
    if phase == "phase2":
        p = GPIO.PWM(7,50)		
        p.start(5.0)				
        p.stop()
        GPIO.cleanup()
        click(phase)
    if phase == "phase3":
        p = GPIO.PWM(7,50)		
        p.start(5.0)				
        p.stop()
        GPIO.cleanup()
        click(phase)
    if phase == "phase4":
        p = GPIO.PWM(7,50)		
        p.start(5.0)				
        p.stop()
        GPIO.cleanup()
        click(phase)
    if phase == "phase5":
        p = GPIO.PWM(7,50)		
        p.start(5.0)				
        p.stop()
        GPIO.cleanup()
        click(phase)
    if phase == "phase6":
        p = GPIO.PWM(7,50)		
        p.start(5.0)				
        p.stop()
        GPIO.cleanup()
        click(phase)
    reset()
    return True

from time import sleep
from picamera import PiCamera


def snapshot(imgName):
    sleep(1)
    camera = PiCamera()
    camera.resolution = (1920, 1080)
    camera.start_preview()
    # Camera warm-up time
    sleep(2)
    camera.capture("images/"+imgName+'.jpg')
    return True


# 二进制方式打开图片文件

def request(imagePath):
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic"

    f = open(imagePath, 'rb')
    img = base64.b64encode(f.read())
    params = {"image":img}
    # access_token = '[调用鉴权接口获取的token]'
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)

    if response:
        word_list = response.json()['words_result']
        print (word_list)
        for obj in word_list:
            print (obj['words'].encode('utf-8'))
            if u"第1章" in obj['words']:
                print("phase1")
                rotate("phase1")
                break
            if u"近海" in obj['words']:
                print("phase2")
                rotate("phase2")
                break
            if u"选择" in obj['words']:
                print("phase3")
                rotate("phase3")
                break
            if u"撤" in obj['words']:
                print("phase4")
                rotate("phase4")
                break
            if u"战斗评价" in obj['words']:
                print("phase5")
                rotate("phase5")
                break
            if u"获得" in obj['words']:
                print("phase6")
                rotate("phase6")
                break
            if u"确定" in obj['words']:
                print("phase7")
                rotate("phase7")
                break


def run(phase):
    snapshot(phase)

    request("images/" + phase + ".jpg")

    sleep(10)


run("phase1")
run("phase2")
run("phase3")
run("phase4")


# request("images/i2.jpg")
# request("images/i3.jpg")
# request("images/i4.jpg")
# request("images/i5.jpg")
# request("images/i6.jpg")

