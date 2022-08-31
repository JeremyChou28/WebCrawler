# @description:
# @author:周健平
# @company:山东大学
# @Time:2020/12/20 15:55
import numpy as np
import re

f1 = open('train_in1.txt', 'r', encoding='utf-8')
f2 = open('train_out1.txt', 'r', encoding='utf-8')
# f3=open('trainhebing.txt','a',encoding='utf-8')
f4 = open('test_in1.txt', 'r', encoding='utf-8')
f5 = open('test_out1.txt', 'r', encoding='utf-8')
# f6=open('testhebing.txt','a',encoding='utf-8')
f = open('hebing.txt', 'a', encoding='utf-8')

l1 = f1.readlines()
l2 = f2.readlines()
col1 = []
for k in l1:
    k = k.strip('\n')  # 去掉读取中的换行字符
    col1.append(k)
col2 = []
for k in l2:
    k = k.strip('\n')  # 去掉读取中的换行字符
    col2.append(k)
col = []
l4 = f4.readlines()
l5 = f5.readlines()
col4 = []
for k in l4:
    k = k.strip('\n')  # 去掉读取中的换行字符
    col4.append(k)
col5 = []
for k in l5:
    k = k.strip('\n')  # 去掉读取中的换行字符
    col5.append(k)
# print(len(col1))
# print(len(col2))
for i in range(len(col1)):
    col.append(col1[i] + '；' + col2[i])
for i in range(len(col4)):
    col.append(col4[i] + '；' + col5[i])
# print(col)
for i in range(len(col)):
    f.write("对联" + str(i + 1) + "::" + "author" + "::" + col[i] + '\n')
# def sort(path):
#     w = open(path,'r',encoding='utf-8')
#     l = w.readlines()
#     col=[]
#     for k in l:
#         k = k.strip('\n')  #去掉读取中的换行字符
#         col.append(k)
#     # print(col)
#     for k in col:
#         k = re.split(r'\s+',k)
#         k=''.join(k)
#         f.write(k+'\n')
#     # for m in col:
#     #   print(m)          #一行行的输出结果
# if __name__ == '__main__':
#   path="test_out.txt"
#   sort(path)
