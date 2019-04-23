# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 08:52:58 2019

@author: Heali
"""

#requests库使用
import testR
# from bs4 import BeautifulSoup
# import bs4 

def getHtml(url):
    try:
        r=testR.get(url, timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return(r.text)
    except:
        print("页面访问异常!")
# def getData(html,uinfo):
#     soup=BeautifulSoup(html,"html.parser")
#     for tr in soup.find('tbody').children:
#         if isinstance(tr,bs4.element.Tag):
#             tds=tr('td')
#             uinfo.append[tds[0].string,tds[1].string,tds[2].string,tds[3].string,tds[4].string]
# def saveDate(uinfo,num):
#     print("{:^5}\t{:^20}\t{:^80}\t{:^10}\t{:^10}").format()
#     for i in range(num):
#         u=uinfo[i]
#         print("{:^5}\t{:^20}\t{:^80}\t{:^10}\t{:^10}").format()
if __name__ == "__main__":
    url="http://www.baidu.com"
    html=getHtml(url)
    print(html)