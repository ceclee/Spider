# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentItem(scrapy.Item):
    # define the fields for your item here like:
    # 职位名称
    zh_name = scrapy.Field()
    # 职位链接
    zh_link = scrapy.Field()
    # 职位类别
    zh_type = scrapy.Field()
    # 招聘人数
    zh_number = scrapy.Field()
    # 招聘地点
    zh_address = scrapy.Field()
    # 招聘时间
    zh_time = scrapy.Field()
    # 工作职责
    zh_duty = scrapy.Field()
    # 工作要求
    zh_requirement = scrapy.Field()














