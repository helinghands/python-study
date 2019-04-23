# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 22:29:25 2019

@author: Heali
"""

"""
Python语法基础---循环结构
循环结构：五猴分桃
"""
#初始最后桃子个数
n=4
#初始桃子增加个数
m=0
cycle=True
#开始往上循环
while cycle :
    m=m+1
    #5只猴子往前递推
    for i in range(1,6):
        n=n*5/4+1
        #桃子数必须为整数
        if int(n)!=n:
            break
        #如果到第5个猴子后是整数，则满足条件
        elif i==5:
            print("桃子最少为{:d}个".format(int(n)))
            cycle=False
            break
    #不满足条件则初始为最开始的桃子数
    n=4+m