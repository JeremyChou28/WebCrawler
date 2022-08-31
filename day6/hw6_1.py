# @description:scrapy架构学习
# @Author: 周健平
# @company: 山东大学
# @Time: 2020/7/10 10:05
# scrapy的7大架构：Spider(爬虫) SpiderMiddlewares(爬虫中间件) ScrapyEngine(引擎) Scheduler(调度器)
# DownloaderMiddlewares(下载中间件) Downloader(下载器) ItemPipeline(管道)
# scarpy运行流程：
# 通过scrapy创建爬虫，爬虫请求通过爬虫中间件传递给引擎，引擎再将爬虫请求传给调度器入列
# 调度器进行调度选择合适的请求通过下载中间件发送给下载器，下载器根据请求到Internet网络中下载数据并返回给引擎，引擎再将下载器传回的响应通过爬虫中间件传递给爬虫
# 爬虫从网络响应中分析提取Item所需数据，并通过爬虫中间件交给引擎，引擎将Item数据传给管道进行数据存储

# 爬取多个网页，起始爬取列表中可以是存储多个url
# 可以通过分析多个网页之间url的联系和区别，找到循环的方法
# 方法一：通过占位符来构造通用URL
# start_urls = ['http://bj.maitian.cn/zfall/PG{}'.format( page ) for page in range( 1 , 4 )]

# url_prefix="http://.bj.maitian.cn/zfall/PG{}"
# start_urls=[url_prefix.format(i) for i in range(1,4)]
# 方法二：通过重写start_requests方法，获取所有起始的url，不用写start_urls
#     def start_requests(self):
#         pages=[]
#         for page in range(1,4):
#             url='http://bj.maitian.cn/zfall/PG{}'.format(page)
#             page=scrapy.Request(url)
#             pages.append(page)
#         return pages  #返回请求对象的列表
# 方法三：递归调用parse直到每个页面都被爬取完，该方法实例参考mingYan.py
# class MaitianSpider( scrapy.Spider ):
#     name = 'maitian'
#     start_urls = ['http://bj.maitian.cn/zfall/PG']
#     # 设计一个url模板
#     url = 'http://bj.maitian.cn/zfall/PG/%d/'
#     pageNum = 1
#
#     def parse( self , response ):
#         div_list = response.xpath( "//div[@id='content-left']/div" )
#         for div in div_list:
#             # 处理将item提交给管道
#             item = SecondspiderItem( )
#             yield item
#         # 多url请求，请求手动发送
#         if self.pageNum <= 13:
#             self.pageNum += 1
#             print( '爬第：%d' % self.pageNum )
#             new_url = self.url % self.pageNum
#         # callback回调函数，页面进行解析
#         yield scrapy.Request( url=new_url , callback=self.parse( ) )
