#!/usr/bin/env python
# coding=UTF-8
'''
@Description: 字典-导演、演员统计
@Author: your name
@LastEditors: Please set LastEditors
@Date: 2019-03-19 11:00:13
@LastEditTime: 2019-04-01 12:50:27
'''
from collections import Counter

dao=[1,2,3,1,2,3,4,1,2,3,1,2,3,4,5,6]
yan=[[1,2,3,4],[3,2,4,5],[1,5,3,6],[1,4,3,7],
    [1,2,3,8],[5,7,3,9],[1,4,6,7],[1,4,3,8],
    [5,4,3,9],[1,4,5,10],[1,4,3,11],[7,4,9,12],
    [1,7,3,13],[10,4,9,14],[1,8,11,15],[14,4,13,16]]
# index = [i for i in range(1,17)]
# dic = dict(index,dao)
dao_dic={i:dao[i-1] for i in range(1,17)}
yan_dic={i:yan[i-1] for i in range(1,17)}
def test1():
    print("创作电影最多的导演是：",Counter(dao).most_common(1)[0][0])
def test2():
    #每个演员参演的电影数量
    yan_num=[0 for i in range(16)]
    for i in range(16):
        for j in yan[i]:
            yan_num[j-1]+=1
    print("参演电影最多的演员是：",yan_num.index(max(yan_num))+1)
def test3():
    #每个演员参演的电影
    yan_mo_dic={i:set() for i in range(1,17)}
    for i in range(1,17):
        for j in yan[i-1]:
            yan_mo_dic[j].add(i)
    #每两个演员参演的电影数量
    two_yan_dic={}
    for i in range(1,17):
        for j in range(i+1,17):
            two_yan_dic["{}*{}".format(i,j)]=len(yan_mo_dic[i]&yan_mo_dic[j])

    two_max=max(zip(two_yan_dic.values(),two_yan_dic.keys()))
    print("{}号演员共同参演电影最多,数量为{}".format(two_max[1],two_max[0]))

    # print(yan_mo_dic)
if __name__ == "__main__":
    test1()
    test2()
    test3()
    