# @description:爬取http://lab.scrapyd.cn的名言，scrapy爬取多个网页实例
# @Author: 周健平
# @company: 山东大学
# @Time: 2020/7/13 20:49

# 提取http://lab.scrapyd.cn中的五条名言
# 然后接着继续爬取下一页，下一页......
# 作者-语录合集命名保存

import time

import scrapy

start_time = time.time()


# 定义一个mingyan类，继承Spider父类
class NextSpider(scrapy.Spider):
    # 定义蜘蛛名
    name = 'NextSpider'
    start_urls = ['http://lab.scrapyd.cn']

    def parse(self, response):

        # 提取页面中的所有的名言
        # css()返回该表达式所对应的所有节点的selector list选择器列表，语法和bs4类似
        mingyan = response.css('div.quote')

        for v in mingyan:
            # 提取css中text标签对应的文字内容，名言的正文
            text = v.css('.text::text').extract_first()
            # 提取作者
            author = v.css('.author::text').extract_first()
            # 提取标签
            tags = v.css('.tags .tag::text').extract()
            # 数组转换为字符串
            tags = ', '.join(tags)
            # 将爬去的内容存入文件，文件名为：作者-语录.txt
            # 注意可以设置文件保存的路径
            filename = 'E:\Python_language\pycharmProjects\Web_Crawler\day6\mingYan_txt\%s-语录合集.txt' % (author)
            # 以写的方式打开文件并写入内容
            f = open(filename, 'a', encoding='UTF-8')
            f.write(text)
            f.write('\n')
            f.write('标签: ' + tags)
            f.write('\n---------------\n')
            f.close()

        # 上面已经爬取保存完成了第一页的内容
        # 接下来我们先判断下一页是否存在，如果存在
        # 就提交给上面的parse方法继续执行，下面是提交的方法
        # css选择器提取下一页链接，并判断是否有下一页这个链接

        # 第一次实现时extract_first()写成了extrast_first()，未提示拼写错误
        next_page = response.css('li.next a::attr(href)').extract_first()
        if next_page is not None:
            # 第二页链接是http://lab.scrapyd.cn/page/2
            # 第三页链接是http://lab.scrapyd.cn/page/3
            # 如果是相对路径，如：/page/1
            # url.join能替我们转换为绝对路径，也就是加上我们的域名
            # 执行urljoin后我们最终next_page的网址就是http://lab.scrapyd.cn/page/2
            next_page = response.urljoin(next_page)

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
            print("程序运行了%.2f秒" % spend_time)
