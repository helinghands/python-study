import keyword
import sys
from sys import argv,path
# python保留字
print(keyword.kwlist)
#python注释：单行注释以 # 开头，多行注释可以用多个 # 号，还有 ''' 和 """
#第一行注释
print("hello python")#第二行注释

word = '字符串'
sentence = "这是一个句子。"
paragraph = """这是一个段落，
可以由多行组成"""
print(word,sentence,paragraph)

####字符串
str='Runoob'
print(str)#输出字符串
print(str[0:-1])#输出第一个到倒数第二个的所有字符
print(str[0])#输出第一个字符
print(str[2:5])#输出第三个字符到第五个的字符
print(str[2])#输出第三个字符串
print(str[5])#输出第六个字符串
print(str[2:])#输出二到所有字符
print(str*2)#输出字符串两次
print(str[2:4]+"test")#字符串的拼接

#等待用户输入
input("\n\n按下enter键退出")

"""
print输出
    print默认输出是要换行的，如果想要实现不换行只需在末尾添加end=""
"""
x="aaa"
y="bbb"
#换行输出
print(x)
print(y)
#不换行输出
print(x,end="")
print(y,end="")

#import与from...import
print('================Python import mode==========================');
print ('命令行参数为:')
for i in sys.argv:
    print (i)
print ('\n python 路径为',sys.path)

print('================Python from import==========================');
print("path:",path)