# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 19:45:00 2020
learn python
@author: wangrui
"""
'''
import requests # 导入网页请求库
from bs4 import BeautifulSoup # 导入网页解析库
import pprint # 使打印出来的列表更方便看
import json # 用于将列表字典（json格式）转化为相同形式字符串，以便存入文件

# 豆瓣加了反爬 需要加下面这两行
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}

r = requests.get('https://movie.douban.com/top250', headers=headers)

soup = BeautifulSoup(r.content, 'html.parser')
movie_list = soup.find_all('div', class_ = 'item')

result_list = [] # 创建一个列表存储所有结果
 
for movie in movie_list:
    mydict = {}
    mydict['title'] = movie.find('span', class_ = 'title').text
    mydict['score'] = movie.find('span', class_ = 'rating_num').text
    mydict['quote'] = movie.find('span', class_ = 'inq').text
    star = movie.find('div', class_ = 'star')
    mydict['comment_num'] = star.find_all('span')[-1].text[:-3]
    result_list.append(mydict)

# 显示结果
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(result_list)
# 将result_list这个json格式的python对象转化为字符串
s = json.dumps(result_list, indent = 4, ensure_ascii=False)
# 将字符串写入文件
with open('./douban250.json', 'w', encoding = 'utf-8') as f:
    f.write(s)
    
# 如果要读取上面的json文件
#import json
#with open('movies.json', encoding = 'utf-8') as f:
#    s = f.read()
#data = json.loads(s)
#print(data)
    
# 写爬虫一定要习惯封装函数，在爬虫比较复杂的时候才能展现更清晰的逻辑

# 用于发送请求，获得网页源代码以供解析
def start_requests(url):
    r = requests.get(url)
    return r.content

# 接收网页源代码解析出需要的信息
def parse(text):
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
    r = requests.get('https://movie.douban.com/top250', headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    movie_list = soup.find_all('div', class_ = 'item')
    result_list = []
    for movie in movie_list:
        mydict = {}
        mydict['title'] = movie.find('span', class_ = 'title').text
        mydict['score'] = movie.find('span', class_ = 'rating_num').text
        mydict['quote'] = movie.find('span', class_ = 'inq').text
        star = movie.find('div', class_ = 'star')
        mydict['comment_num'] = star.find_all('span')[-1].text[:-3]
        result_list.append(mydict)
    return result_list

# 将数据写入json文件
def write_json(result):
    s = json.dumps(result, indent = 4, ensure_ascii=False)
    with open('movies.json', 'w', encoding = 'utf-8') as f:
        f.write(s)

# 主运行函数，调用其他函数
def main():
    url = 'https://movie.douban.com/top250'
    text = start_requests(url)
    result = parse(text)
    write_json(result)

# 一般做法
if __name__ == '__main__':
    main()



## 关于反爬
    
import requests
mycookie = '' # 将上图中的cookie对应部分复制过来，以字符串形式传入mycookie变量
# 这个是用户登录,输入的是用户账号信息,可以输入自己的
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
           'cookie': mycookie}  # 这个是模拟人登录
r = requests.get('https://www.zhihu.com/', headers = headers)
r.status_code # 200，表示请求成功
r.text
#下面我们来更详细地介绍这个Response对象（即上面的r变量）。
#
# Response对象，顾名思义，就是包含了网页返回信息的对象，
# 我们可以通过提取属性的方式提取其中的信息。这些信息里有我们要提取的网页源代码，
# 也有我们请求、响应的信息，有助于我们查看请求的状态。常用的有下面这些

r.status_code # 提取请求状态码
#这是HTTP状态码，表示请求的响应状态。由三位数字组成，这三位数中最重要的是第一位数字
#
#2开头的表示请求成功最常见的是200，这是最好的结果，请求没有任何问题
#3开头表示重定向，即你请求的URL可能是无效的，自动转而去请求了另外一个URL，常见301
#4开头表示客户端错误，即我们这里发的是错的。比如常见的404表示链接是无效的
#5开头表示服务器错误，即那边接收时发生了错误

r.url # 当前请求的url
r.text # 网页源代码字符型
r.content # 网页源代码bytes型
# 两种编码
r.encoding
r.apparent_encoding

'''

#### 多级链接
import requests # 导入网页请求库
from bs4 import BeautifulSoup # 导入网页解析库

def start_requests(url):
    r = requests.get(url)
    return r.content

def parse(text):
    soup = BeautifulSoup(text, 'html.parser')
    movie_list = soup.find_all('div', class_ = 'item')
    for movie in movie_list:
        print(movie.find('span', class_ = 'title').text)

def main():
    for i in range(10):
        url = 'https://movie.douban.com/top250?start={}&filter='.format(i * 25)
        text = start_requests(url)
        parse(text)

if __name__ == '__main__':
    main()












    