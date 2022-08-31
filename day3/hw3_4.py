# @description:京东商品页面的爬取
# @Author: 周健平
# @company: 山东大学
# @Time: 2020/7/11 16:32
import requests

url = "https://item.jd.com/100011333796.html#crumb-wrap"
try:
    # 更改头部信息，模拟浏览器访问
    kv = {'user-agent': 'Mozilla/5.0'}
    r = requests.get(url, headers=kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text)
except:
    print("爬取失败")
