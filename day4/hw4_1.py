# @description:beautiful soup爬取整个网页
# @Author: 周健平
# @company: 山东大学
# @Time: 2020/7/7 21:21

# beautiful soup提供一些简单的python式的函数用来处理导航、搜索、修改分析树等功能
# 通过解析html文档为用户提供需要抓取的数据
import urllib.request

from bs4 import BeautifulSoup

url = "http://www.baidu.com"
response = urllib.request.urlopen(url)
# bs4库将任何读入的html文件或字符串都转换成UTF-8编码，解析器是使用自带的html.parser，速度慢但通用
# 另外Html5lib可以将不规范的html文本转换为规范的文本再进行解析
# lxml支持HTML和XML的解析，支持XPath解析方式，效率高但是只会局部遍历
soup = BeautifulSoup(response, 'html.parser')
# prettify会以html格式输出
print(soup.prettify())
