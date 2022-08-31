import numpy as np
import re
f=open('train_in1.txt','a',encoding='utf-8')
def sort(path):
    w = open(path,'r',encoding='utf-8')
    l = w.readlines()
    col=[]
    for k in l:
        k = k.strip('\n')  #去掉读取中的换行字符
        col.append(k)
    # print(col)
    for k in col:
        k = re.split(r'\s+',k)
        k=''.join(k)
        f.write(k+'\n')
    # for m in col:
    #   print(m)          #一行行的输出结果
if __name__ == '__main__':
  path="train_in.txt"
  sort(path)
