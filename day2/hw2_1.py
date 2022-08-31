# @description:
# @Author: 周健平
# @company: 山东大学
# @Time: 2020/7/7 16:50
import re

r2 = re.compile('World$', re.I)  # re.I忽略大小写
if r2.search('helloworld\n'):
    print("Search successful")
else:
    print("Search fails")
