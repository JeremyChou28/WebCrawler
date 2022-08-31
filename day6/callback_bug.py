# @description:通过递归调用parse来爬取多个网页实例--爬取名言
# @Author: 周健平
# @company: 山东大学
# @Time: 2020/7/15 22:59
import time

import scrapy

start_time = time.time()
# 清空文件中已有内容
f = open('callbackParse2.txt', 'w', encoding='utf-8')
f.close()


class CallbackBugSpider(scrapy.Spider):
    name = 'callback_bug'
    start_urls = ['http://lab.scrapyd.cn']
    # 设计url模板
    url = 'http://lab.scrapyd.cn/page/{}/'
    pageNum = 1

    # 一直会报404请求错误,真是瞎了眼，url复制错了http://lab.scrapyd.cn/text/page/{}/
    # 而应该是http://lab.scrapyd.cn/page/{}/

    def parse(self, response):
        f = open('callbackParse2.txt', 'a', encoding='utf-8')
        contents = response.xpath('//div[@class="quote post"]').xpath('string(.)').extract()
        for content in contents:
            f.write(content)
        f.write("=================================================")
        f.close()
        print("第%d页爬取完成" % self.pageNum)
        if self.pageNum <= 5:
            self.pageNum += 1
            new_url = self.url.format(self.pageNum)
            yield scrapy.Request(new_url, callback=self.parse)
        else:
            end_time = time.time()
            spend_time = end_time - start_time
            print("爬取完毕，程序运行了%.2f秒" % spend_time)
