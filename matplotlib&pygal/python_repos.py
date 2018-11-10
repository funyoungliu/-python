import requests
import pygal
from pygal.style import LightColorizedStyle as LCS,LightenStyle as LS

#请求相应的url
url='https://api.github.com/search/repositories?q=python&sort=stars'
url_request=requests.get(url)
#查看网址相应信息
print('stats code: '+str(url_request.status_code))
#获取网址中相应的信息
items_information=url_request.json()
#打印项目总数
print('total items:'+str(items_information['total_count']))
#遍历项目信息
items=items_information['items']
print('items count:',len(items))
#存储图像的横纵坐标
names,plot_dicts=[],[]
for item in items:
    names.append(item['name'])
    plot_dict={
        'value':item['stargazers_count'],
        'label':item['description'],
        'xlink':item['html_url']
    }
    plot_dicts.append(plot_dict)
#设置图像参数
my_style=LS('#333366',base_style=LCS)
my_config=pygal.Config()
my_config.x_label_rotation=45
my_config.show_legend=False
my_config.title_font_size=24
my_config.label_font_size=14
my_config.major_label_font_size=18
my_config.truncate_label=15
my_config.show_y_guides=False
my_config.width=1000
#绘制图像
chart=pygal.Bar(config=my_config,style=my_style)
chart.title='Most-Starred Python Projects on GitHub'
chart.x_labels=names
chart.add('',plot_dicts)
#显示图像
chart.render_to_file('python_repos.svg')