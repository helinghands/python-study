# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 22:30:18 2019

@author: Heali
"""
"""
Pyhon语法基础---函数
函数：实现1000以内的所有素数之和
"""
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
    print("1000以内的所有素数之和为：{:d}".format(sum))
#函数从这里开始执行
main()