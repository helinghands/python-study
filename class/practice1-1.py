# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 08:41:27 2019

@author: Heali
"""
"""
Python语法基础---程序结构
airIndex:空气指数变量
"""
while(True):
    try:
        airIndex=input("请输入空气指数的值：")
        airIndex = float(airIndex)
        if airIndex<0 or airIndex>500:
            print("输入有误！")
            continue
        elif 0<=airIndex<=500:
           break
    except ValueError:
        print("请输入数值")
if airIndex<=35:
    print("优")
elif airIndex<=75:
    print("良")
elif airIndex<=115:
    print("轻度污染")
elif airIndex<=150:
    print("中度污染")
elif airIndex<=250:
    print("重度污染")
elif airIndex<=500:
    print("严重污染")