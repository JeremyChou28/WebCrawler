# @description:beautiful soup爬取url
# @Author: 周健平
# @company: 山东大学
# @Time: 2020/7/12 10:07

# 输出第一个a标签
# print(soup.a)
# 输出所有的a标签，以列表形式显示
# print(soup.find_all('a'))
# 输出所有的a标签中的url，锚文本
# for link in soup.find_all('a'):
#     print(link.get('href'))
#     print(link.text)
import urllib.request

from bs4 import BeautifulSoup

url = "http://www.aixiawx.com/16/16039/"
response = urllib.request.urlopen(url)

soup = BeautifulSoup(response, 'html5lib')
# find_all方法是所有当前tag的所有tag子节点，并判断是否符合过滤器的条件
for link in soup.find_all('a'):
    # 输出a标签中的url文本
    print(link.get('href'))
    # 输出锚文本
    print(link.text)
    print("------------------")
