# @description:
# @Author: 周健平
# @company: 山东大学
# @Time: 2020/7/11 21:44
from urllib.parse import urlencode

import pandas as pd
import requests
from bs4 import BeautifulSoup
from requests import RequestException


def get_one_page(i):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
        }
        paras = {
            'reportTime': '2017-12-31',
            # 可以改报告日期，比如2018-6-30获得的就是该季度的信息
            'pageNum': i  # 页码
        }
        url = 'http://s.askci.com/stock/a/?' + urlencode(paras)
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print('爬取失败')


# beatutiful soup解析然后提取表格
def parse_one_page(html):
    soup = BeautifulSoup(html, 'lxml')
    content = soup.select('#myTable04')[0]  # [0]将返回的list改为bs4类型
    tb1 = pd.read_html(content.prettify(), header=0)[0]
    # prettify()优化代码,[0]从pd.read_html返回的list中提取出DataFrame
    tb1.to_csv('RankStock.csv', mode='a', encoding='utf_8_sig', header=1, index=0)
    # tbl.rename(
    #     columns={ '序号': 'serial_number' , '股票代码': 'stock_code' , '股票简称': 'stock_abbre' , '公司名称': 'company_name' ,
    #               '省份': 'province' , '城市': 'city' , '主营业务收入(201712)': 'main_bussiness_income' ,
    #               '净利润(201712)': 'net_profit' , '员工人数': 'employees' , '上市日期': 'listing_date' , '招股书': 'zhaogushu' ,
    #               '公司财报': 'financial_report' , '行业分类': 'industry_classification' , '产品类型': 'industry_type' ,
    #               '主营业务': 'main_business' } , inplace=True )
    # print( tbl )


# return tbl
# rename将表格15列的中文名改为英文名，便于存储到mysql及后期进行数据分析
# tbl = pd.DataFrame(tbl,dtype = 'object') #dtype可统一修改列格式为文本

# 主函数
def main(page):
    for i in range(1, page):  # page表示提取页数
        html = get_one_page(i)
        parse_one_page(html)
        print("第" + str(i) + "页提取完成")


# 单进程
if __name__ == '__main__':
    main(191)  # 共提取n页
