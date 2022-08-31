# @description:通过递归调用parse来爬取多个网页实例--爬取糗事百科网
# @Author: 周健平
# @company: 山东大学
# @Time: 2020/7/15 22:59
import time

import scrapy

start_time = time.time( )


# 需要在settings.py文件中设置user-agent请求头，单独的爬虫文件无法爬取，会出现下述报错
#  [<twisted.python.failure.Failure twisted.internet.error.ConnectionDone: Connection was c
# losed cleanly.>]
class QiushispiderSpider( scrapy.Spider ):
    name = 'QiuShiSpider'
    start_urls = ['https://www.qiushibaike.com/text/']
    # 设计url模板
    url = 'https://www.qiushibaike.com/text/page/%d/'
    pageNum = 1

    def parse( self , response ):
        content_list = response.xpath( '//div[@class="content"]' ).xpath( 'string(.)' ).extract( )
        f = open( 'QiuShiBaiKe.txt' , 'a' , encoding='utf-8' )
        for content in content_list:
            f.write( content )
        f.write( "=========================================================" )
        f.close( )

        if self.pageNum <= 13:
            print( "第%d页爬取完成" % self.pageNum )
            self.pageNum += 1
            new_url = self.url % self.pageNum
            yield scrapy.Request( new_url , callback=self.parse )
        else:
            end_time = time.time( )
            spend_time = end_time - start_time
            print( "爬取完毕，程序运行了%.2f秒" % spend_time )
