# @description:beautiful soup爬取网页正文
# @Author: 周健平
# @company: 山东大学
# @Time: 2020/7/12 9:19
import urllib.request

from bs4 import BeautifulSoup

# 爬取庆余年小说第一章网页标题和正文内容
url = "http://www.aixiawx.com/16/16039/10137185.html"
response = urllib.request.urlopen(url)
soup = BeautifulSoup(response, 'html5lib')
# 找到网页标题，带标签
print(soup.find('title'))
# 输出网页标题
print(soup.find('title').get_text())
# print( soup.title.string )
# 爬取网页正文，带标签
contents = soup.find(id='content')
# print( contents )
# get_text输出正文内容，去掉标签
# 之前修改过pycharm的file encoding默认设置，改成了gbk就出现pycharm运行乱码，但是shell正常
# 后来把pycharm的设置又修改过来成UTF-8了
print(contents.get_text())
# 将爬取下来的网页正文保存成txt文件，注意编码
# f = open( "QingYuNian_FirstChapter.txt" , 'a' , encoding='UTF-8' )
# f.write( contents.get_text( ) )
# f.close( )
