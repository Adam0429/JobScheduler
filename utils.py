import requests
import json

def dingmessage(text):
    webhook = "https://oapi.dingtalk.com/robot/send?access_token="
    header = {
        "Content-Type": "application/json",
        "Charset": "UTF-8"
    }
    if '失败' in text:
        isAtAll = True
    else:
        isAtAll = False

    message = {
        "msgtype": "text",
        "text": {
            "content": text
        },
        "at": {
            "isAtAll": isAtAll
        }
    }
    message_json = json.dumps(message)
    requests.post(url=webhook, data=message_json, headers=header)
    # print(text)