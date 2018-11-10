import requests
from operator import itemgetter

#获取url存储
url='https://hacker-news.firebaseio.com/v0/topstories.json'
url_request=requests.get(url)
#打印url响应信息
print('status code:',url_request.status_code)
#获取json文件
submissions_ids=url_request.json()
#创建一个id的相关信息字典
submissions_dicts=[]
for id in submissions_ids[:30]:
    #访问主页
    id_url=('https://hacker-news.firebaseio.com/v0/item/'+
            str(id)+'.json')
    id_url_request=requests.get(id_url)
    id_json=id_url_request.json()
    submissions_dict={
        'title':id_json['title'],
        'link':'http:news.ycombinator.com/item?id='+str(id),
        'comments':id_json.get('descendants',0),
    }
    submissions_dicts.append(submissions_dict)
#为新得到的id字典排序
submissions_dicts=sorted(submissions_dicts,
                        key=itemgetter('comments'),reverse=True)
#打印得到的id信息
for submissions_dict in submissions_dicts:
    print('\nTitle:',submissions_dict['title'])
    print('Discussion link:',submissions_dict['link'])
    print('Comments:',submissions_dict['comments'])