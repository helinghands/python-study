# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 22:34:32 2019

@author: Heali
"""
"""
Python算法思维---动态规划
"""
weight = [4, 5, 2, 1, 6]    #weight[i]表示物品的重量
value = [45, 57, 22, 11, 67]    #value[i]表示物品的价值
m = 8   #背包所能承受的最大重量
n=len(weight)-1
x=[False for raw in range(n+1)]     #x[i]为TRUE，表示物品被放入背包
a=[[0 for col in range(m+1)] for raw in range(n+1)]
def knp_DP(n,m):
    for i in range(1,n+1):
        for j in range(1,m+1):
            a[i][j]=a[i-1][j]
            if(j>=weight[i])and(a[i-1][j-weight[i]]+value[i]>a[i-1][j]):
                a[i][j]=a[i-1][j-weight[i]]+value[i]
    j=m
    for i in range(n,0,-1):
        if a[i][j]>a[i-1][j]:
            x[i]=True
            j=j-weight[i]
    print(x)
    Maxvalue=a[n][m]
    return Maxvalue
print("最大收益：",knp_DP(n,m))