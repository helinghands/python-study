# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 09:04:03 2019

@author: weidongdong
"""

#爬虫通用框架
'''
import requests

def getHtml(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return(r.text)
    except:
        print('页面访问异常!')
        
if __name__ == "__main__":
    url='http://www.baidu.com'
    html=getHtml(url)
    print(html)
'''
import requests
from bs4 import BeautifulSoup
import bs4

#用requests获取页面
def getHtml(url):
    '''
    url:要访问的页面地址
    '''
    try:
        r=requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return(r.text)
    except:
        print('页面访问异常!')

#用bs4解析页面，获取数据
def getData(html):
    unifo=[]
    soup=BeautifulSoup(html,'html.parser')  #按html解析
    #这里只有一个tbody，有两个：soup.find('tbody')[0].child
    for tr in soup.find('tbody').children:  #得到数据行
        if isinstance(tr,bs4,element.tag):  #去除非tag项(除tr的tag项外，其他的有tr的都不要)
        tds=tr('td')        #得到行内的数据
        unifo.append([tds[0].string,tds[1].string,tds[2].string,tds[3].string])
        
    return unifo

if __name__ == "__main__":
    url='http://www.baidu.com'
    html=getHtml(url)
    CNUInfo=getData(html)
    # saveData(CNUInfo)
    