# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 09:09:32 2019

@author: Heali
"""

"""
猜数字游戏
"""
"""
while循环
"""
day=10
nums=1
"""
while day>=1:
    day-=1
    nums=(nums+1)*2
"""

"""
输出结果
"""
print(nums)

"""
for循环
"""
for i in range(10):
    nums=(nums+1)*2
print(nums)

for day in range(10,1,1):
    nums=(nums+1)*2
print(nums)