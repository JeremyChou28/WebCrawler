import urllib
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from urllib import request, parse
import time
import random
import re
import pymysql
import requests
from selenium.webdriver.common.by import By


def getmoveinfo(movie_url):
    ''' 解析每部电影信息 '''
    # req = request.Request(url=movie_url, headers={'User-Agent': random.choice(ua_info.ua_list)})
    # # req = request.Request(url=url, headers={'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.55"})
    # page = urllib.request.urlopen(req)
    # browser.execute_script("arguments[0].click();", movie_url)
    # html_str = browser.execute_script("return document.documentElement.outerHTML")
    browser.get(movie_url)
    v = browser.page_source
    # page_html = BeautifulSoup(., 'html5lib')
    page_html = BeautifulSoup(v, 'html5lib')
    # page_html = BeautifulSoup(page, 'html5lib')
    title = page_html.find_all("title")
    # print(title)
    title_content = title[0].contents
    # print(title_content)
    img = page_html.find_all('img')[0].get('src')
    # print(img)
    content = browser.find_elements(by=By.XPATH, value='//div[@id="Zoom"]/span')[0]
    str_content = content.text
    movie_name = None
    movie_type = None
    movie_script = None
    movie_director = None
    movie_timelength = None
    movie_ratings = None
    movie_leadingrole = None
    movie_district = None
    publish_year = None
    movie_introduction = None
    movie_language = None
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

    res = {}
    res['title'] = title_content[0].encode('utf8')
    res['img'] = img
    res['movie_name'] = movie_name.encode('utf8')
    res['movie_type'] = movie_type
    res['movie_language'] = movie_language
    res['movie_script'] = movie_script
    res['publish_year'] = publish_year
    res['movie_ratings'] = movie_ratings
    res['movie_timelength'] = movie_timelength
    res['movie_director'] = movie_director
    res['movie_district'] = movie_district
    res['movie_leadingrole'] = movie_leadingrole
    res['movies_introduction'] = movie_introduction
    return res


def load_to_db(index, info, cursor):
    # print(info['title'].decode("utf-8"))
    # print(info['img'])
    # print(info['movie_name'].decode("utf-8"))
    # print(info['movie_type'])
    # print(info['movie_language'])
    # print(info['movie_script'])
    # print(info['publish_year'])
    # print(info['movie_ratings'])
    # print(info['movie_timelength'])
    # print(info['movie_director'])
    # print(info['movie_leadingrole'])
    # print(info['movies_introduction'])
    movie_title = info['title'].decode("utf-8")
    movie_img = info['img']
    movie_name = info['movie_name'].decode("utf-8")
    movie_type = info['movie_type']
    movie_language = info['movie_language']
    movie_script = info['movie_script']
    movie_publish_year = info['publish_year']
    movie_ratings = info['movie_ratings']
    movie_timelength = info['movie_timelength']
    movie_director = info['movie_director']
    movie_leadingrole = info['movie_leadingrole']
    movies_introduction = info['movies_introduction']
    try:
        cursor.execute(
            "INSERT INTO movies(movie_title,movie_img,movie_name,movie_type,movie_language,movie_script,movie_publish_year,movie_ratings,movie_timelength,movie_director,movie_leadingrole,movies_introduction)VALUES('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}');".format(
                movie_title, movie_img, movie_name, movie_type, movie_language, movie_script, movie_publish_year,
                movie_ratings,
                movie_timelength,
                movie_director, movie_leadingrole, movies_introduction))
        print('第', index, '部电影信息导入数据库成功！')
    except:
        conn.rollback()
        print('第', index, '部电影信息导入数据库失败！')
    conn.commit()


def get_movie_list(url_index):
    ''' 爬取电影列表 '''
    movie_list = []
    url = "https://www.ygdy8.net/html/gndy/dyzz/list_23_{0}.html".format(url_index)
    browser.get(url)
    table_list = browser.find_elements_by_xpath('//*[@class="co_content8"]/ul/table')

    for hrefs in table_list:
        item = {}
        item['href'] = hrefs.find_element_by_class_name("ulink").get_attribute("href")
        movie_list.append(item['href'])
        # print(item['href'])
        # browser.get("item['href']")
    print('第', url_index, '页电影列表爬取完毕！该页爬取到', len(table_list), '部电影！')
    return movie_list


if __name__ == '__main__':
    conn = pymysql.connect(host='localhost', port=3306, user='root', password='sdu.292653', db='db1',
                           charset='utf8')
    cursor = conn.cursor()
    sql = "drop table if exists movies"
    cursor.execute(sql)
    sql = "create table if not exists movies(movie_id int primary key auto_increment,movie_title text,movie_img text,movie_name text,movie_type text,movie_language text,movie_script text,movie_publish_year text,movie_ratings text,movie_timelength text,movie_director text,movie_leadingrole text,movies_introduction text)auto_increment=0;"
    cursor.execute(sql)

    # 配置chrome参数，无需打开浏览器窗口即可请求
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gup')

    browser = webdriver.Chrome(options=chrome_options)
    # driver = webdriver.Chrome()
    browser.implicitly_wait(2)
    # 访问电影天堂首页
    browser.get("https://m.dytt8.net/")
    # 访问最新影片
    latest_url = "https://www.ygdy8.net/html/gndy/dyzz/index.html"
    browser.get(latest_url)
    page_num = 245
    for url_index in range(page_num):
        movielist = get_movie_list(url_index + 1)
        print('=' * 50, '解析电影信息', '=' * 50)
        for index in range(len(movielist)):
            info = getmoveinfo(movielist[index])
            load_to_db(index, info, cursor)
        # 每爬取一个页面随即休眠1-2秒钟的时间
        time.sleep(random.randint(2, 3))
    print('爬取完毕！')
    cursor.close()
    conn.close()
