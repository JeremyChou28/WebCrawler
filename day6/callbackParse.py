# @description:通过递归调用parse来爬取多个网页实例--爬取糗事百科网
# @Author: 周健平
# @company: 山东大学
# @Time: 2020/7/15 22:59
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


read_account('QiuShiBaiKe.txt')


# 本例存在问题：下载中间件缺少请求头，单独的爬虫文件无法爬取
# 增加请求头，重写start_requests方法解决
class QiuShiSpider(scrapy.Spider):
    name = 'callbackParse'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/text/']
    url = 'https://www.qiushibaike.com/text/page/%d/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'gzip, deflate, br',
        'Connection': 'keep-alive'
    }
    pageNum = 1

    def start_requests(self):
        for i in range(1, 14):
            url = self.url % i
            # 注意回调函数callback=self.parse这里的parse后面是不带括号的
            yield scrapy.Request(url, headers=self.headers, callback=self.parse)

    def parse(self, response):
        content_list = response.xpath('//div[@class="content"]').xpath('string(.)').extract()
        f = open('QiuShiBaiKe.txt', 'a', encoding='utf-8')
        for i in range(len(content_list)):
            f.write(content_list[i])
        f.write("====================================================================")
        f.close()
        print("第%d页爬取完成" % self.pageNum)
        self.pageNum += 1
        if self.pageNum == 14:
            end_time = time.time()
            spend_time = end_time - start_time
            print("爬取完毕，程序运行了%.2f秒" % spend_time)

        # if self.pageNum <= 13:
        #     print( "第%d页爬取完成" % self.pageNum )
        #     self.pageNum += 1
        #     new_url = self.url % self.pageNum
        #     yield scrapy.Request( new_url , headers=self.headers , callback=self.parse )
        # else:
        #     end_time = time.time( )
        #     spend_time = end_time - start_time
        #     print( "爬取完毕，程序运行了%.2f秒" % spend_time )
