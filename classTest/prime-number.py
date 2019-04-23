# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 10:32:47 2019

@author: Heali
"""

"""
求100以内的素数和:只能有一和本身整除的数
"""
sum = 0
for i in range(2, 1001):
    for j in range(2, i-1):
        if i % j == 0:
            break
    else:
        #print(i)
        sum+=i
else:
    print(sum)
    
    
m = 0
for i in range(2, 1001):
    #判断是否素数,如果是就累加
    #素数的定义
    #循环2~i-1中是否有被整除的
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        m+=i
print(m)



#减少循环次数
m = 2
for i in range(3,1001,2):
    #判断是否素数,如果是就累加
    #素数的定义
    #循环2~i-1中是否有被整除的
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        m+=i
print(m)

#函数的使用
def prime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    else:
        return True 
def main():
    sum=2
    for i in range(3,1001,2):
        if prime(i):
            sum+=i
    print(sum)
#函數从这里开始执行
main()


"""
猴子爬山
递推公式：
        1   n=1
        2   n=2
f(n)=       
        4   n=3
        f(n-3)+f(n-2)+f(n-1)
"""
def upMounain(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    elif n==3:
        return 4
    else:
        return upMounain(n-3)+upMounain(n-2)+upMounain(n-1)
x=upMounain(20)
print(x)
    