# @description:
# @Author: 周健平
# @company: 山东大学
# @Time: 2020/7/11 19:00
import urllib.request

import pandas as pda

# IMDB世界电影票房排行榜：
url = "https://www.boxofficemojo.com/"
response = urllib.request.urlopen(url)
contents = pda.read_html(response)[0]
contents.to_csv('RankMovie.csv', encoding="utf_8_sig")
print(contents)
