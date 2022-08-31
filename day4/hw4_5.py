# @description:beautiful soup爬取网页正文并保存到txt文件中
# @Author: 周健平
# @company: 山东大学
# @Time: 2020/7/12 9:43
import codecs
import time
import urllib.request

from bs4 import BeautifulSoup

start_time = time.time()
url = "http://www.aixiawx.com/16/16039/10137185.html"
response = urllib.request.urlopen(url)
soup = BeautifulSoup(response, 'html5lib')

idContents = soup.find(id='content')
contents = idContents.get_text()
# codecs提供open方法将文件保存成utf-8编码格式，防止出现乱码现象
f = codecs.open("QingYuNian_FirstChapter.txt", 'wb', 'UTF-8')
f.write(contents)
f.close()
end_time = time.time()
spend_time = end_time - start_time
print("爬取完毕,程序运行了%.2f秒" % spend_time)
