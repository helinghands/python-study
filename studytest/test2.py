"""
基本数据类型
"""
import math
a=12#整型变量
b=12.0#浮点变量
c="aaabbbccc"#字符串

#多个变量赋值
a1=b1=c1=4
print(a1,b1,c1)
a2,b2,c2=1,2,"test"
print(a2,b2,c2)

"""
Number类型
"""
a=111
b=222
print(isinstance(a,int))#判断变量a是否为一个int类型变量
print(isinstance(a,float))#判断变量a是否为float类型变量
print(isinstance(a,bool))#判断变量a是否为bool类型变量
print(b)

""""
数值计算
"""
print(5+4)#加法运算
print(5-3.2)#减法运算
print(3*7)#乘法运算
print(9/2)#除法，得到一个浮点数
print(9//2)#除法，得到一个整数
print(9%2)#取余
print(2**3)#指数运算2^3

"""
list（列表）:与字符串不同之处，列表元素可改变
加号 + 是列表连接运算符，星号 * 是重复操作
"""
list=['abc',123,12.3,'bcd']
list1=['avc','ace',251]
print(list)#输出整个list
print(list[1])#输出list的第二个元素
print(list[1:3])#输出第二到第三个元素
print(list[1:])#输出第二到所有的元素
print(list*2)#输出列表list两次
print(list+list1)#将list列表与list1两个列表相加
list[0]=8
print(list)#输出整个list
list.append(789)
print(list)#输出整个list
list.pop(0)
print(list)#输出整个list
print(list[1:4:1])#索引1到索引4的位置并设置为步长为1-->间隔一个元素取

"""
元组：Tuple：元组的元素不能修改。元组写在小括号 () 里，元素之间用逗号隔开
"""
tuple=(123,"456",12.6,"Asdasda")
tuple1=(123,"asdasd",12.8)
print(tuple)#输出整个元组
print(tuple[1])#输出第二个元素
print(tuple[1:3])#输出第二到第三个元素
print(tuple[1:])#输出第二到所有元素
print(tuple*2)#输出两遍元组
print(tuple+tuple1)

"""
Set（集合）
集合（set）是由一个或数个形态各异的大小整体组成的，构成集合的事物或对象称作元素或是成员
"""
student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
print(student)
#集合测试
if 'Rose' in student:
    print("Rose in student")
else:
    print("Rose not in student")

# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')
print(a)
print(a - b)     # a 和 b 的差集

"""
字典：字典（dictionary）是Python中另一个非常有用的内置数据类型
"""
dict={}
dict['one']=1
dict['name']="allan"
print(dict)
dict1={'name':"duli",'age':18,"gender":"female"}
print(dict1)#输出dict1字典
print(dict1['name'])
print(dict1['gender'])
print(dict1.keys())#输出dict1的所有键
print(dict1.values())#输出dict1的所有值

"""
运算符
"""
a = 20
b = 20

if (a is b):
    print("1 - a 和 b 有相同的标识")
else:
    print("1 - a 和 b 没有相同的标识")

if (id(a) == id(b)):
    print("2 - a 和 b 有相同的标识")
else:
    print("2 - a 和 b 没有相同的标识")

# 修改变量 b 的值
b = 30
if (a is b):
    print("3 - a 和 b 有相同的标识")
else:
    print("3 - a 和 b 没有相同的标识")

if (a is not b):
    print("4 - a 和 b 没有相同的标识")
else:
    print("4 - a 和 b 有相同的标识")

a=7.0//2
print(int(a))
print(a)

print(math.log(100,10))

#返回参数的最大值
list1=[145,123,12.3,789,345]
print(max(list1))


print ("math.modf(100.12) : ", math.modf(100.12))
print(math.pow(3,4))
print(round(3.5456))
