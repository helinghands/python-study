# -*- coding:utf-8 -*-
"""
@project:Python
@author:Heali
@file:preactice1-11-2.py
@ide:PyCharm
@time1:2019-04-17 18:23:06
"""
import requests
def getHtml(url):
    try:
        r = requests.get(url, timeout=15)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        # print(r.status_code)
        return r.text
    except:
        print("页面访问异常")
url = "https://item.jd.com/100003023796.html"
html = getHtml(url)
print(html)