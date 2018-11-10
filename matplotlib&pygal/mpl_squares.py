import matplotlib.pyplot as plt
#显示中文
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']


#设置横纵坐标的数值
values=[1,2,3,4,5]
squares=[1,4,9,16,25]
#绘制函数图,并设置曲线宽度
plt.plot(values,squares,linewidth=5)
#写标题，横纵坐标标签
plt.title('二次方函数',fontsize=24)
plt.xlabel('数值',fontsize=14)
plt.ylabel('平方数',fontsize=14)
#设置刻度标记的大小
plt.tick_params(axis='both',labelsize=14)
#显示函数图
plt.show()