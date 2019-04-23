# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 22:33:24 2019

@author: Heali
"""
import math
"""
Python算法思维---贪心算法
"""
#存放每种找零金额的张数
counts=[0,0,0,0,0,0]#定义数组
#递归函数
def giveChange(surplus):
    global str
    if surplus>=100:
        counts[0]=math.floor(surplus/100)#向下取整
        print("找您100元：",counts[0],"张")
        giveChange(surplus-100*counts[0])
    elif surplus>=50:
        counts[1]=math.floor(surplus/50)
        print("找您50元：",counts[1],"张")
        giveChange(surplus-50*counts[1])
    elif surplus>=20:
        counts[2]=math.floor(surplus/20)
        print("找您20元：",counts[2],"张")
        giveChange(surplus-20*counts[2])
    elif surplus>=10:
        counts[3]=math.floor(surplus/10)
        print("找您10元：",counts[3],"张")
        giveChange(surplus-10*counts[3])
    elif surplus>=5:
        counts[4]=math.floor(surplus/5)
        print("找您5元：",counts[4],"张")
        giveChange(surplus-5*counts[4])
    elif surplus>=1:
        counts[5]=math.floor(surplus/1)
        print("找您1元：",counts[5],"张")
        giveChange(surplus-1*counts[5])
#主函数       
def main():
    #用户支付宝金额：money
    while(True):
        try:
            money=input("请输入小明支付金额：")
            money = float(money)
            if money<0:
                print("输入有误！")
                continue
            elif 0<=money:
               break
        except ValueError:
            print("请输入数值")
    #输入小汽车单价；price
    while(True):
        try:
            price=input("请输入小汽车单价：")
            price = float(price)
            if price<0:
                print("输入有误！")
                continue
            elif 0<=price:
               break
        except ValueError:
            print("请输入数值")
    #购买小汽车数量：num
    num=eval(input('请输入要购买的汽车数量：'))
    if num<=0:
        print('对不起，请重新输入合理的汽车数目')
        return
    #找零surplus=money-price*num
    surplus=money-price*num  
    if surplus<0:
        print("对不起，您的钱不足")
    elif surplus==0:
        print("不用找零")
    else:
        print("总共找您：",surplus,"元")
        print("=================================")
        giveChange(surplus)
        print("=================================")
main()     