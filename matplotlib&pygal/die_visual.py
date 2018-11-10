import pygal
from die import Die


#创建一个D6
die_1=Die()
die_2=Die()
#存储掷色子的结果
results=[]
for roll_number in range(1000):
    resault=die_1.roll()+die_2.roll()
    results.append(resault)
#统计结果中的频率
frequencies=[]
max_side=die_1.sides+die_2.sides
for value in range(2,max_side+1):
    frequency=results.count(value)
    frequencies.append(frequency)
#绘制统计直方图
hist=pygal.Bar()
#设置直方图的横纵坐标
hist.title='掷1000次两个6面色子的和结果'
hist.x_labels=[2,3,4,5,6,7,8,9,10,11,12]
hist.x_title='结果'
hist.y_title='结果的频率'
#添加数值
hist.add('D6',frequencies)
#渲染为svg图像
hist.render_to_file('掷色子结果统计.svg')