# @description:
# @author:周健平
# @company:山东大学
# @Time:2020/12/21 10:19
import urllib.request

from bs4 import BeautifulSoup

filename = "biansaiPoem.txt"
f = open(filename, 'w+', encoding='UTF-8')

url = 'http://www.bookasia.cn/songci/34458.html'
response = urllib.request.urlopen(url)
soup = BeautifulSoup(response, 'html5lib')

idcontents = soup.find(id='artContent')
contents = idcontents.find_all('p')
# contents=contents[1:-1:1]
for i in contents:
    f.write(i.text + '\n')
print("爬取完毕")
