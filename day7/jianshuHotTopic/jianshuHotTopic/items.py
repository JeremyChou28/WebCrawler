# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JianshuhottopicItem( scrapy.Item ):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 定义需要爬取的字段
    collection_name = scrapy.Field( )
    collection_description = scrapy.Field( )
    collection_article_count = scrapy.Field( )
    collection_attention_count = scrapy.Field( )
