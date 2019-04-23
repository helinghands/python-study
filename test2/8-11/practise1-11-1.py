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
ipInfo={}
url = "http://ip.tool.chinaz.com/"
ip = input("请输入ip地址:")
html=getHtml(url+ip)
soup = BeautifulSoup(html, "html.parser")
soupDiv = soup.find('div', attrs={'class': 'WhoIpWrap'})
soupText = soup.find("p",attrs={'class':'bg-blue08'})
keyName = soupText.find_all('span')
soupData = soup.find("p",attrs={'class':'bor-b1s'})
data = soupData.find_all("span")
for i in range(len(data)):
    key = keyName[i].text
    value = data[i].text
    ipInfo[key]=value
div2 = soup.find('div',attrs={'class':'IpMainWrap-right'})
dl=div2.find("dl")
dt = dl.find_all("dt")
dd = dl.find_all("dd")
for i in range(len(dd)):
    key = dt[i].text
    value = dd[i].text
    ipInfo[key]=value
print(ipInfo)

