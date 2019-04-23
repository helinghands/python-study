import _thread
import time
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pandas import Series
list_ph=[]
list_temp=[]
list_pa=[]
list_rain=[]
list_max_month=[]
list_month_resule=[]
dit={}
s_pm2={}
s_pa={}
s_rain={}
s_temp={}
s_result={}
p_data={}
ph_data={}
year_data=[]
color=['dodgerblue','orangered','red','blue','green']
def avg_pm():
    global s_pm2
    p_data = data.dropna()
    for year in year_data:
        list_ph.append(p_data.loc[p_data["year"] == year].pm2.mean())
    s_pm2=Series(list_ph)
    rects1=plt.bar(range(len(list_ph)), s_pm2.values,0.5,tick_label=year_data)
    plt.xlabel('年')
    plt.ylabel('PH2.5的值')
    plt.title('各年PH2.5的值')
    for rect in rects1:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2, height + 1, str('%.2f'%(height)), ha="center", va="bottom")
    plt.show()
def avg_temp():
    global s_temp
    for year in year_data:
        list_temp.append(data.loc[data["year"] == year].TEMP.mean())
    s_temp = Series(list_temp)
    rects1 = plt.bar(range(len(list_temp)), s_temp.values, 0.5, tick_label=year_data)
    plt.xlabel('年')
    plt.ylabel('温度值')
    plt.title('各年平均温度温度值')
    for rect in rects1:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2, height + 1, str('%.2f' % (height)), ha="center", va="bottom")
    plt.show()
def all_data():
    for year in year_data:
        list_pa.append(data.loc[data["year"] == year].PRES.mean())
    s_pa = Series(list_pa)
    for year in year_data:
        list_rain.append(data.loc[data["year"] == year].Iws.mean())
    s_rain = Series(list_rain)
    plt.figure(figsize=(6.5, 8.5))
    plt.subplot(221)
    plt.xlabel('年')
    plt.ylabel('气压值')
    plt.title('各年平均气压')
    plt.plot(year_data,s_pa.values)
    plt.subplot(222)
    plt.xlabel('年')
    plt.ylabel('降雨量')
    plt.title('各年平均降雨量')
    plt.plot(year_data,s_rain.values)
    plt.subplot(223)
    plt.xlabel('年')
    plt.ylabel('温度值')
    plt.title('各年平均温度温度值')
    plt.plot(year_data,s_temp.values)
    plt.subplot(224)
    plt.xlabel('年')
    plt.ylabel('PH2.5的值')
    plt.title('各年PH2.5的值')
    plt.plot(year_data, s_pm2.values)
    plt.show()
def ph_year():
    color_id = 0
    ph_data= data.dropna()
    for year in year_data:
        #存放五个月天数
        c=0
        #存放天数
        list3=[]
        #日均phm2.5
        list4=[]
        #截取本年的数据
        data2 = ph_data.loc[ph_data['year'] == year]
        list_ph_year = []
        #遍历本年的12个月
        for month in range(1,13):
            #找出本年每个月平均值
            list_ph_year.append((float)('%.3f'%data2.loc[data2['month']== month].pm2.mean()))
            if(month==12):
                #取本年phm2.5的最大五个月
                list2=sorted(list_ph_year)[-5:]
                #遍历最大月月份
                for list in list2:
                    #找出最大月份为第几月
                    b = (list_ph_year.index(list) + 1)
                    #截取第几月的数据
                    data3=data2.loc[data2['month'] == b]
                    #判断第几月为几月
                    if b==2:
                        if(year%4==0 and year%100!=0) or year%400==0:
                            for i in range(1, 30):
                                c=c+1
                                list3.append(c)
                                list4.append(data3.loc[data3['day'] == i].pm2.mean())
                        else:
                            for i in range(1, 29):
                                c=c+1
                                list3.append(c)
                                list4.append(data3.loc[data3['day'] == i].pm2.mean())
                    if b==4 or b==6 or b==9 or b==11:
                        for i in range(1,31):
                            c=c+1
                            list3.append(c)
                            list4.append(data3.loc[data3['day'] == i].pm2.mean())
                    if b == 1 or b == 3 or b == 5 or b == 7 or b==8 or b==10 or b==12:
                        for i in range(1, 32):
                            #表达天数列表
                            c=c+1
                            list3.append(c)
                            #取日平均值
                            list4.append(data3.loc[data3['day'] == i].pm2.mean())

        plt.figure(num=3, figsize=(25, 10))
        plt.plot(list3,list4,c=color[color_id],label=year)
        color_id=color_id+1
        plt.legend(loc='upper right')
    plt.xlabel('日')
    plt.ylabel('phm2.5')
    plt.title('各年phm2.5最高的五个月')
    plt.show()

if __name__ == '__main__':
    plt.rcParams['font.sans-serif'] = ['SimHei']
    data = pd.DataFrame(pd.read_csv('pollution.csv'))
    year_data = sorted(set(data['year'].values.tolist()), key=data['year'].values.tolist().index)
    avg_pm()
    avg_temp()
    all_data()
    ph_year()



