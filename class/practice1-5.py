# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 22:32:47 2019

@author: Heali
"""

"""
Python算法思维---递归
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
print("上山有{:d}种不同的跳法".format(x))