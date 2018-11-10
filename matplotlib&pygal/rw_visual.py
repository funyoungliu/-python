import matplotlib.pyplot as plt
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']
from random_walk import Randomwalk

#随机游走循环
while True:
    #创建一个随机游走用例,并随机游走
    randomwalk=Randomwalk(50000)
    randomwalk.walk()
    #设置绘制窗口
    plt.figure(dpi=128,figsize=(100,60))
    #绘制图像
    point_numbers=list(range(randomwalk.num_points+1))
    plt.scatter(randomwalk.x_values,randomwalk.y_values,
        c=point_numbers,cmap=plt.cm.Blues,edgecolors='none',s=1)
    #重新绘制起点和终点
    plt.scatter(0,0,c='green',edgecolors='none',s=100)
    plt.scatter(randomwalk.x_values[-1],randomwalk.y_values[-1],
        c='green',edgecolors='none',s=100)
    #隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    #显示图像
    plt.show()
    keep_running=input('你愿意继续吗,请按y/n')
    if keep_running=='n':
        break