import pandas as pd
import numpy as np
# print(pd.show_versions())

"""
对象创建
    通过传递值列表来创建系列，让Pandas创建一个默认的整数索引:从0开始
"""
s = pd.Series([1,3,5,np.nan,6,8])
print(s)
s = pd.Series([1,2,3,4,8,9,14])
print(s)

"""
通过传递numpy数组，使用datetime索引和标记列来创建DataFrame
"""
dates = pd.date_range('20170101', periods=7)
print(dates)

print("--"*16)
df = pd.DataFrame(np.floor(np.random.randn(7,4)*10), index=dates, columns=list('ABCD'))
print(df)


"""
通过传递可以转换为类似系列的对象的字典来创建DataFrame
"""
df2 = pd.DataFrame({'A':1.,
                    'B':pd.date_range('20170101', periods=4),
                    'C':pd.Series(1,index=list(range(4)),dtype='float32'),
                    'D':np.array([3]*4,dtype='int32'),
                    'E':pd.Categorical(["test","train","test","train"]),
                    'F':'foo'})
print(df2)

"""
查看数据
"""
dates=pd.date_range('20190412',periods=7)
df=pd.DataFrame(np.random.randn(7,4),index=dates,columns=list('ABCD'))
print("df\n",df)
print("----------------"*4)
print("df.head\n",df.head(2))
print("----------------"*4)
print("df.tail(3)\n",df.tail(3))

"""
显示索引，列和底层numpy数据
"""
dates = pd.date_range('20190412',periods=7)
df=pd.DataFrame(np.random.randn(7,4),index=dates,columns=list('ABCD'))
print("index is:")
print(df.index)
print("colume is:")
print(df.columns)
print("Value is:")
print(df.values)

print("======"*4+"df.index循环"+"======"*4)
for item in df.index:
    print(item)
print("======"*4+"df.colume循环"+"======"*4)
for item in df.columns:
    print(item)
print("======" * 4 + "df.values循环" + "======" * 4)
for item in df.values:
    print(item)
"""
描述显示数据的快速统计摘要
"""
print(df.describe())
#调换数据：行列互换
print("==========="*2+"调换数据"+"==========="*2)
print(df.T)

#通过轴排序
print("==========="*2+"通过轴排序"+"==========="*2)
print(df.sort_index(axis=1,ascending=False))
#按值排序
print("==========="*2+"按值排序"+"==========="*2)
print(df.sort_values(by='B'))

"""
# 获取
## 选择一列，产生一个系列，相当于df.A
"""
print("==========="*2+"df['A']产生一个系列"+"==========="*2)
print(df['A'])

"""
选择通过[]操作符，选择切片行。
"""
print("==========="*2+"选择通过[]操作符，选择切片行"+"==========="*2)
print(df['20190412':'20190414'])

"""
使用标签获取横截面
"""
dates = pd.date_range('20190412',periods=7)
df=pd.DataFrame(np.random.randn(7,4),index=dates,columns=list('ABCD'))
print("==========="*2+"使用标签获取横截面"+"==========="*2)
print(df.loc[dates[0]])
#通过标签选择多轴
print("==========="*2+"使用标签选择多轴"+"==========="*2)
print(df.loc[:,['A','B']])
#显示标签切片
print("==========="*2+"显示标签切片"+"==========="*2)
print(df.loc['20190412':'20190414',['A','B']])
#减少返回对象的尺寸（大小）
print("==========="*2+"减少返回对象的尺寸"+"==========="*2)
print(df.loc['20190413',['A','B']])
#获得标量值
print("==========="*2+"获取标量值"+"==========="*2)
print(df.loc[dates[0],'A'])
#快速访问标量
print("==========="*2+"快速访问标量"+"==========="*2)
print(df.at[dates[0],'A'])
"""
通过位置选择
"""
#通过传递的整数的位置选择
print("==========="*2+"通过传递的整数的位置选择"+"==========="*2)
print(df.iloc[3])
#通过整数切片
print("==========="*2+"通过整数切片"+"==========="*2)
print(df.iloc[1:6,0:3])
#通过整数位置的列表
print("==========="*2+"通过整数位置的列表"+"==========="*2)
print(df.iloc[[1,2,4],[0,2]])
#明确切片行
print("==========="*2+"明确切片行"+"==========="*2)
print(df.iloc[1:3,:])
#明确切片列
print("==========="*2+"明确切片列"+"==========="*2)
print(df.iloc[:,1:3])
#明确获取值
print("==========="*2+"明确获取值"+"==========="*2)
print(df.iloc[1,1])
#快速访问标量
print("==========="*2+"快速访问标量"+"==========="*2)
print(df.iat[1,1])

"""
布尔索引
"""
#使用单列的值选择数据
print("==========="*2+"使用单列的值选择数据"+"==========="*2)
print(df[df.A>0])
#从满足布尔条件的DataFrame选择值
print("==========="*2+"从满足布尔条件的DataFrame选择值"+"==========="*2)
print(df[df>0])
#使用isin()方法进行过滤
df2=df.copy()#复制df
df2['E']=['one','one','two','two','three','four','five']
print(df2)
print("==========="*2+"start to filter"+"==========="*2)
print(df2[df2['E'].isin(['two','four'])])