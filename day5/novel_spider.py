# @description:scrapy框架生成文件
# @Author: 周健平
# @company: 山东大学
# @Time: 2020/7/12 13:09
# --------------------------------------
# scrapy的选择器Xpath
# --------------------------------------
# / 绝对路径 从根节点开始
# /html/body/form/input     查找html下的body下的form下的所有input节点
# --------------------------------------
# // 相对路径
# //input   查找所有的input节点
# --------------------------------------
# 通配符*选择未知的节点
# //form/*      查找form节点下的所有节点
# //*       查找所有节点
# //*/input     查找所有input节点（input至少有爷爷辈节点，也就是input为第三层的节点）
# --------------------------------------
# 选择id/class 加上@属性符
# --------------------------------------
# //input[@name]    定位所有包含name属性的input节点
# //input[@*]       定位所有含有属性的input节点
# //input[@value='2']       定位所有value=2的input节点
# //div[@id]        定位所有拥有id名的属性的div元素
# //div[@class='eng']       定位所有拥有eng的class属性的div元素
# --------------------------------------
# 使用便捷的函数来增强定位的准确性
# --------------------------------------
# //a[contains(@href,'promote.html')]       定位href属性中包含promote.html的所有a节点
# //a[text()='应用推广']     定位元素内的文本为 应用推广 的所有a节点
# //a[starts-with(@href,'ads')]     定位href属性值是以ads开头的所有a节点
# --------------------------------------
import scrapy


class NovelSpiderSpider(scrapy.Spider):
    name = 'novel_spider'  # 唯一定位实例的属性，必须唯一
    # allowed_domains = ['aixiawx']  # 允许爬虫爬取的域名列表，不设置表示允许爬取所有
    start_urls = ['http://faculty.sdu.edu.cn/xionghailiang/zh_CN/index.htm']  # 起始爬取列表，可以是多个url

    # 在parse方法中做数据的提取，回调函数，处理response并返回处理后的数据和需要跟进的url
    # 使用Xpath，从页面的html source里面选取需要抽取的数据
    # scrapy shell分析目标网页有四个方法，都是内置的选择器，不需要导入第三方包。
    # xpath()返回该表达式所对应的所有节点的selector list选择器列表，从而筛选需要定位的元素
    # css()返回该表达式所对应的所有节点的selector list选择器列表，语法和bs4类似
    # re()正则表达式，对数据进行提取，返回unicode字符串list列表
    # extract()序列化节点为unicode字符串，并返回list列表
    def parse(self, response):
        data = response.xpath('//div[@class="t_jbxx_nr"]').extract()
        print(data)
        pass
# scrapy runspider novel_spider.py全局命令运行，需要进入后文件所在目录下运行，必须加上.py后缀名
