from country_code import get_country_coed
import json
import pygal_maps_world.maps
from pygal.style import LightColorizedStyle,RotateStyle

#加载文件
file_name='files/python/population_data.json'
with open(file_name)  as file:
    file_datas=json.load(file)
    #设置一个用于存储的空字典
    country_population={}
    #遍历文件中的数据并筛查
    for file_data in file_datas:
        if file_data['Year']=='2010':
            country=file_data['Country Name']
            country_code=get_country_coed(country)
            population=int(float(file_data['Value']))
            #存储相应的数据
            if country_code:
                country_population[country_code]=population
#将不同人口数量的国家分组
country_population1,country_population2,country_population3={},{},{}
#遍历国家及其人口数量
for country_code,population in country_population.items():
    if population<10000000:
        country_population1[country_code]=population
    elif population<1000000000:
        country_population2[country_code]=population
    else:
        country_population3[country_code]=population
#创建一个地图实例
wm_style=RotateStyle('#336699',base_style=LightColorizedStyle)
wm=pygal_maps_world.maps.World(style=wm_style)
#设置相应的标题
wm.title='World Population in 2010,by Country'
wm.add('0-10m',country_population1)
wm.add('10m-1bn',country_population2)
wm.add('>1bn',country_population3)
wm.render_to_file('world_population.svg')