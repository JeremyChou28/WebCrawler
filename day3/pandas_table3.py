# @description:
# @Author: 周健平
# @company: 山东大学
# @Time: 2020/7/11 18:41
import urllib.request

import pandas as pda

# QS世界大学排名
url = "https://ranking.promisingedu.com/qs"

response = urllib.request.urlopen(url)
contents = pda.read_html(response)[0]
contents.to_csv('RankCollege.csv', encoding="utf_8_sig")
print(contents)
