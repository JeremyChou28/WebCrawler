# @description:urllib.request发送http请求
# @Author: 周健平
# @company: 山东大学
# @Time: 2020/7/7 16:42
import urllib.request

url = "http://www.baidu.com"
response = urllib.request.urlopen(url)
print(response.read())
