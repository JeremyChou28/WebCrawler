# @description:scrapy框架爬虫文件
# @Author: 周健平
# @company: 山东大学
# @Time: 2020/7/12 15:09
import scrapy

from firstSpider.items import FirstspiderItem


class NovelSpiderSpider( scrapy.Spider ):
    name = 'novelspider'  # 唯一定位实例的属性，必须唯一
    allowed_domains = ['aixiawx']  # 允许爬虫爬取的域名列表，不设置表示允许爬取所有
    start_urls = ['http://www.aixiawx.com/15/15575/9642539.html']  # 起始爬取列表，可以是多个url

    # 在parse方法中做数据的提取，回调函数，处理response并返回处理后的数据和需要跟进的url
    # 使用Xpath，从页面的html source里面选取需要抽取的数据
    # scrapy shell分析目标网页有四个方法，都是内置的选择器，不需要导入第三方包。
    # xpath()返回该表达式所对应的所有节点的selector list选择器列表，从而筛选需要定位的元素
    # css()返回该表达式所对应的所有节点的selector list选择器列表，语法和bs4类似
    # re()正则表达式，对数据进行提取，返回unicode字符串list列表
    # extract()序列化节点为unicode字符串，并返回list列表
    def parse( self , response ):
        item = FirstspiderItem( )
        item['title'] = response.xpath( "/html/head/title" ).extract( )
        item['content'] = response.xpath( '//div[@id="content"]/text()' ).extract( )
        item['name'] = response.xpath( '//div[@class="header_logo"]' ).extract( )
        # print( item )
        yield item
# 项目运行爬虫文件，只需要进入项目文件夹后，运行scrapy crawl firstspider即可，不要加上.py后缀名
# 使用scrapy crawl novelspider -o novelspider.csv -t csv转换后打开csv需要先用editplus修改编码方式为ANSI再用excel打开查看
