import scrapy

from jianshuHotTopic.items import JianshuhottopicItem


class JianshuhottopicspiderSpider( scrapy.Spider ):
    # 简书专题数据爬取，获取url地址中特定的子段信息
    name = 'jianshuHotTopicSpider'
    start_urls = ["https://www.jianshu.com/recommendations/collections"]

    # https: // www.jianshu.com / recommendations / collections?page = 2 & order_by = hot
    # https: // www.jianshu.com / recommendations / collections?page = 2 & order_by = city

    def parse( self , response ):
        # @params:response,提取response中特定字段信息
        item = JianshuhottopicItem( )

        selector = scrapy.Selector( response )

        collections = selector.xpath( '//div[@class="col-xs-8"]' )

        for collection in collections:
            collection_name = collection.xpath( 'div/a/h4/text()' ).extract( )[0].strip( )

            collection_description = collection.xpath( 'div/a/p/text()' ).extract( )[0].strip( )

            collection_article_count = collection.xpath( 'div/div/a/text()' ).extract( )[0].strip( ).replace( '篇文章' ,
                                                                                                              '' )

            collection_attention_count = collection.xpath( 'div/div/text()' ).extract( )[0].strip( ).replace( "人关注" ,
                                                                                                              '' ).replace(
                "· " , '' )

            item['collection_name'] = collection_name

            item['collection_description'] = collection_description

            item['collection_article_count'] = collection_article_count

            item['collection_attention_count'] = collection_attention_count

            yield item

        # urls = ['https://www.jianshu.com/recommendations/collections?page={}&order_by=hot'.format( str( i ) ) for i in
        #         range( 3 , 11 )]
        #
        # for url in urls:
        #     sleep( random.randint( 2 , 7 ) )
        #
        #     yield scrapy.Request( url , callback=self.parse )
