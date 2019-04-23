# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import re


def getHtml(url, code):
    try:
        r = requests.get(url)
        # 抛出异常
        r.raise_for_status()
        # 设定编码格式
        r.encoding = code
        return r.text
    except:
        return "error"


def getAddress(aimUrl):
    htmlContent = getHtml(aimUrl, "GB2312")
    # html解析，到这里把整个网站源代码排版整理干净
    soup = BeautifulSoup(htmlContent, 'html.parser')
    try:
        li = soup.find_all('li')
        temp = str(li[0])
        # cList = re.findall(u'[\u4E00-\u9FA5]', temp)
        return temp[9:-5]
    except:
        return 'error'

if __name__=="__main__":
    while True:
        ip = str(input("输入您要查询的ip地址:"))
        url = u'http://www.ip138.com/ips138.asp?ip='+ip+'&action=2'
        address = getAddress(url)
        print('\n归属地为：'+address+'\n')




