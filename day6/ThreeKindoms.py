# @description:利用scrapy爬取三国演义小说
# @Author: 周健平
# @company: 山东大学
# @Time: 2020/7/16 20:12
# 想法就是利用yield和callback迭代
import time

import scrapy

start_time = time.time()


class ThreekindomsSpider(scrapy.Spider):
    name = 'ThreeKindoms'
    url = 'http://www.aixiawx.com'
    start_urls = ['http://www.aixiawx.com/15/15677/9717102.html']
    i = 1

    def parse(self, response):
        f = open('ThreeKindoms.txt', 'a', encoding='UTF-8')
        title = response.xpath('//div[@class="bookname"]/h1/text()').extract()[0]
        contents = response.xpath('//div[@id="content"]').xpath('string(.)').extract()[0]
        f.write(title + '\n')
        f.write(contents + '\n')
        f.write("------------------------------\n")
        print("第" + str(self.i) + "章爬取完毕")
        self.i += 1
        f.close()

        if self.i != 175:
            next_url = response.css('div.bottem2 a::attr(href)').extract()[3]
            next_url = self.url + next_url
            yield scrapy.Request(next_url, callback=self.parse)
        else:
            end_time = time.time()
            spend_time = end_time - start_time
            print("程序运行了%.2f秒" % spend_time)
