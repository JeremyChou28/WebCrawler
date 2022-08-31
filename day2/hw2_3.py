# @description:
# @Author: 周健平
# @company: 山东大学
# @Time: 2020/7/7 16:58
import re

pattern = re.compile(r'\d+')
result1 = pattern.findall('runoob 123 google 456')
result2 = pattern.findall('run88oob123google456', 0, 10)
print(result1)
print(result2)
