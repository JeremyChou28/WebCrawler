# @description:
# @author:Jianping Zhou
# @company:Shandong University
# @Time:2022/3/28 0:22
# coding:utf-8
import requests
from bs4 import BeautifulSoup
import urllib.request

import re
import pymysql
import chardet


def getmoveinfo(movie_url):
    url = "https://www.ygdy8.net" + movie_url
    page = urllib.request.urlopen(url)
    page_html = BeautifulSoup(page, 'html5lib')
    title = page_html.find_all("title")
    print(title)
    title_content = title[0].contents
    print(title_content)
    img = page_html.find_all('img')[0].get('src')
    print(img)
    content = page_html.find('span')
    str_content = str(content)
    # print(content)
    # content_replace = str(content).replace('<br/>', '\n')
    # print(content_replace)
    if (re.findall(r"◎片　　名(.*?)<br/>", str_content)):
        print('yes')
        movie_name = re.findall(r"◎片　　名(.*?)<br/>", str_content)[0]
    else:
        movie_name = ''
    if (re.findall(r"◎类　　别(.*?)<br/>", str_content)):
        movie_type = re.findall(r"◎类　　别(.*?)<br/>", str_content)[0]
    else:
        movie_type = ''
    if (re.findall(r"◎语　　言(.*?)<br/>", str_content)):
        movie_language = re.findall(r"◎语　　言(.*?)<br/>", str_content)[0]
    else:
        movie_language = ''
    if (re.findall(r"◎字　　幕(.*?)<br/>", str_content)):
        movie_script = re.findall(r"◎字　　幕(.*?)<br/>", str_content)[0]
    else:
        movie_script = ''
    if (re.findall(r"◎上映日期(.*?)<br/>", str_content)):
        publish_year = re.findall(r"◎上映日期(.*?)<br/>", str_content)[0]
    else:
        publish_year = ''
    if (re.findall(r"◎豆瓣评分(.*?)<br/>", str_content)):
        movie_ratings = re.findall(r"◎豆瓣评分(.*?)<br/>", str_content)[0]
    else:
        movie_ratings = ''
    if (re.findall(r"◎片　　长(.*?)<br/>", str_content)):
        movie_timelength = re.findall(r"◎片　　长(.*?)<br/>", str_content)[0]
    else:
        movie_timelength = ''
    if (re.findall(r"◎导　　演(.*?)<br/>", str_content)):
        movie_director = re.findall(r"◎导　　演(.*?)<br/>", str_content)[0]
    else:
        movie_director = ''
    if (re.findall(r"◎产　　地(.*?)<br/>", str_content)):
        movie_district = re.findall(r"◎产　　地(.*?)<br/>", str_content)[0]
    else:
        movie_district = ''
    if (re.findall(r"◎主　　演(.*?)<br/>", str_content)):
        movie_leadingrole = re.findall(r"◎主　　演(.*?)<br/>", str_content)[0]
    else:
        movie_leadingrole = ''
    if (re.findall(r'◎简　　介<br/><br/>(.*?)<br/>', str_content)):
        print('yes')
        movies_introduction = re.findall(r'◎简　　介<br/><br/>(.*?)<br/>', str_content)[0]
    else:
        movies_introduction = ''

    print(type(str(title_content[0])))
    print(type(movie_name))
    # print(chardet.detect(title_content[0]))
    # print(movie_name)
    # print(movie_type)
    # print(movie_language)
    # print(movie_script)
    # print(publish_year)
    # print(movie_ratings)
    # print(movie_timelength)
    # print(movie_director)
    # print(movie_district)
    # print(movie_leadingrole)
    # print(movies_introduction)
    res = {}
    res['title'] = str(title_content[0]).encode('utf-8')
    res['img'] = img
    res['movie_name'] = movie_name
    res['movie_type'] = movie_type
    res['movie_language'] = movie_language
    res['movie_script'] = movie_script
    res['publish_year'] = publish_year
    res['movie_ratings'] = movie_ratings
    res['movie_timelength'] = movie_timelength
    res['movie_director'] = movie_director
    res['movie_district'] = movie_district
    res['movie_leadingrole'] = movie_leadingrole
    res['movies_introduction'] = movies_introduction
    return res


