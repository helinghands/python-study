# coding:utf-8
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 设置matplotlib正常显示中文和负号
# matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 用黑体显示中文
# matplotlib.rcParams['font.family']='sans-serif'
# #matplotlib.rcParams['font.sans-serif'] = ['Microsoft YaHei']
# matplotlib.rcParams['axes.unicode_minus'] = False  # 正常显示负号

data_path = 'pollution.csv'
pollution_data = pd.read_csv(data_path)
# preprocession drop row of Nan from PM2.5
preproData = pollution_data.dropna()
# 统计每一年的数据条数
years_sum = preproData.groupby(['year']).size()
# 提出所有年份 为一个列表
years = np.array(years_sum.index)
year_day_mean_pm = []
year_day_mean_temp = []
year_day_mean_pres = []
year_totol_iws = []
for year in years:
    # 提出当前年的数据
    current_year_data = preproData.loc[preproData['year'] == year]
    # 重新对year排列 并对pm2.5求平均值 只取pm2.5列的值
    year_day_mean = current_year_data.groupby(['year'])['pm2.5'].mean()
    year_day_mean_pm.append(year_day_mean[year])
    print(str(year) + '年的日平均pm2.5:\n' + str(year_day_mean[year]))

    # 气温
    year_day_mean = current_year_data.groupby(['year'])['TEMP'].mean()
    year_day_mean_temp.append(year_day_mean[year])
    print(str(year) + '年的日平均气温:\n' + str(year_day_mean[year]))

    # 气压
    year_day_mean = current_year_data.groupby(['year'])['PRES'].mean()
    year_day_mean_pres.append(year_day_mean[year])
    print(str(year) + '年的日平均气压:\n' + str(year_day_mean[year]))

    # 年累计降雨量
    year_totol = current_year_data.groupby(['year'])['Iws'].sum()
    year_totol_iws.append(year_totol[year])
    print(str(year) + '年累计降雨量:\n' + str(year_totol[year]))

    print('\n')
# PM2.5
x = range(len(year_day_mean_pm))
rects1 = plt.bar(x=x, height=year_day_mean_pm, width=0.4, alpha=0.8, color='red')

# y轴取值范围
plt.ylim(0, 150)
plt.ylabel(u'pm2.5')
plt.xticks([index for index in x], years)
plt.xlabel(u'year')
plt.title("2010-2014 PM2.5 average of day ")
# plt.legend()     # 设置题注
for rect in rects1:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width() / 2, height + 1, str(int(height)), ha="center", va="bottom")
plt.show()

# 气温
x = range(len(year_day_mean_temp))
rects2 = plt.bar(x=x, height=year_day_mean_temp, width=0.4, alpha=0.8, color='red')

# y轴取值范围
plt.ylim(0, 50)
plt.ylabel(u'℃')
plt.xticks([index for index in x], years)
plt.xlabel(u'year')
plt.title("2010-2014 temperature average of day ")
# plt.legend()     # 设置题注
for rect in rects2:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width() / 2, height + 1, str(int(height)), ha="center", va="bottom")
plt.show()

# 2）折线图 2X2子图
plt.rcParams['figure.figsize'] = (20, 10)
# 221:pm2.5
plt.suptitle('2010-2014')
plt.subplot(221)
plt.plot(years, year_day_mean_pm, c='red')
plt.xticks(rotation=45)
plt.xlabel('year')
plt.ylabel('pm2.5')
plt.title('PM2.5 average of day')

# 气温
plt.subplot(222)
plt.plot(years, year_day_mean_temp, c='blue')
plt.xticks(rotation=45)
plt.xlabel('year')
plt.ylabel('temperature')
plt.title('temperature average of day')

# 气压
plt.subplot(223)
plt.plot(years, year_day_mean_pres, c='black')
plt.xticks(rotation=45)
plt.xlabel('year')
plt.ylabel('presure')
plt.title('presure average of day')

# 累计降雨量
plt.subplot(224)
plt.plot(years, year_totol_iws, c='gray')
plt.xticks(rotation=45)
plt.xlabel('year')
plt.ylabel('mm')
plt.title('annual rainfall')
plt.show()

# 3) pm2.5
colors = ['green', 'red', 'blue', 'gray', 'black']
for year in years:
    # 获取当前年的数据 只要'month','day','pm2.5'值
    current_year_data = preproData.loc[preproData['year'] == year, ['month', 'day', 'pm2.5']]
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
