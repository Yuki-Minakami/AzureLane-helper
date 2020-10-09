import requests 
import base64
from time import sleep


# client_id 为官网获取的AK， client_secret 为官网获取的SK
# host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=vyRzDgxyEmIXKQtKnN1Fh4zB&client_secret=SjLaMh0ZYS8Fdi8geZYa9ox1hOfnwRY8'
# response = requests.get(host)
# print(response.json()["access_token"])

access_token = '24.5b19270cbe2bec9aaca4caa4f93ad836.2592000.1602645989.282335-19301522'


def getToken():
    url ="https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=vyRzDgxyEmIXKQtKnN1Fh4zB&client_secret=SjLaMh0ZYS8Fdi8geZYa9ox1hOfnwRY8"
    response = requests.post(url)
    print(response.json())

def request(imagePath):
    sleep(1)
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic"

    f = open(imagePath, 'rb')
    img = base64.b64encode(f.read())
    params = {"image":img}
    # access_token = '[调用鉴权接口获取的token]'
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    # print(response.json())
    if response:
        
        try:
            word_list = response.json()['words_result']
        except:
            print(response.json())
        # print (word_list)
        for obj in word_list:
            if '到达' in obj['words'] :
                return 'cannot'
            if '确定' in obj['words']  or  '确' in obj['words'] or '定' in obj['words'] :
                return 'mission'
            if '大获全胜' in obj['words'] or  '胜利' in obj['words']  or  '继续' in obj['words']  :
                return 'end'


# request('./images/shot.png')