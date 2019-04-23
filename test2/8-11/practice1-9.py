# practice1-9
import pandas as pd
import numpy as np

dao = [1, 2, 3, 1, 2, 3, 4, 1, 2, 3, 1, 2, 3, 4, 5, 6]
yan = [[1, 2, 3, 4], [3, 2, 4, 5], [1, 5, 3, 6], [1, 4, 3, 7],
       [1, 2, 3, 8], [5, 7, 3, 9], [1, 4, 6, 7], [1, 4, 3, 8],
       [5, 4, 3, 9], [1, 4, 5, 10], [1, 4, 3, 11], [7, 4, 9, 12],
       [1, 7, 3, 13], [10, 4, 9, 14], [1, 8, 11, 15], [14, 4, 13, 16]]
# index = [i for i in range(1,17)]
# dic = dict(index,dao)
# 加字
for i in range(16):
    dao[i] = '导演' + str(dao[i])
for i in range(16):
    for j in range(4):
        yan[i][j] = '演员' + str(yan[i][j])
daosum = []
# 将全部演员放入一个列表
for l in yan:
    daosum += l
dicdao = {'导演': dao}
# npdao = np.array(dao)
# npyan = np.array(yan)
dfdao = pd.DataFrame(data=dicdao)
# 统计导演整体列表的 每个导演出现次数
daoct = dfdao.groupby(['导演']).size()
mx = max(daoct)  # 求最高次数的次数值
for i in range(1, 7):  # 遍历每个导演
    if daoct['导演' + str(i)] == mx:  # 若该导演的次数为最高次 则输出导演名字
        print('导演' + str(i) + ': ' + str(mx) + '次')
# print(daoct)

yansum = []
# 将全部演员放入一个列表
for l in yan:
    yansum += l
dicyan = {'演员': yansum}
dfyan = pd.DataFrame(data=dicyan)
# 统计演员整体列表的 每个演员出现次数
yanct = dfyan.groupby(['演员']).size()
mx = max(yanct)
for i in range(1, 17):
    if yanct['演员' + str(i)] == mx:
        print('演员' + str(i) + ': ' + str(mx) + '次')

yan = [[1, 2, 3, 4], [3, 2, 4, 5], [1, 5, 3, 6], [1, 4, 3, 7],
       [1, 2, 3, 8], [5, 7, 3, 9], [1, 4, 6, 7], [1, 4, 3, 8],
       [5, 4, 3, 9], [1, 4, 5, 10], [1, 4, 3, 11], [7, 4, 9, 12],
       [1, 7, 3, 13], [10, 4, 9, 14], [1, 8, 11, 15], [14, 4, 13, 16]]
yanTable = np.array([[0] * 17] * 17)
for i in yan:  # 构造表 值为合作次数 记录合作次数
    ct = 0
    for v in i:  # 遍历表中所有元素
        if ct == 0:  # 若为第一个 则赋给flag 退出当前循环 遍历当前列别非第一个的演员
            flag = v
            # print('c')
            ct += 1
            continue
        yanTable[flag][v] += 1  # 把每个列表的第一个演员与其他演员关联 并在演员计数列表上记录合作值

corpName = ''
corpMax = 0
print(yanTable)
for i in range(1, 17):
    for j in range(1, 17):  # 遍历合作次数列表 将列表的对角值相加为总合作次数
        temp = yanTable[i][j] + yanTable[j][i]
        if temp > corpMax:
            corpName = '演员' + str(i) + '与演员' + str(j)
            corpMax = temp
print(corpName + ': ' + str(corpMax))


