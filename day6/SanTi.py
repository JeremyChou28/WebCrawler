# @description:利用scrapy爬取三体小说
# @Author: 周健平
# @company: 山东大学
# @Time: 2020/7/15 20:12
# 想法就是利用yield和callback迭代
import time

import scrapy

start_time = time.time()  # 计算程序运行时间


class SantiPySpider(scrapy.Spider):
    name = 'SanTi'
    url = 'http://www.aixiawx.com'
    start_urls = ['http://www.aixiawx.com/15/15710/9756527.html']
    i = 1

    def parse(self, response):
        # 引入成员变量i来循环新建文件
        filename = 'E:\Python_language\pycharmProjects\Web_Crawler\day6\SanTi_txt\第%d章.txt' % (self.i)
        # 利用w是保证每次会先清空文件已有内容再接着往文件中写内容进去
        f = open(filename, 'w', encoding='UTF-8')
        # 取出h1标签中的内容：每一章的标题，返回的是数组，因此再将数组元素取出
        title = response.xpath('//div[@class="bookname"]/h1/text()').extract()[0]
        # 取出content中的内容，但是由于里面还有其他标签影响，所以采用字符串拼接把文本连接起来
        # 如果单纯用contents = response.xpath( '//div[@id="content"]' ).extract( )[0]取出的是html的DOM数
        # 而用contents = response.xpath( '//div[@id="content"]/text()' ).extract( )[0]只能取出第一个标签中间的内容
        contents = response.xpath('//div[@id="content"]').xpath('string(.)').extract()[0]
        f.write(title + '\n')
        f.write(contents)
        print("第" + str(self.i) + "章爬取完毕")
        self.i += 1
        f.close()
        # 利用成员变量i来判断是否结束，考虑到三体整本小说只有213章，因此设定了这个临界值
        if self.i != 214:
            # 由于下一章的href是通过css提取出来的第四个，而且是相对路径，因此结合起始url构造出下一章的url
            next_page = response.css('div.bottem2 a::attr(href)').extract()[3]
            next_page = self.url + next_page
            '''
            接下来就是爬取下一页或是内容页的秘诀所在：
            scrapy给我们提供了这么一个方法：scrapy.Request()
            这个方法还有许多参数，后面我们慢慢说，这里我们只使用了两个参数
            一个是：我们继续爬取的链接（next_page），这里是下一页链接，当然也可以是内容页
            另一个是：我们要把链接提交给哪一个函数(callback=self.parse)爬取，
            这里是parse函数，也就是本函数,回到parse函数开头，然后爬取完第2页内容
            同时，又提取到第3页的连接，然后，一直循环下去，直到下一页的连接不存在位置
            当然，我们也可以在下面另写一个函数，比如：内容页，专门处理内容页的数据
            经过这么一个函数，下一页链接又提交给了parse，那就可以不断的爬取了，直到不存在下一页
            yield生成器函数，每次调用都从yield这里开始执行
            '''
            yield scrapy.Request(next_page, callback=self.parse)
        else:
            end_time = time.time()
            spend_time = end_time - start_time
            print('程序运行了%.2f秒' % spend_time)
        # if next_page is not None:
        #     next_page = response.urljoin( next_page )
        #     yield scrapy.Request( next_page , callback=self.parse )
