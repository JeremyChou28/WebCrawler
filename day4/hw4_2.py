# @description:beautiful soup爬取网页title
# 获取url对应的网页-->网页转化成DOM格式-->title标记
# @Author: 周健平
# @company: 山东大学
# @Time: 2020/7/12 8:26
import urllib.request

from bs4 import BeautifulSoup

url = "http://www.baidu.com"
response = urllib.request.urlopen(url)

# soup = BeautifulSoup( response , 'html.parser' )  # python内置标准库，执行速度居中，文档容错能力强
# soup = BeautifulSoup( response , 'lxml' )  # lxml html解析器速度快，文档容错能力强
# soup = BeautifulSoup( response , features="lxml-xml" )  # lxml xml解析器，速度快，唯一支持xml的解析器
soup = BeautifulSoup(response, 'html5lib')  # html5lib最好的容错性，以浏览器的方式解析文档，生成html5格式的文档

# 带title标签的网页标题
print(soup.title)
# 返回网页标题的标签名title
print(soup.title.name)
# 返回title标签中的标题
print(soup.title.string)
# 返回父节点
print(soup.title.parent)
# 返回标签父节点的名称link
print(soup.title.parent.name)
