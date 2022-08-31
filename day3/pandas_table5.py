# @description:
# @Author: 周健平
# @company: 山东大学
# @Time: 2020/7/11 20:26

import pandas as pd

for i in range(1, 20):  # 爬取19页数据
    url = 'http://s.askci.com/stock/a/?reportTime=2017-12-31&pageNum=%s' % (str(i))
    tb = pd.read_html(url)[3]  # 经观察发现所需表格是网页中第4个表格，故为[3]
    tb.to_csv('stock.csv', mode='a', encoding='utf_8_sig', header=1, index=0)
    print('第' + str(i) + '页抓取完成')
