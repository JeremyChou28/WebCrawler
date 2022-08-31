# @description:beautiful soup爬取小说三体
# @Author: 周健平
# @company: 山东大学
# @Time: 2020/7/12 10:26
import re
import time
import urllib.request

from bs4 import BeautifulSoup

start_time = time.time()  # 计算程序运行时间
# 三体小说的目录页
url = "http://www.aixiawx.com/15/15710"
# 三体小说的网站,为了之后和chapterURL并起来得到每一章节的URL
internetURL = "http://www.aixiawx.com"
response = urllib.request.urlopen(url)

soup = BeautifulSoup(response, 'html5lib')

i = 1  # 作为循环变量滤除掉前九章最新更新的目录
k = 1  # 作为循环变量滤除掉前九章最新更新的正文内容
j = 9  # 循环变量截止的数值变量
index = 1  # 作为章节序号
# 爬取章节目录，保存到文件中
f = open("SanTi.txt", 'a', encoding='UTF-8')
f.write("小说三体  \n作者：刘慈欣\n\t 目录\n")
for link in soup.find_all('a'):
    href = link.get('href')
    # 将正则表达式编译为正则表达式对象
    r2 = re.compile('/15/15710/975', re.I)
    if r2.search(href):
        if i > j:
            f.write(link.text + "\n")
            print(link.text + "抓取完成")  # 打印目录抓取完毕的信息
        i += 1
f.close()
# 爬取各个章节的正文内容，保存到文件中
f = open("SanTi.txt", 'a', encoding='UTF-8')
for link in soup.find_all('a'):
    href = link.get('href')
    # 将正则表达式编译为正则表达式对象
    r2 = re.compile('/15/15710/975', re.I)
    if r2.search(href):
        if k > j:
            chapterURL = internetURL + href  # 得到章节网页的URL
            chapterResponse = urllib.request.urlopen(chapterURL)
            chapterSoup = BeautifulSoup(chapterResponse, 'html.parser')
            title = chapterSoup.title.string  # 读取该章节的标题
            idContents = chapterSoup.find(id='content')
            contents = idContents.get_text()  # 读取该章节的正文内容
            f.write("\n" + title + "\n\n")  # 把标题保存到文件中
            f.write(contents)  # 把正文内容保存到文件中
            f.write("\n\n----------------------------------------------\n")
            print("第" + str(index) + "章正文内容抓取完毕")  # 打印章节抓取完毕的信息
            index += 1
        k += 1
f.close()
endtime = time.time() - start_time
print(
    '程序运行了%.2f秒' % endtime)
