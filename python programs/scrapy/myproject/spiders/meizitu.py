# -*- coding: utf-8 -*-
import scrapy
from myproject.items import MeizituItem
from scrapy.loader import ItemLoader, Identity
from twisted.internet import reactor

reactor.suggestThreadPoolSize(30)

class MeiziSpider(scrapy.Spider):
    name = "meizi"
    allowed_domains = ["meizitu.com"]
    start_urls = (
        'http://www.meizitu.com/a/list_1_1.html',
    )

    def parse(self, response):
            for link in response.xpath('//*[@id="maincontent"]/div[1]/ul/li//@href').extract():
                

                request = scrapy.Request(link, callback=self.parse_item)
                yield request
            #获取页码集合
            pages = response.xpath('//*[@id="wp_page_numbers"]/ul/li/a/@href').extract()
            print('pages: %s' % pages)#打印页码
            if len(pages) > 2:#如果页码集合>2
                
                page_link = pages[-2]#图片连接=读取页码集合的倒数第二个页码
                page_link = page_link.replace('/a/', '')#图片连接=page_link（a替换成空）
                request = scrapy.Request('http://www.meizitu.com/a/%s' % page_link, callback=self.parse)
                yield request#返回请求


    def parse_item(self, response):
        #l=用ItemLoader载入MeizituItem()
        l = ItemLoader(item=MeizituItem(), response=response)



        #名字
        
        l.add_xpath('name', '//h2/a/text()')
        
        #图片连接
        l.add_xpath('image_urls', '//*[@id="picture"]/p/img/@src', Identity())
        #url
        l.add_value('url', response.url)

        
        return l.load_item()
