import requests
from bs4 import BeautifulSoup

def getHtml(url):
    try:
        r = requests.get(url, timeout=15)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        # print(r.status_code)
        return r.text
    except:
        print("页面访问异常")

def getIp(html):
    infoDict = {}
    try:
        soup = BeautifulSoup(html, "html.parser")
        soupDiv = soup.find('div', attrs={'class': 'WhoIpWrap'})
        soupT = soup.find(attrs={'class': 'bg-blue08'})
        soupP = soupDiv.find(attrs={'class': 'bor-b1s'})
        data = soupP.find_all('span')
        title = soupT.find_all('span')
        for i in range(len(data)):
            key = title[i].text
            value = data[i].text
            infoDict[key] = value
        soupRightDiv = soup.find('div', attrs={'class', 'IpMainWrap-right fr'})
        soupRightDl = soupRightDiv.find('dl', attrs={'class', 'IpMRig-tit'})
        dt = soupRightDl.find_all('dt')
        dd = soupRightDl.find_all('dd')
        for i in range(len(dt)):
            key = dt[i].text
            value = dd[i].text
            infoDict[key] = value
        print(infoDict)
    except:
        print("转换异常")


url = "http://ip.tool.chinaz.com/"
temp = input("请输入ip地址:")
getIp(getHtml(url + temp))