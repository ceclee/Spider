# -*- coding: utf-8 -*-
import scrapy
from Csdn.items import CsdnItem

class CsdnSpider(scrapy.Spider):
    name = 'csdn'
    allowed_domains = ['blog.csdn.net']
    start_urls = ['https://blog.csdn.net/java123456789010/article/details/89061997']

    def parse(self, response):
        # 创建item对象
        item = CsdnItem()

        item['title'] = response.xpath('//h1[@class="title-article"]/text()').extract()[0]
        item['time'] = response.xpath('//span[@class="time"]/text()').extract()[0]
        item['number'] = response.xpath('//span[@class="read-count"]/text()').extract()[0]
        # 把item交给了管道文件
        yield item















