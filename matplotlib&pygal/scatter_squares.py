import matplotlib.pyplot as plt
#显示中文
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']


#设置横纵坐标（自动计算）
x_values=list(range(1,1001))
y_values=[x**2 for x in x_values]
#设置图像散点，并设置颜色映射
plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,edgecolors='none',s=40)
#标题横纵坐标的标签
plt.title('二次方散点图',fontsize=24)
plt.xlabel('数值',fontsize=14)
plt.ylabel('二次方值',fontsize=14)
#设置横纵坐标的取值范围
plt.axis=([0,1100,0,11000])
#自动保存图像
plt.savefig('二次函数图像',bbox_inches='tight')
plt.show()