# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 22:32:06 2019

@author: Heali
"""

"""
Python算法思维---穷举法
百鸡百钱
鸡翁一值钱无，鸡母一值钱三，鸡雏三值钱一
百钱白鸡：问鸡翁，鸡母，鸡雏各几只？
数学建模：3x+5y+(100-x-y)/3=100-->8x+14y=200
"""

"""
x:鸡母
y:鸡翁
100-x-y:鸡雏
"""
for x in range(0,34):   
    for y in range(0,21):
        if (8*x+14*y)==200:
            print("鸡母:{:d},鸡翁:{:d},鸡雏:{:d}".format(x,y,100-x-y));