# @description:通过递归调用parse来爬取多个网页实例--爬取名言
# @Author: 周健平
# @company: 山东大学
# @Time: 2020/7/17 10:51
import time

import scrapy

start_time = time.time()

# 清空原来文件所有内容并返回
f = open('callbackParse2.txt', 'w', encoding='utf-8')
f.close()


class Callbackparse2Spider(scrapy.Spider):
    # 文件名和name必须相同，否则找不到爬虫文件
    name = 'callbackParse2'
    start_urls = ['http://lab.scrapyd.cn']
    # 设计url模板
    url = 'http://lab.scrapyd.cn/page/%d/'
    pageNum = 1

    def parse(self, response):
        f = open('callbackParse2.txt', 'a', encoding='utf-8')
        contents = response.xpath('//div[@class="quote post"]').xpath('string(.)').extract()
        for content in contents:
            f.write(content)
        f.write(
            "======================    n   、                                                           =================")
        f.close()
        print("第%d页爬取完成" % self.pageNum)
        if self.pageNum <= 5:
            self.pageNum += 1
            new_url = self.url % self.pageNum
            yield scrapy.Request(new_url, callback=self.parse)
        else:
            end_time = time.time()
            spend_time = end_time - start_time
            print("爬取完毕，程序运行了%.2f秒" % spend_time)
