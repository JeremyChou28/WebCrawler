# @description:URL的筛选
# @Author: 周健平
# @company: 山东大学
# @Time: 2020/7/12 10:18
import re
import urllib.request

from bs4 import BeautifulSoup

url = "http://www.aixiawx.com/16/16039"
response = urllib.request.urlopen(url)

soup = BeautifulSoup(response, 'html.parser')
# 输出网页带a标签
# print( soup.a )
# 输出庆余年小说所有目录
i = 0
for link in soup.find_all('a'):
    href = link.get('href')
    # 将正则表达式编译为正则表达式对象
    r2 = re.compile('/16/16039/1', re.I)

    if r2.search(href):
        # 输出a标签中的url文本
        i += 1
        print(link.get('href'))
        # 输出锚文本
        print(link.text)
print(i)
