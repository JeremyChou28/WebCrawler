# @description:beautiful soup爬取庆余年小说
# @Author: 周健平
# @company: 山东大学
# @Time: 2020/7/16 19:49
import re
import time
import urllib.request

from bs4 import BeautifulSoup

start_time = time.time()
# 庆余年首页url和小说网站url
url = 'http://www.aixiawx.com/16/16039/'
index_url = 'http://www.aixiawx.com'
response = urllib.request.urlopen(url)
soup = BeautifulSoup(response, 'html5lib')
index = 1
# 爬取庆余年小说目录
f = open("QingYuNian.txt", 'w', encoding='UTF-8')
f.write("庆余年  \n作者：猫腻\n\t 目录\n")
for link in soup.find_all('a'):
    href = link.get('href')
    r2 = re.compile('/16/16039/1', re.I)

    if r2.search(href):
        if index > 9:
            title = link.text
            f.write(title + '\n')
        index += 1
print("章节目录爬取完成")
f.close()
# 爬取庆余年小说正文标题和内容
index = 1
f = open("QingYuNian.txt", 'a', encoding='UTF-8')
for link in soup.find_all('a'):
    href = link.get('href')
    r2 = re.compile('/16/16039/1', re.I)

    if r2.search(href):
        if index > 9:
            chapter_url = index_url + href
            chapterResponse = urllib.request.urlopen(chapter_url)
            chapterSoup = BeautifulSoup(chapterResponse, 'html5lib')
            title = chapterSoup.title.string
            contents = chapterSoup.find(id='content').get_text()
            # print( title )
            f.write('\n' + title + '\n')
            f.write(contents + '\n')
            f.write("---------------------------------\n")
            print("第" + str(index - 9) + "章爬取完毕")
        index += 1
f.close()
print("章节正文爬取完成")
end_time = time.time()
spend_time = end_time - start_time
print("爬取完毕，程序运行了%.2f秒" % spend_time)
