# encoding:utf-8
import requests 

# client_id 为官网获取的AK， client_secret 为官网获取的SK
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=vyRzDgxyEmIXKQtKnN1Fh4zB&client_secret=SjLaMh0ZYS8Fdi8geZYa9ox1hOfnwRY8'
response = requests.get(host)
# if response:
print(response.json()["access_token"])

access_token = response.json()["access_token"]

import requests
import base64

request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic"
# 二进制方式打开图片文件
f = open('images/i6.jpg', 'rb')
img = base64.b64encode(f.read())


def click(phase):
    return True


params = {"image":img}
# access_token = '[调用鉴权接口获取的token]'
request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/x-www-form-urlencoded'}
response = requests.post(request_url, data=params, headers=headers)
if response:
    word_list =  response.json()['words_result']
    # print (word_list)
    for obj in word_list:
        if "第1章" in obj['words']:
            print("phase1")
            click("phase1")
            break
        if "近海" in obj['words']:
            print("phase2")
            click("phase2")
            break
        if "选择" in obj['words']:
            print("phase3")
            click("phase3")
            break
        if "撤" in obj['words']:
            print("phase4")
            click("phase4")
            break
        if "战斗评价" in obj['words']:
            print("phase5")
            click("phase5")
            break
        if "获得" in obj['words']:
            print("phase6")
            click("phase6")
            break
        if "确定" in obj['words']:
            print("phase7")
            click("phase7")
            break


