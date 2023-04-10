import os
import requests


def run(openid):
    # headers and other basic info
    url = ''
    headers = {
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.34(0x18002230) NetType/4G Language/zh_CNF'}
    payload = {'openid': openid}
    # get user info
    url = 'http://qndxx.youth54.cn/SmartLA/dxxjfgl.w?method=getUserBasicInfo'
    res_user_info = requests.post(url=url, headers=headers, params=payload)
    user_info = res_user_info.json()
    print(user_info)
    # get current version
    url = 'http://qndxx.youth54.cn/SmartLA/dxxjfgl.w?method=getNewestVersionInfo'
    res_get_version = requests.get(url=url, headers=headers)
    version = res_get_version.json()['version']
    print('version =', version)
    # learn qndxx
    url = 'http://qndxx.youth54.cn/SmartLA/dxxjfgl.w?method=studyLatest'
    headers['content-type'] = 'application/x-www-form-urlencoded; charset=UTF-8'
    payload['version'] = version
    res_result = requests.post(url=url, headers=headers, params=payload)
    try:
        if (res_result.json()['errcode'] == '0'):
            print('qndxx success!')
    except:
        print('qndxx error!')


if __name__ == '__main__':
    OPENID = os.environ["OPENID"]
    run(openid=OPENID)
