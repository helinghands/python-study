# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 11:06:11 2019

@author: Heali
"""
import requests
import re
from bs4 import BeautifulSoup
def getHTMLText(url,code="utf-8"):
    try:
        r=requests.get(url)
        r.raise_for_status()
        r.encoding=code
        return r.text
    except:
        return ""
#获取股票代码，并且存放在全局变量slist
def getStockList(slist,stock_list_url):
    #获取页面超文本
    html=getHTMLText(stock_list_url,'GB2312')
    soup=BeautifulSoup(html,'html.parser')
    #找tag
    a=soup.find_all('a')
    for i in a:
        try:
            href=i.attrs['href']#提取所有href属性
            temp=re.findall(r's[hz][_]\d{6}',href)#提取代码
            temp.replace("_","")#股票代码预处理
            slist.append(temp)
        except:
            continue
    
#依次获取股票交易信息，存放到output_file
def getStockInfo(slist,stock_list_url,output_file):
    """
        slist --股票代码列表
        stock_list_url --百度股票URL前缀
        output_file --信息存储路径
    """
    count=0#进度计数器，便于计算进度
    for stockCode in slist:
        count+=1
        url=stock_list_url+stockCode+'.html'
        html=getHTMLText(url)
        try:
            if html=='':
                continue
            infoDict={}
            soup=BeautifulSoup(html,'html.parser')
            #tag数已经由BeautifulSoup建立
            #提取股票信息部分的超文本
            stockInfo=soup.find('div',attrs={'class':'stock-bets'})
            #进一步提取股票名称信息
            name=stockInfo.find_all(attrs={'class':'bets-name'})
            infoDict.update({'股票名称':name.text.split()[0]})
            
            #进一步提取指标数据
            keylist=stockInfo.find_all('dt')
            valuelist=stockInfo.find_all('dd')
            
            for j in range(len(keylist)):
                key=keylist[j].text
                value=valuelist[j].text
                infoDict[key]=value
            with open(output_file,'a',encoding='utf-8') as f:
                f.write(str(infoDict)+'\n')
                print("\r当前进度:{:.2f}%".format(count*100/len(slist)))
        except:
            print("\r当前进度:{:.2f}%".format(count*100/len(slist)))
            continue
    
if __name__=="__main__":
    stock_list_url = "http://quote.stockstar.com/stock/stock_index.html"
    stock_info_url = "https://gupiao.baidu.com/stock/"
    output_file = "BaiduSackInfo-RE.txt"
    slist=[]
    getStockList(slist,stock_list_url)
    getStockInfo(slist,stock_list_url,output_file)