def load_to_db(info):
    conn = pymysql.connect(host='localhost', port=3306, user='root', password='sdu.292653', db='db1', charset='utf8')
    cursor = conn.cursor()
    sql = "create table if not exists movie(id int primary key auto_increment,title text,img text,movie_name text,movie_type text,movie_language text,movie_script text,publish_year text,movie_ratings text,movie_timelength text,movie_director text,movie_leadingrole text,movies_introduction text)auto_increment=0;"
    cursor.execute(sql)

    title = info['title']
    img = info['img']
    movie_name = info['movie_name']
    movie_type = info['movie_type']
    movie_language = info['movie_language']
    movie_script = info['movie_script']
    publish_year = info['publish_year']
    movie_ratings = info['movie_ratings']
    movie_timelength = info['movie_timelength']
    movie_director = info['movie_director']
    movie_leadingrole = info['movie_leadingrole']
    movies_introduction = info['movies_introduction']
    cursor.execute(
        "INSERT INTO movie(title,img,movie_name,movie_type,movie_language,movie_script,publish_year,movie_ratings,movie_timelength,movie_director,movie_leadingrole,movies_introduction)VALUES('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}');".format(
            title, img, movie_name, movie_type, movie_language, movie_script, publish_year, movie_ratings,
            movie_timelength,
            movie_director, movie_leadingrole, movies_introduction))
    conn.commit()
    cursor.close()
    conn.close()


def get_movie_list():
    movie_list = []
    for url_index in range(1, 2):
        url = "https://www.ygdy8.net/html/gndy/dyzz/list_23_{0}.html".format(url_index)
        page = urllib.request.urlopen(url)
        page_html = BeautifulSoup(page, 'html5lib')
        # print(page_html)
        label_a_list = page_html.find_all("a", {"class": "ulink"})
        # print(label_a_list)
        # print(len(label_a_list))

        for str_href in label_a_list:
            movie_list.append(str_href.get('href'))
        print('第', url_index, '页爬取完毕！', len(label_a_list))
        # print(movie_list)
    print(len(movie_list))
    return movie_list


if __name__ == '__main__':
    movielist = get_movie_list()
    for movieurl in movielist:
        info = getmoveinfo(movieurl)
        load_to_db(info)
        break
'''

for n in name:
    print("http://dytt8.net" + n)
    info = getmoveinfo("http://dytt8.net" + n)
    title = info['title']
    movie_name = info['movie_name']
    movie_type = info['movie_type']
    movie_language = info['movie_language']
    movie_script = info['movie_script']
    publish_year = info['publish_year']
    movie_ratings = info['movie_ratings']
    movie_timelength = info['movie_timelength']
    movie_director = info['movie_director']
    movie_leadingrole = info['movie_leadingrole']
    movies_introduction = info['movies_introduction']
    move_address = info['move_address']
    # print(movie_name)
    # print(movie_type)
    # print(movie_language)
    # print(movie_script)
    # print(publish_year)
    # print(movie_ratings)
    # print(movie_timelength)
    # print(movie_director)
    # print(movie_leadingrole)
    # print(movies_introduction)
    # print(move_address)
    break
    # print title.decode('utf-8').encode('gbk')
    cursor.execute(
        "INSERT INTO movie(title,movie_name,movie_type,movie_language,movie_script,publish_year,movie_ratings,movie_timelength,movie_director,movie_leadingrole,movies_introduction,move_address)VALUES('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}');".format(
            title, movie_name, movie_type, movie_language, movie_script, publish_year, movie_ratings, movie_timelength,
            movie_director, movie_leadingrole, movies_introduction, move_address))
    conn.commit()
conn = pymysql.connect(host='localhost', port=3306, user='root', password='sdu.292653', db='db1', charset='utf8')
sql = "create table if not exists movie(id int primary key auto_increment,title text,movie_name text,movie_type text,movie_language text,movie_script text,publish_year text,movie_ratings text,movie_timelength text,movie_director text,movie_leadingrole text,movies_introduction text,move_address text)auto_increment=0;"
cursor = conn.cursor()
cursor.execute(sql)
cursor.close()
conn.close()
print('ok')
'''
