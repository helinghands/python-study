import re
import numpy as np
import operator
f = open('text1.txt','r', encoding='UTF-8')#读取文件并设置编码为UTF-8
list_info=[]
director=[]
performer=[]
for  line in  f.readlines():#读取一行
    # print(line)#显示输出的每一行
    if len(re.sub('[\，]', " ", line).split()) != 0:
        list_info.append(re.sub('[\，]', " ", line).split())#切割字符串并保存在list数组中
f.close()#关闭文件
arr = np.array(list_info)
#循环输出每一行的导演
for i in range(arr.shape[0]):
    director.append(arr[i][1])
    for j in range(2,len(arr[i])):
        performer.append(arr[i][j])
# 导演字典
directorDict = {}
# 演员字典
performerDict={}
# 循环统计每一个导演出现的次数并加入字典
for key in director:
    directorDict[key] = directorDict.get(key, 0) + 1
# 循环统计每一个演员出现的次数并加入字典
for key in performer:
    performerDict[key] = performerDict.get(key, 0) + 1
#对字典进行降序排序
sorted_director = sorted(directorDict.items(),key = operator.itemgetter(1), reverse=True)
sorted_performer = sorted(performerDict.items(),key = operator.itemgetter(1), reverse=True)
print("=============="*5)
string = ""
for i in range(len(sorted_director)):
    if i<3:
        string += sorted_director[i][0] + " "
    print(sorted_director[i][0] + ':' + str(sorted_director[i][1]) + "次")
print("创作的电影最多的导演为:" + string)
print("==========="*5)
for i in range(len(sorted_performer)):
    print(sorted_performer[i][0] + ':' + str(sorted_performer[i][1]) + "次")
print("参演的作品最多的演员是：" + sorted_performer[0][0])
############################
#共同参演的电影最多的演员
############################
yan = [[1, 2, 3, 4], [3, 2, 4, 5], [1, 5, 3, 6], [1, 4, 3, 7],
       [1, 2, 3, 8], [5, 7, 3, 9], [1, 4, 6, 7], [1, 4, 3, 8],
       [5, 4, 3, 9], [1, 4, 5, 10], [1, 4, 3, 11], [7, 4, 9, 12],
       [1, 7, 3, 13], [10, 4, 9, 14], [1, 8, 11, 15], [14, 4, 13, 16]]
yanTable = np.array([[0] * 17] * 17)
# 构造表 值为合作次数 记录合作次数
for i in yan:
    ct = 0
    # 遍历表中所有元素
    for v in i:
        # 若为第一个 则赋给flag 退出当前循环 遍历当前列别非第一个的演员
        if ct == 0:
            flag = v
            ct += 1
            continue
        # 把每个列表的第一个演员与其他演员关联 并在演员计数列表上记录合作值
        yanTable[flag][v] += 1
corpName = ''
corpMax = 0
for i in range(1, 17):
    # 遍历合作次数列表 将列表的对角值相加为总合作次数
    for j in range(1, 17):
        temp = yanTable[i][j] + yanTable[j][i]
        if temp > corpMax:
            corpName = '演员' + str(i) + '与演员' + str(j)
            corpMax = temp
print("共同参演的电影最多的演员为：" + corpName)
print(corpName + ': ' + str(corpMax))