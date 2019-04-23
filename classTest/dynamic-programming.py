# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 09:25:55 2019

@author: Heali
"""

weight = [4, 5, 2, 1, 6]
value = [45, 57, 22, 11, 67]
maxweight = 8

# 只输出最大价值
def CompletePack_Simple(W, V, MW):#完全背包
    #存储最大价值的一维数组
    valuelist = [0] * (MW + 1)
    #开始计算
    for ii in range(len(W)):#从第一个物品
        for jj in range(MW + 1):#从重量0
            if jj >= W[ii]:#如果重量大于物品重量
                valuelist[jj] = max(valuelist[jj - W[ii]] + V[ii], valuelist[jj])#选中第ii个物品和不选中，取大的
    return '最大价值：', valuelist[-1]

#  也输出选择物品的编号以及个数
def CompletePack(W, V, MW):#完全背包
    #存储最大价值的一维数组
    valuelist = [0] * (MW + 1)
    #存储物品编号的字典
    codedict = {i: [] for i in range(0, MW + 1)}
    #开始计算
    for ii in range(len(W)):#从第一个物品
        copyvalue = valuelist.copy()
        copydict = codedict.copy()
        for jj in range(MW + 1):#从重量0
            if jj >= W[ii]:#如果重量大于物品重量
                cc = copyvalue[jj]
                copyvalue[jj] = max(copyvalue[jj - W[ii]] + V[ii], copyvalue[jj])#选中第ii个物品和不选中，取大的
                #输出被选中的物品编号
                if copyvalue[jj] > cc:
                    copydict[jj] = [ii]
                    for hh in copydict[jj - W[ii]]:
                        copydict[jj].append(hh)
        codedict = copydict.copy()#更新
        valuelist = copyvalue.copy()#更新
    result = ''
    for hcode in sorted(list(set(copydict[MW]))):
        result += '物品：%d :%d个' % (hcode + 1, copydict[MW].count(hcode))
    print(result)
    return '最大价值：', valuelist[-1]

print(CompletePack_Simple(weight, value, maxweight))