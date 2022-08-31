# @description:通过占位符构造通用URL来爬取多个网页实例--爬取麦田租房网站房源信息,存在被封爬取不了的可能
# @Author: 周健平
# @company: 山东大学
# @Time: 2020/7/15 21:54
import time

import scrapy

start_time = time.time()


class MaitianzfallSpider(scrapy.Spider):
    name = 'fallInformation'

    start_urls = ['http://bj.maitian.cn/zfall/PG{}'.format(page) for page in range(100)]
    # start_urls = ['http://bj.maitian.cn/zfall/PG{}'.format( page ) for page in range( 3 )]

    pageNum = 1

    def parse(self, response):
        f = open('FallInformation.txt', 'a', encoding='utf-8')
        # 得到租房信息的第一条关于房间类型的
        fall_information1 = response.xpath('//div[@class="list_title"]/h1/a/text()').extract()
        fall_information2 = response.xpath('//div[@class="list_title"]/p').xpath('string(.)').extract()
        for i in range(len(fall_information1)):
            fall_information = fall_information1[i] + fall_information2[i]
            f.write(fall_information)
        f.write("================================================")
        f.close()
        print("第%d页爬取完成" % self.pageNum)
        self.pageNum += 1
        if self.pageNum == 100:
            end_time = time.time()
            spend_time = end_time - start_time
            print("爬取完毕，程序运行了%.2f秒" % spend_time)
