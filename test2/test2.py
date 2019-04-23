# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 09:04:03 2019

@author: DuLi
"""

#爬虫通用框架
import requests
import bs4
from bs4 import BeautifulSoup

#用requests获取页面
def getHtml(url):
    #url:要访问的页面地址
    try:
        r=requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return(r.text)
    except:
        print('页面访问异常!')


def getData(uinfo,html):
    """" 用bs4解析页面，获取数据"""
    soup=BeautifulSoup(html,"html.parser")  #按html解析
    #这里只有一个tbody，有两个：soup.find('tbody')[0].child
    for tr in soup.find('tbody').children:  #得到数据行
        if isinstance(tr,bs4.element.Tag):  #去除非tag项(除tr的tag项外，其他的有tr的都不要)
            tds=tr('td')        #得到行内的数据
            uinfo.append([tds[0].string,tds[1].string,tds[2].string,tds[3].string,tds[4].string])

def saveData(uinfo,num):
    tql="{0:^5}\t{1:^20}\t{2:^80}\t{3:^10}\t{4:^10}"
    print(tql.format("排名","学校名称","省市","总分","指标得分",chr(12288)))
    for i in range(num):
        u=uinfo[i]
        if u[0] is not None and u[1] is not None and u[2] is not None and u[3] is not None and u[4] is not None:
            print(tql.format(u[0],u[1],u[2],u[3],u[4],chr(12288)))

if __name__ == "__main__":
    uinfo=[]
    url='http://www.zuihaodaxue.com/zuihaodaxuepaiming2018.html'
    html=getHtml(url)
    getData(uinfo,html)
    saveData(uinfo,40)
