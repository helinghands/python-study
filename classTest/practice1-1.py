# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 08:41:27 2019

@author: Heali
"""
"""
airIndex:空气指数变量
"""
airIndex=eval(input("请输入空气指数："))
if airIndex<=0:
    print("error")
elif airIndex<=35:
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
else:
    print("error")