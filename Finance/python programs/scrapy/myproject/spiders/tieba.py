# -*- coding: utf-8 -*-
import scrapy
from myproject.items import MeizituItem
from scrapy.loader import ItemLoader, Identity
from twisted.internet import reactor

reactor.suggestThreadPoolSize(30)

class MeiziSpider(scrapy.Spider):
    name = "tieba"
    allowed_domains = ["tieba.baidu.com"]
    start_urls = (
        'http://tieba.baidu.com/f?ie=utf-8&kw=%E9%BB%91%E4%B8%9D',
    )

    def parse(self, response):
            for link in response.xpath('//*[@id="thread_list"]/li/div/div/div/div/a/@href').extract():
                link = 'http://tieba.baidu.com/'+ link
                request = scrapy.Request(link, callback=self.parse_item)
                yield request
            #获取页码集合
            pages = response.xpath('//*[@id="wp_page_numbers"]/ul/li/a/@href').extract()
            print('pages: %s' % pages)#打印页码
            page_link = response.xpath('//*[@id="frs_list_pager"]/a/@href').extract()[-2]

            request = scrapy.Request(page_link, callback=self.parse)
            yield request#返回请求


    def parse_item(self, response):
        #l=用ItemLoader载入MeizituItem()
        l = ItemLoader(item=MeizituItem(), response=response)



        #名字
        
        l.add_xpath('name', '//h3/@title')
        
        #图片连接
        l.add_xpath('image_urls', '//img[@class="BDE_Image"]/@src', Identity())
        #url
        l.add_value('url', response.url)

        
        return l.load_item()
