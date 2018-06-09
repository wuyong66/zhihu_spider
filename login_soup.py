
#!/usr/bin/env python
# -*- coding: utf-8 -*-

'模拟登陆知乎，采用的是BeautifulSoup方法，以便访问所有页面'
__Author__ = 'wuyong'
__Date__ = '2018/06/07'

import requests
import time
import json
import os
import re
import sys
from bs4 import BeautifulSoup

def login():
    url = 'http://www.zhihu.com'
    loginURL = 'http://www.zhihu.com/login/email'
    headers = {
        "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:41.0) Gecko/20100101 Firefox/41.0',
        "Referer": "http://www.zhihu.com/",
        'Host': 'www.zhihu.com',
    }

    data = {
        'email': '1062073083@qq.com',
        'password': 'wfmx94111807056',
        'rememberme': "true",
    }
    global s
    s = requests.session()
    global xsrf
    if os.path.exists('cookiefile'):
        with open('cookiefile') as f:
            cookie = json.load(f)
        s.cookies.update(cookie)
        req1 = s.get(url, headers=headers)
        soup = BeautifulSoup(req1.text, "html.parser")
        xsrf = soup.find('input', {'name': '_xsrf', 'type': 'hidden'}).get('value')
        # 建立一个zhihu.html文件,用于验证是否登陆成功
        with open('zhihu.html', 'w') as f:
            f.write(req1.content)

    else:
        req = s.get(url, headers=headers)
        print(req)
        soup = BeautifulSoup(req.text, "html.parser")
        #print(soup)
        xsrf = soup.find('input', {'name': '_xsrf', 'type': 'hidden'}).get('value')
        data['_xsrf'] = xsrf

        timestamp = int(time.time() * 1000)
        captchaURL = 'http://www.zhihu.com/captcha.gif?=' + str(timestamp)
        print(captchaURL)

        with open('zhihucaptcha.gif', 'wb') as f:
            captchaREQ = s.get(captchaURL, headers=headers)
            f.write(captchaREQ.content)
        loginCaptcha = input('input captcha:\n').strip()
        data['captcha'] = loginCaptcha
        print(data)
        loginREQ = s.post(loginURL, headers=headers, data=data)
        if not loginREQ.json()['r']:
            print(s.cookies.get_dict())
            with open('cookiefile', 'wb') as f:
                json.dump(s.cookies.get_dict(), f)
        else:
            print('login fail')



if __name__ == '__main__':
    login()