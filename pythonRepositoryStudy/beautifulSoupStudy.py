#导入库
import requests
from bs4 import BeautifulSoup

def getHtml(url):
    try:
        r = requests.get(url, timeout=3000)
        r.encoding = 'utf-8'
        r.raise_for_status()
        print(r.headers)
        return r.text
    except:
        print("获取页面异常")
html_doc = getHtml('https://www.baidu.com/')
#BeautifulSoup 第一个参数应该是要被解析的文档字符串或是文件句柄,第二个参数用来标识怎样解析文档.
soup = BeautifulSoup(html_doc, "html.parser")
"""
print(soup.prettify())#按照标准的缩进格式的结构输出
"""
print(soup.title)
print(soup.title.name)
print(soup.title.string)
print(soup.title.parent.name)
#获取第一个p元素
print(soup.p)
#获取文档中第一个a元素
print(soup.a)
#获取文档中所有的a元素
print(soup.find_all('a'))
#循环所有的a元素
for link in soup.find_all('a'):
    print(link.get('href'))#得到a元素的href属性
    print(link.get_text())#获取a元素的文本内容
print(soup.get_text())#获取文档中的所有文本内容
print(soup.find('title'))#查找title元素

markup = '<a href="http://example.com/">I linked to <i>example.com</i></a>'
soup = BeautifulSoup(markup)
tag = soup.a
tag.insert(1, "but did not endorse ")
print(tag)
print(tag.contents)