# @description:beautiful soup学习
# @Author: 周健平
# @company: 山东大学
# @Time: 2020/7/12 8:57
from bs4 import BeautifulSoup

# 针对gbk' codec can't decode byte 0xbf in position 2: illegal multibyte sequence的报错
# 由于文档是UTF-8编码，但是读取默认是用的gbk，因此要加上encoding='utf-8'
# 在open函数中加入参数'rb'
# soup = BeautifulSoup( open( "E:\HTML5_files\selectors.html" , 'rb' ) , 'html.parser' )
soup = BeautifulSoup(open("E:\HTML5_files\selectors.html", encoding='utf-8'), 'html.parser')
# soup = BeautifulSoup( "<html>data</html>" , 'html.parser' )
# 读取出来的是html的DOM树形式，不是纯文本
print(soup.prettify())
