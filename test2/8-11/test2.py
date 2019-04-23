a = ["1", "2", "3", "1", "1", "2"]
dict = {}
for key in a:
    dict[key] = dict.get(key, 0) + 1
print(dict)
from collections import Counter
a = ["1", "2", "3", "1", "1", "2"]
result = Counter(a)
print(result)

import matplotlib.pyplot as plt
num_list = [1.5, 0.6, 7.8, 6]
name_list = ['Monday','Tuesday','Friday','Sunday']
plt.bar(range(len(num_list)), num_list,color='rgb',tick_label=name_list)
plt.show()

import  numpy as np
list = [[1,2,5],[2,3,5],[3,4,5],[2,3,6]]
arr = np.array(list)
print(arr.shape)#输出数组行和列
print(arr.shape[0])#输出数组的行
print(arr.shape[1])#输出数组的列