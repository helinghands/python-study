# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 08:41:28 2019

@author: Heali
"""

"""
输入小汽车单价；price,用户支付宝金额：money,购买小汽车数量：num
找零surplus=money-price*num
"""
price=eval(input("请输入小汽车单价："))
money=eval(input("请输入小明钱的面值："))
num=eval(input("请输入小明买的车的辆数："))
str=""
surplus=money-price*num
print("总共找您：",surplus,"元")
def giveChange(surplus):
    global str
    if surplus<0:
        print("对不起，您的钱不足")
    elif surplus-100>=0:
        str+="一张100,"
        giveChange(surplus-100)
    elif surplus-50>=0:
        str+="一张50,"
        giveChange(surplus-50)
    elif surplus-20>=0:
        str+="一张20,"
        giveChange(surplus-20)
    elif surplus-10>=0:
        str+="一张10,"
        giveChange(surplus-10)
    elif surplus-5>=0:
        str+="一张5,"
        giveChange(surplus-5)
    elif surplus-1>=0:
        str+="一张1"
        giveChange(surplus-1)
giveChange(surplus)
print(str)  