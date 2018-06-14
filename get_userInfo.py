#!/usr/bin/env python
# -*- coding: utf-8 -*-

'获取某个ID的昵称，居住地，所在行业等信息'
__Author__ = 'wuyong'
__Date__ = '2018/06/07'

import login
from login import ZhihuAccount
import lxml
from bs4 import BeautifulSoup

import json

#find_all(name , attrs , recursive , text , **kwargs)
#find(name , attrs , recursive , text , **kwargs)

def get_userInfo(userID):
    account = ZhihuAccount()
    account.login(username=None, password=None, load_cookies=True)
    id = userID
    user_url = 'https://www.zhihu.com/people/' + id + '/activities'
    response = account.session.get(user_url, headers=login.HEADERS)  # 利用这个session可以维持一个会话，保持登录状态
    #print(response.content.decode('utf-8'))  #decode解码
    soup = BeautifulSoup(response.content, 'lxml')
    print(soup.prettify())   #以标准格式显示html源码
    name = soup.title.string.split()[0]  # 把标签以外的内容打印出来，使用split分开,选取第一个字符串
    print("name: %s" % name)
    ID = id
    print("ID: %s" % id)
    university = soup.find(name = 'svg', class_="Zi Zi--Education").find_parent().find_next_sibling().string
    print("university: %s" % university)
    major = soup.find(name = 'div', class_="ProfileHeader-infosDivider").find_next_sibling().string
    print("major: %s" % major)



if __name__ == '__main__':
    get_userInfo("marcovaldong")
