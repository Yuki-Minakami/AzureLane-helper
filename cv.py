import requests 
import base64

# client_id 为官网获取的AK， client_secret 为官网获取的SK
# host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=vyRzDgxyEmIXKQtKnN1Fh4zB&client_secret=SjLaMh0ZYS8Fdi8geZYa9ox1hOfnwRY8'
# response = requests.get(host)
# print(response.json()["access_token"])

access_token = '24.fbde2e097cfca488b200b3795e4a06a0.2592000.1600047619.282335-19301522'


def getToken():
    url ="https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=vyRzDgxyEmIXKQtKnN1Fh4zB&client_secret=SjLaMh0ZYS8Fdi8geZYa9ox1hOfnwRY8"
    response = requests.post(url)
    print(response.json())

def request(imagePath):
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
        # print(response.json())
        word_list = response.json()['words_result']
        # print (word_list)
        for obj in word_list:
            if '到达' in obj['words'] :
                return 'cannot'
            if '确定' in obj['words']  or  '确' in obj['words'] or '定' in obj['words'] :
                return 'mission'
            if '大获全胜' in obj['words'] or  '胜利' in obj['words']  or  '继续' in obj['words']  :
                return 'end'


# request('./images/shot.png')