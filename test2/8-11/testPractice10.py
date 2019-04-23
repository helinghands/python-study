import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#读取数据
data = pd.read_csv('pollution.csv')
#删除带有缺失值的数据行
preData = data.dropna()#返回删除后剩下的数据
#统计每一年的记录条数,将数据按年拆分成组
year_num = preData.groupby(['year']).size()
#将所有的年份创建成一个数组
yearArray = np.array(year_num.index)
#存放数据
year_mean_pm=[]#存放每个year年的pm2.5平均值
year_mean_temp=[]#存放每个year年的气温平均值
year_mean_pres=[]#存放每个year年的气压平均值
year_totol_iws=[]#存放每个year年的累计降雨量
for year in yearArray:
    #year当年的所有数据
    current_year_data = preData.loc[preData['year'] == year]
    #pm2.5
    #求当年的日平均
    year_mean = current_year_data.groupby(['year'])['pm2.5'].mean()#取出pm2.5列并求平均值
    #将当年的日平均pm2.5加入year_mean_pm
    year_mean_pm.append(year_mean[year])
    # 气温
    year_mean = current_year_data.groupby(['year'])['TEMP'].mean()
    year_mean_temp.append(year_mean[year])
    # 气压
    year_mean = current_year_data.groupby(['year'])['PRES'].mean()
    year_mean_pres.append(year_mean[year])
    # 年累计降雨量
    year_totol = current_year_data.groupby(['year'])['Iws'].sum()#求和
    year_totol_iws.append(year_totol[year])

"""
输出数据
printData(yearArray,string,data)
yearArray:年数组
string:字符串拼接是所用的字符串
data:需要输出的数据
"""
def printData(yearArray,string,data):
    #循环输出每年的日平均pm2.5
    for i in range(len(yearArray)):
        print(str(yearArray[i]) + string + str(data[i]))
    print("==============" * 5)
printData(yearArray,"年的日平均pm2.5:",year_mean_pm)
printData(yearArray,"年的日平均气温:",year_mean_pres)
printData(yearArray,"年的日平均气压:",year_mean_pres)
printData(yearArray,"年累计降雨量:",year_totol_iws)
#绘图
#绘制实战10(1)图
"""
绘制柱状图
drawChart(xData,yData,xLabel,yLabel,title,height,color)
xData:横轴数据
YData:纵轴数据
xLabel:横轴标签
yLabel:纵轴标签
title:图形标题
height:y轴取值范围
color:图表颜色
"""
def drawHistogram(xData,yData,xLabel,yLabel,title,height,color):
    x = range(len(yData))
    rects1 = plt.bar(x=x, height=yData, width=0.4, alpha=0.8, color=color)
    # y轴取值范围
    plt.ylim(0, height)
    # 设置纵轴标签
    plt.ylabel(u'' + yLabel)
    # 设置横轴标签
    plt.xlabel(u'' + xLabel)
    # 添加纵横轴的刻度：将刻度设置成yearArray
    plt.xticks(x, xData)
    # 为图形添加标题
    plt.title(u'' + title)
    for rect in rects1:
        # 为图形添加数据标签
        plt.text(rect.get_x() + rect.get_width() / 2, rect.get_height() + 1, str(int(rect.get_height())), ha="center",
                 va="baseline", fontsize=16)
    # 创建新的画图窗口
    plt.figure()
    plt.show()
pmTitle = "Daily average PM2.5 index for 2010-2014"
tempTitle = "Average Daily Temperature in 2010-2014"
drawHistogram(yearArray,year_mean_pm,'year','pm2.5',pmTitle,150,'red')
drawHistogram(yearArray,year_mean_temp,'year','℃',tempTitle,50,'blue')

# 2）2X2子图折线图
plt.rcParams['figure.figsize'] = (20,10)# 设置figure_size尺寸
plt.suptitle('2010-2014')
"""
绘制折线图
drawBrokenline(region,xData,yData,color,xLable,yLabel,title)
region：子图所在地方
xData：x轴数据
yData：y轴数据
color：折线颜色
xLabel：x轴标签
yLabel：y轴标签
title：图形标题
"""
def drawBrokenline(region,xData,yData,color,xLable,yLabel,title):
    #一个Figure对象可以包含多个子图（Axes），可以使用subplot()快速绘制
    plt.subplot(region)
    plt.plot(xData, yData, c=color)
    plt.xlabel(xLable)
    plt.ylabel(yLabel)
    plt.title(title)
#pm2.5
drawBrokenline(221,yearArray,year_mean_pm,'red','year','pm2.5','PM2.5 average of day')
# 气温
drawBrokenline(222,yearArray,year_mean_temp,'blue','year','temperature','temperature average of day')
# 气压
drawBrokenline(223,yearArray,year_mean_pres,'green','year','temperature','presure average of day')
# 累计降雨量
drawBrokenline(224,yearArray,year_totol_iws,'gray','year','mm','annual rainfall')
#显示图形
plt.show()

# 3) pm2.5
colors = ['green', 'red', 'blue', 'gray', 'black']
for year in yearArray:
    # 获取当前年的数据 只取'month','day','pm2.5'值
    current_year_data = preData.loc[preData['year'] == year, ['month', 'day', 'pm2.5']]
    # 重新对当前年的月排列 并对pm2.5 只取pm2.5列的值 并降序排列
    month_mean = current_year_data.groupby(['month'])['pm2.5'].mean().sort_values(ascending=False)
    # 取降序索引值的第一个 代表当前年的月平均pm2.5最高的五个月数 并加入列表中记录下来
    max_months = month_mean.index[:5]
    # 初始化当年最高五月总天数 当前月日平均pm2.5 value值列表
    days = 0
    pm_values = []
    for current_month in max_months:
        # 取出当月数据
        current_month_data = current_year_data.loc[current_year_data['month'] == current_month, ['day', 'pm2.5']]
        # 计算日平均pm2.5
        current_month_day_mean = current_month_data.groupby(['day'])['pm2.5'].mean()
        # 计算总天数
        days += current_month_day_mean.size
        # 提出当前月数据 并加入记录到value值列表中
        pm_values += list(current_month_day_mean.values)
    # 输入当前天数 和 pm值 画图
    plt.plot(range(days), pm_values, color=colors[year % 10], label=str(year))
plt.legend()  # 让图例生效
plt.xlabel('day')
plt.ylabel('pm2.5')
plt.show()