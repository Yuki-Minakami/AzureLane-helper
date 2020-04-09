# -*- coding: UTF-8 -*-
import requests 
import sys

import RPi.GPIO as GPIO

GPIO.setmode (GPIO.BOARD) 



# client_id 为官网获取的AK， client_secret 为官网获取的SK
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=vyRzDgxyEmIXKQtKnN1Fh4zB&client_secret=SjLaMh0ZYS8Fdi8geZYa9ox1hOfnwRY8'
response = requests.get(host)
# if response:
print(response.json()["access_token"])

access_token = response.json()["access_token"]

# imgPath = sys.argv[1] 

import requests
import base64

def click(phase):
    p = GPIO.PWM(35,50)	
    p.start(5.0)				
    p.stop()
    GPIO.cleanup()
    return True


def rotate(phase):
    p = GPIO.PWM(7,50)		
    p.start(5.0)				
    p.stop()
    GPIO.cleanup()

    click(phase)

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
    camera.capture(imgName+'.jpg')
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
        word_list =  response.json()['words_result']
        print (word_list)
        for obj in word_list:
            if u"第1章" in obj['words']:
                print("phase1")
                click("phase1")
                break
            if u"近海" in obj['words']:
                print("phase2")
                click("phase2")
                break
            if u"选择" in obj['words']:
                print("phase3")
                click("phase3")
                break
            if u"撤" in obj['words']:
                print("phase4")
                click("phase4")
                break
            if u"战斗评价" in obj['words']:
                print("phase5")
                click("phase5")
                break
            if u"获得" in obj['words']:
                print("phase6")
                click("phase6")
                break
            if u"确定" in obj['words']:
                print("phase7")
                click("phase7")
                break


request("images/i1.jpg")
request("images/i2.jpg")
request("images/i3.jpg")
request("images/i4.jpg")
request("images/i5.jpg")
request("images/i6.jpg")

