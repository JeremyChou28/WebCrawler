# @description:scrapy爬取琅琊榜小说
# @Author: 周健平
# @company: 山东大学
# @Time: 2020/7/15 21:54
import time

import scrapy

start_time = time.time()


class LangyabangPySpider(scrapy.Spider):
    name = 'LangYaBang.py'
    start_urls = ['http://www.aixiawx.com/15/15733/9788999.html']
    url = 'http://www.aixiawx.com'
    i = 1

    def parse(self, response):
        filename = 'E:\Python_language\pycharmProjects\Web_Crawler\day6\LangYaBang_txt\第%d章.txt' % self.i
        f = open(filename, 'w', encoding='UTF-8')
        title = response.xpath('//div[@class="bookname"]/h1/text()').extract()[0]
        contents = response.xpath('//div[@id="content"]').xpath('string(.)').extract()[0]
        f.write(title + '\n')
        f.write(contents)
        print("第" + str(self.i) + "章爬取完毕")
        self.i += 1
        f.close()

        if self.i != 175:
            next_page = response.css('div.bottem2 a::attr(href)').extract()[3]
            next_page = self.url + next_page
            yield scrapy.Request(next_page, callback=self.parse)
        else:
            endtime = time.time()
            Spendtime = endtime - start_time
            print("程序运行花费了%.2f秒" % Spendtime)
# python计算程序运行的几种方法
# 方法1
# import datetime
# starttime = datetime.datetime.now()
# #long running
# endtime = datetime.datetime.now()
# print (endtime - starttime).seconds
# 方法 2
# start = time.time()
# run_fun()
# end = time.time()
# print end-start
# 方法3
# start = time.clock()
# run_fun()
# end = time.clock()
# print end-start
