# @description:
# @Author: 周健平
# @company: 山东大学
# @Time: 2020/7/7 17:07
import urllib.request

import pandas as pda

url = "http://www.maigoo.com/news/463071.html"
response = urllib.request.urlopen(url)
contents = pda.read_html(response)[0]
mingCi = contents[0]
name = contents[1]
profit = contents[2]
print(f"{mingCi[0]}\t{' ' * 2}\t{name[0]}\t{' ' * 10}\t{profit[0]}")
for i in range(1, len(contents[0])):
    print(f"{mingCi[i]}\t{' ' * 2}\t{name[i]}\t{' ' * 10}\t{profit[i]}")
