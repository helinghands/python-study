# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 10:44:32 2019

@author: Heali
"""

"""
为多个变量赋值
"""
a, b, c = 1, 2, "john"
print(c)

"""
python元组
"""
tuple = ( 'runoob', 786 , 2.23, 'john', 70.2 )
tinytuple = (123, 'john')
print(tuple)               # 输出完整元组
print(tuple[0])            # 输出元组的第一个元素
print(tuple[1:3])          # 输出第二个至第三个的元素 
print(tuple[2:])           # 输出从第三个开始至列表末尾的所有元素
print(tinytuple * 2)       # 输出元组两次
print(tuple + tinytuple)   # 打印组合的元组



"""
python字典
"""
dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"
 
tinydict = {'name': 'john','code':6734, 'dept': 'sales'}
 
print(dict['one'])          # 输出键为'one' 的值
print(dict[2])              # 输出键为 2 的值
print(dict)
print(tinydict)             # 输出完整的字典
print(tinydict.keys())      # 输出所有键
print(tinydict.values())    # 输出所有值

x=int(input("请输入一个数字:"))
print(isinstance(x,int))#isinstance用于判断数据类型

"""
python之运算符
"""
a = 16
b = 5
c = a//b
d = a/b
print("c 的值为：", c)#取整除 - 返回商的整数部分（向下取整）
print("d 的值为：", d)

"""
python之逻辑运算符
"""
x=10
y=20
print(x>y and y)

"""
成员运算符
"""
a = 10
b = 20
list = [1, 2, 3, 4, 5 ];
if ( a in list ):
   print("变量 a 在给定的列表中 list 中")
else:
   print("变量 a 不在给定的列表中 list 中")
