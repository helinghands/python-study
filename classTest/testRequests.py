# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 08:52:58 2019

@author: Heali
"""

#requests库使用
import requests

def getHtml(url):
    try:
        r=requests.get(url, timeout=3000)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return(r.text)
    except:
        print("页面访问异常!")

if __name__ == "__main__":
    url="http://www.baidu.com"
    html=getHtml(url)
    print(html)