# @description:百度搜索关键词的提交
# @Author: 周健平
# @company: 山东大学
# @Time: 2020/7/11 17:19
import requests

keyword = "Python"
try:
    kv = {'wd': keyword}
    r = requests.get("http://www.baidu.com/s", params=kv)
    print(r.request.url)
    r.raise_for_status()
    print(len(r.text))
except:
    print("爬取失败")
