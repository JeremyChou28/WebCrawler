# @description:
# @Author: 周健平
# @company: 山东大学
# @Time: 2020/7/7 17:01
import urllib.request

import pandas as pda

url = "http://www.maigoo.com/news/463071.html"
response = urllib.request.urlopen(url)
contents = pda.read_html(response)
print(contents[0])
