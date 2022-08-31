# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FirstspiderItem( scrapy.Item ):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field( )  # 标题字段
    content = scrapy.Field( )  # 正文字段
    name = scrapy.Field( )  # 网站名称字段
    pass
