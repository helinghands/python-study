#导入requests库
import requests

"""
# r = requests.get('https://api.github.com/events')
#获取网页
r = requests.get('https://www.baidu.com/')
#设置r.encoding为相应的编码
r.encoding='utf-8'
#响应状态码：如果发送了一个错误请求(一个 4XX 客户端错误，或者 5XX 服务器错误响应)，我们可以通过 Response.raise_for_status() 来抛出异常
r.raise_for_status()
#响应内容r.text
print(r.text)
"""

#将以上的封装成一个函数
def getHtml(url):
    try:
        r = requests.get(url, timeout=3000)
        r.encoding = 'utf-8'
        r.raise_for_status()
        print(r.headers)
        return r.text
    except:
        print("获取页面异常")

if __name__ == "__main__":
    url = 'https://www.baidu.com/'
    print(getHtml(url))