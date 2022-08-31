# @description:通过重写start_requests方法获取所有的起始url实例--爬取名言
# @Author: 周健平
# @company: 山东大学
# @Time: 2020/7/15 22:57
import time

import scrapy

start_time = time.time()


# 清空原来文件所有内容并返回
def read_account(filename):
    with open(filename, 'r+', encoding='utf-8') as f:
        res = f.readlines()
        print(res)
        f.seek(0)
        f.truncate()


read_account('mingYan1_StartRequest_txt.txt')


class StartRequest(scrapy.Spider):
    name = 'StartRequest'
    # 通过重写start_requests方法，获取所有的起始url，而不用再写start_urls
    # start_urls = ['http://lab.scrapyd.cn/page/{}/'.format( page ) for page in range( 1 , 7 )]
    index = 0

    # pages相当于是存放了多个起始url的请求对象的列表
    def start_requests(self):
        pages = []
        for page in range(1, 7):
            url = 'http://lab.scrapyd.cn/page/{}/'.format(page)
            # page变成了url对应的请求对象
            page = scrapy.Request(url)
            print(page)
            pages.append(page)
        return pages

    def parse(self, response):
        # 爬取出每页的名言正文内容
        f = open('mingYan1_StartRequest_txt.txt', 'a', encoding='utf-8')
        contents = response.xpath('//div[@class="quote post"]').xpath('string(.)').extract()
        for i in range(len(contents)):
            f.write(contents[i])
            # 把每页的五条名言依次写入文本中
        f.write("-----------------------------")
        self.index += 1
        f.close()
        if self.index == 6:
            end_time = time.time()
            spend_time = end_time - start_time
            print("程序运行了%.2f秒" % spend_time)
