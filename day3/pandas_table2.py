# @description:
# @Author: 周健平
# @company: 山东大学
# @Time: 2020/7/11 20:18
import urllib.request

import pandas as pda

# 2018年世界财富500强排行榜：
url = "http://www.fortunechina.com/fortune500/c/2018-07/19/content_311046.htm"
response = urllib.request.urlopen(url)
contents = pda.read_html(response)[0]
contents.to_csv('RankCompanyMoney.csv', encoding="utf_8_sig")
print(contents)
