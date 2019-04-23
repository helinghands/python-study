import re

import requests
from bs4 import BeautifulSoup
import html5lib
def get_ip_adress():
    s=""
    header={
        "authority": "www.ip.cn",
    "method": "GET",
        "path": "/",
        "scheme": "https",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "accept - encoding": "gzip,deflate,br",
        "accept-language": "zh-CN, zh;q=0.9",
        "cache-control": "max-age=0",
        "cookie": "__cfduid=d89ab5c7776a57b78a7564cb70693fbe51554612028; UM_distinctid=169f6191240717-09f492235e450f-335b4e73-1fa400-169f6191241588; CNZZDATA123770=cnzz_eid%3D1039528809-1554610028-https%253A%252F%252Fwww.sogou.com%252F%26ntime%3D1554643230",
        "referer": "https://www.sogou.com/link?url=DSOYnZeCC_oc8hI7xg6C624YafSeot-j",
        "upgrade-insecure-requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6735.400 QQBrowser/10.2.2328.400"
    }
    html = requests.get('https://www.ip.cn/',headers=header)
    html.encoding = 'utf-8'
    # print(html.text)
    bs = BeautifulSoup(html.text,"html5lib")
    list=bs.find_all('p')
    for data in list:
        s=s+data.text
    a=re.findall(r'IP.*?所在地理位置.*?\s',s)
    print(a)
if __name__ == '__main__':
    get_ip_adress()