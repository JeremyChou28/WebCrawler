# @description:
# @Author: 周健平
# @company: 山东大学
# @Time: 2020/7/11 18:29
import requests

keyword = "山东大学信息科学与工程学院"
try:
    kv = {'wd': keyword}
    r = requests.get("http://www.baidu.com/s", params=kv)
    print(r.request.url)
    r.raise_for_status()
    print(len(r.text))
except:
    print("爬取失败")
