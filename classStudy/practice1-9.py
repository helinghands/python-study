'''(1)那一位导演创作的电影最多；
(2)那一位演员参演的作品最多；
(3)那两个演员共同参演的电影最多。
'''

#生成二维数组表示v[1][1]表示一号演员和一号演员合作
import re
from os import path

V = [[0 for j in range(17)] for i in range(17)]
# V=[[0]*4]*4
#存放数据数组
list=[]
#存放导演列表
list1=[]
list2=[]
list3=[]
result = {}
result2= {}
#存放导演导电影数目的临时列表
list4=[]
list5=[]
list6=[]
p = path.dirname(__file__)

def GetData():
    f = open(path.join(p, "text1.txt"), "r+", encoding='UTF-8')  # 文件的路径
    while True:
        line = f.readline()
        if len(re.sub('[\，]', " ", line).split())!=0:
            list.append(re.sub('[\，]', " ", line).split())
        if not line:
            break
    f.close()
    return list


def ChuLiData(d):
    global V
    #局部变量组装演员
    str3 = ''
    b = True
    for i in range(1,17):
        for j in range(1, 17):
            # 只填半张表
            #防止重复
            if i>=j:
                for d1 in d:
                    str="演员"+("%d"%(i))
                    str1="演员" +("%d"%(j))
                    if d1.count(str)==1 and d1.count(str1)==1:
                        V[i][j]=V[i][j]+1
    #遍历二维表查出哪位演员出演电影最多
    for i in range(0,17):
        list5.append(V[i][i])
    for i in list5:
        if i==max(list5):
            str3=str3+"演员%d"%(list5.index(i))+","
    print("%s的出演电影最多,最多为%d部"%(str3,max(list5)))
    # for x in V:
    #     print(x)
    while b:

        a=max(map(max, V))
        for i in range(1,17):
            for j in range(1, 17):
                #只遍历一边
                if i>=j:
                    if V[i][j]==a and i!=j:
                        print("演员%d和演员%d合作的次数最多，最多为%d"%(i,j,a))
                        V[i][j] = 0
                        b=False
                    if V[i][j]==a and i==j:
                        V[i][j]=0    #

def daoyan(d2):
    #局部变量组装导演
    str=''
    for d3 in d2:
        list1.append(d3[1])
    while True:
        #拷贝列表
        list3 = list1.copy()
        a = 0
        k = len(list3)
        # 循环退出条件数组为0
        if k == 0:
            break
            # 判断导演的个数
        a = list3.count(list3[0])
        result[list3[0]] = a
        while list3[0] in list1:
            list1.remove(list3[0])
            if len(list1) == 0:
                break

    max_value = max(zip(result.values(), result.keys()))
    for k in result.keys():
        if result[k]==max_value[0]:
            str=str+k+","
    print("%s创作的电影最多,最多为%d部"%(str,max_value[0]))
if __name__ == '__main__':

    data=GetData()
    #判断演员
    ChuLiData(data)
    #查出导演
    daoyan(data)