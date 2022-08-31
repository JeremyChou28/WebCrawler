# @description:
# @Author: 周健平
# @company: 山东大学
# @Time: 2020/7/7 16:55
import re

line = "Cats are smarter than dogs"
searchObj = re.search(r'(.*) are (.*?).*', line, re.M | re.I)
if searchObj:
    print("searchObj.group():", searchObj.group())
    print("searchObj.group(1):", searchObj.group(1))
    print("searchObj.group(2):", searchObj.group(2))
else:
    print("Nothing found!!")
