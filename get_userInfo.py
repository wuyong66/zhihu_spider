#!/usr/bin/env python
# -*- coding: utf-8 -*-

'获取某个ID的昵称，居住地，所在行业等信息'
__Author__ = 'wuyong'
__Date__ = '2018/06/07'

import login
import lxml
from bs4 import BeautifulSoup

import json

def get_userInfo(userID):
    account = login.ZhihuAccount()
    account.login(username=None, password=None, load_cookies=True)

    user_url = 'https://www.zhihu.com/people/' + userID;
    response = account.session.get(user_url, headers = login.HEADERS)[1].string

    soup = BeautifulSoup(response.content, 'lxml')
    name = soup.find_all('span', {'class': 'name'})
    print(name)

if __name__ == '__main__':
    get_userInfo("liuliu")

