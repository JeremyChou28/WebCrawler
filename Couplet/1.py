# @description:
# @author:周健平
# @company:山东大学
# @Time:2020/12/20 15:01
import urllib.request

from bs4 import BeautifulSoup

filename = "Couplet.txt"  # 文本文件名
f = open(filename, 'w+', encoding='UTF-8')

url = 'https://www.lz13.cn/lizhikouhao/59331.html'  # 爬取的网页url
response = urllib.request.urlopen(url)  # 读取网页
soup = BeautifulSoup(response, 'html5lib')  # 美丽汤解析

contents = soup.find_all('p')  # 找到所有p标签
contents = contents[1:-1:1]  # 剔除无用p标签
for i in contents:
    f.write(i.text + '\n')  # 提取p标签中的文本
print("爬取完毕")
