# encoding:utf-8

import requests
import base64

'''
通用文字识别
'''

# client_id 为官网获取的AK， client_secret 为官网获取的SK
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=dmrLU83szTXVUd5SEQKNQbtu&client_secret=K0N6gTZwaaPeI4nN8Ij2ZEaI5tt1aEuE'
response = requests.get(host)
if response:
    # print(response.json())
    access_token = response.json().get('access_token')
    # print(access_token)

    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic"
    # 二进制方式打开图片文件
    f = open('pic.png', 'rb')
    img = base64.b64encode(f.read())

    params = {"image":img}
    # access_token = '[调用鉴权接口获取的token]'
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        print (response.json())