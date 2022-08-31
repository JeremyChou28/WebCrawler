# @description:
# @author:Jianping Zhou
# @company:Shandong University
# @Time:2022/3/31 10:05
from bs4 import BeautifulSoup
import urllib.request

str_content = '''◎译　　名　登山家
◎片　　名　The Alpinist
◎年　　代　2021
◎产　　地　美国
◎类　　别　纪录片
◎语　　言　英语
◎字　　幕　中英双字
◎上映日期　2021-09-10(美国)
◎IMDb评分　8.0/10 from 6218 users
◎豆瓣评分　9.3/10 from 2194 users
◎片　　长　92分钟
◎导　　演　彼得·莫蒂默 Peter Mortimer
◎主　　演　马克·安德烈·莱克莱尔 Marc-André Leclerc
  　彼得·莫蒂默 Peter Mortimer
  　亚历克斯·霍诺德 Alex Honnold
  　赖因霍尔德·梅斯纳 Reinhold Messner

◎简　　介

马克·安德烈·莱克莱尔独自攀登，远离聚光灯。这位23岁的自由主义者进行了历史上最大胆的单人攀登。没有摄像机，也没有失误的余地，莱克莱尔提供了一种单人冒险方式的精髓。


磁力链 登山家.2021.BD.1080P.中英双字'''


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
    str_content = content.contents
    print(str_content)


movie_url = "/html/gndy/dyzz/20220317/62407.html"
getmoveinfo(movie_url)

movie_type = ''
movie_language = ''
for item in str_content.split('◎'):
    if item.find("片　　名") != -1:
        movie_name_index = item.find("片　　名")
        movie_name = item[movie_name_index + 5:-1]
        print(movie_name)
    elif item.find("类　　别") != -1:
        movie_type_index = item.find("类　　别")
        movie_type = item[movie_type_index + 5:-1]
        print(movie_type)
    elif item.find("语　　言") != -1:
        movie_language_index = item.find("语　　言")
        movie_language = item[movie_language_index + 5:-1]
        print(movie_language)
    elif item.find("字　　幕") != -1:
        movie_script_index = item.find("字　　幕")
        movie_script = item[movie_script_index + 5:-1]
        print(movie_script)
    elif item.find("上映日期") != -1:
        publish_year_index = item.find("上映日期")
        publish_year = item[publish_year_index + 5:-1]
        print(publish_year)
    elif item.find("豆瓣评分") != -1:
        movie_ratings_index = item.find("豆瓣评分")
        movie_ratings = item[movie_ratings_index + 5:-1]
        print(movie_ratings)
    elif item.find("片　　长") != -1:
        movie_timelength_index = item.find("片　　长")
        movie_timelength = item[movie_timelength_index + 5:-1]
        print(movie_timelength)
    elif item.find("导　　演") != -1:
        movie_director_index = item.find("导　　演")
        movie_director = item[movie_director_index + 5:-1]
        print(movie_director)
    elif item.find("产　　地") != -1:
        movie_district_index = item.find("产　　地")
        movie_district = item[movie_district_index + 5:-1]
        print(movie_district)
    elif item.find("主　　演") != -1:
        # filter_item = item.split()
        # item = ''.join(filter_item)
        movie_leadingrole_index = item.find("主　　演")
        item = item[movie_leadingrole_index + 5:-2].split('\u3000')
        item = ''.join(item)
        movie_leadingrole = item.replace('\n ', ',')
        print(movie_leadingrole)
    elif item.find("简　　介") != -1:
        item = item.split('\n\n\n')[0]
        movie_introduction_index = item.find("简　　介")
        movie_introduction = item[movie_introduction_index + 6:-1]
        print(movie_introduction)
