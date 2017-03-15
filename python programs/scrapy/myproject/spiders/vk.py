# -*- coding: utf-8 -*-
import scrapy
from myproject.items import MeizituItem
from scrapy.loader import ItemLoader, Identity
from twisted.internet import reactor

reactor.suggestThreadPoolSize(30)

class MeiziSpider(scrapy.Spider):
    name = "vk"
    allowed_domains = ["vk.com"]
    start_urls = (
        'https://m.vk.com/album-69328374_192676001',
    )

    def parse(self, response):
            for link in response.xpath('//*[@class="photos_page thumbs_list"]//@href').extract():
                link = 'https://m.vk.com/'+ link
                

                request = scrapy.Request(link, callback=self.parse_item)
                yield request
            more_link = 'https://m.vk.com/'+ response.xpath('//*[@class="show_more"]/@href').extract()[0]
            request = scrapy.Request(more_link, callback=self.parse)
            yield request


        


    def parse_item(self, response):
        #l=用ItemLoader载入MeizituItem()
        l = ItemLoader(item=MeizituItem(), response=response)


        
        #图片连接
        l.add_xpath('image_urls', '//*[@class="pv_photo_wrap"]//img/@src', Identity())
        #url
        l.add_value('url', response.url)

        
        return l.load_item()

 
