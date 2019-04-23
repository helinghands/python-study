import  random
import math
"""
随机数
"""
'''
choice() :从序列的元素中随机挑选一个元素
    方法返回一个列表，元组或字符串的随机项。
    *choice()是不能直接访问的，需要导入 random 模块，然后通过 random 静态对象调用该方法。
'''
list1=[145,123,12.3,789,345]
print(random.choice(list1))#随机数
print(random.choice('abcdefg'))#随机数
print(random.choice(range(10)))#随机数


'''
randrange() 
    方法返回指定递增基数集合中的一个随机数，基数缺省值为1。
'''
# 从 1-100 中选取一个奇数
print("randrange(1,100, 2) : ", random.randrange(1, 100, 2))
# 从 1-100 中选取一个偶数
print("randrange(1,100, 2) : ", random.randrange(2, 100, 2))
# 从 0-99 选取一个随机数
print("randrange(100) : ", random.randrange(100))


'''
random() 
    方法返回随机生成的一个实数，它在[0,1)范围内。
'''
print(random.random())

'''
seed() 
    方法改变随机数生成器的种子，可以在调用其他随机模块函数之前调用此函数。。
'''
random.seed()
print ("使用默认种子生成随机数：", random.random())
random.seed(10)
print ("使用整数种子生成随机数：", random.random())
random.seed("hello",2)
print ("使用字符串种子生成随机数：", random.random())

'''
shuffle() 
    方法将序列的所有元素随机排序。
'''
list = [20, 16, 10, 5]
random.shuffle(list)
print("随机排序列表 : ", list)
random.shuffle(list)
print("随机排序列表 : ", list)


'''
uniform() 
    方法将随机生成下一个实数，它在 [x,y] 范围内。
'''
print("uniform(5, 10) 的随机浮点数 : ", round(random.uniform(5, 10)))
print("uniform(7, 14) 的随机浮点数 : ", round(random.uniform(7, 14)))
print(math.degrees(math.pi/2))