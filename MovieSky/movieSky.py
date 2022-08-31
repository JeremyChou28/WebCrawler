# @description:
# @author:Jianping Zhou
# @company:Shandong University
# @Time:2022/3/28 0:22
from bs4 import BeautifulSoup
import urllib.request

import re
import pymysql


def getmoveinfo(movie_url):
    ''' 解析每部电影信息 '''
    url = "https://www.ygdy8.net" + movie_url
    page = urllib.request.urlopen(url)
    page_html = BeautifulSoup(page, 'html5lib')
    title = page_html.find_all("title")
    # print(title)
    title_content = title[0].contents
    # print(title_content)
    img = page_html.find_all('img')[0].get('src')
    # print(img)
    content = page_html.find('span')
    str_content = str(content)
    # print(str_content)
    if (re.findall(r"◎片　　名(.*?)<br/>", str_content)):
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
        movies_introduction = re.findall(r'◎简　　介<br/><br/>(.*?)<br/>', str_content)[0]
    else:
        movies_introduction = ''

    res = {}
    res['title'] = title_content[0]
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


def load_to_db(index, info, cursor):
    ''' 将电影信息导入数据库 '''

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
    try:
        cursor.execute(
            "INSERT INTO movie(title,img,movie_name,movie_type,movie_language,movie_script,publish_year,movie_ratings,movie_timelength,movie_director,movie_leadingrole,movies_introduction)VALUES('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}');".format(
                title, img, movie_name, movie_type, movie_language, movie_script, publish_year, movie_ratings,
                movie_timelength,
                movie_director, movie_leadingrole, movies_introduction))
        print('第', index + 1, '部电影信息导入数据库成功！')
    except:
        conn.rollback()
        print('第', index + 1, '部电影信息导入数据库失败！')
    conn.commit()


def get_movie_list(url_index):
    ''' 爬取电影列表 '''
    movie_list = []
    url = "https://www.ygdy8.net/html/gndy/dyzz/list_23_{0}.html".format(url_index)
    page = urllib.request.urlopen(url)
    page_html = BeautifulSoup(page, 'html5lib')
    # print(page_html)
    label_a_list = page_html.find_all("a", {"class": "ulink"})
    # print(label_a_list)
    # print(len(label_a_list))

    for str_href in label_a_list:
        movie_list.append(str_href.get('href'))
    print('第', url_index, '页电影列表爬取完毕！该页爬取到', len(label_a_list), '部电影！')
    # print(movie_list)
    # print(len(movie_list))
    return movie_list


if __name__ == '__main__':
    conn = pymysql.connect(host='localhost', port=3306, user='root', password='sdu.292653', db='db1', charset='utf8')
    cursor = conn.cursor()
    sql = "drop table if exists movie"
    cursor.execute(sql)
    sql = "create table if not exists movie(id int primary key auto_increment,title text,img text,movie_name text,movie_type text,movie_language text,movie_script text,publish_year text,movie_ratings text,movie_timelength text,movie_director text,movie_leadingrole text,movies_introduction text)auto_increment=0;"
    cursor.execute(sql)

    page_num = 245
    for url_index in range(page_num):
        movielist = get_movie_list(url_index + 1)
        print('=' * 50, '解析电影信息', '=' * 50)
        for index in range(len(movielist)):
            info = getmoveinfo(movielist[index])
            load_to_db(index, info, cursor)
    print('爬取完毕！')
    cursor.close()
    conn.close()
