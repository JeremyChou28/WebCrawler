# @description:
# @Author: 周健平
# @company: 山东大学
# @Time: 2020/7/7 16:47
import urllib.request

url = "file:///E:\HTML5_files/css样式.html"
response = urllib.request.urlopen(url)
print(response.read())
