# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CsdnItem(scrapy.Item):
    # define the fields for your item here like:
    # 定义爬取的数据结构,后期给爬虫文件做铺垫
    # 标题
    title = scrapy.Field()
    # 时间
    time = scrapy.Field()
    # 数量
    number = scrapy.Field()










