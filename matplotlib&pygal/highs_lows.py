import csv
from datetime import datetime
from matplotlib import pyplot as plt

#存储文件路径
file_name='files/python/death_valley_2014.csv'
#打开文件
with open(file_name) as file:
    #读取第一行
    reader=csv.reader(file)
    header_row=next(reader)
    #读取最高气温最低气温并转换为数值存储,读取日期
    dates,highs,lows=[],[],[]
    for row in reader:
        #处理数据中的空值
        try:
            current_date=datetime.strptime(row[0],'%Y-%m-%d')
            high=int(row[1])
            low=int(row[3])
        except ValueError:
            print(str(current_date)+'缺少数据')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
    #画出每日最高气温图
fig=plt.figure(dpi=128,figsize=(10,6))
#绘制图像
plt.plot(dates,highs,c='red',alpha=0.5,linewidth=1)
plt.plot(dates,lows,c='blue',alpha=0.5,linewidth=1)
plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)
#设置标题，坐标标签以及日期格式
plt.title('Dily high and low temperatures,2014 Death Valley,CA',fontsize=24)
plt.xlabel('',fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperature(F)',fontsize=16)
plt.tick_params(axis='both',which='major',labelsize=16)
#显示图像
plt.show()