# -*- coding: utf-8 -*-
import scrapy


class MiddleSpider(scrapy.Spider):
    name = 'middle'
    allowed_domains = ['www.baidu.com']
    start_urls = ['http://baidu.com/']

    def parse(self, response):
        print('我是parse函数的输出')












