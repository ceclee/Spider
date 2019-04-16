# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# 导入scrapy已经写好的图片管道类
from scrapy.pipelines.images import ImagesPipeline
import scrapy

class SoPipeline(ImagesPipeline):
    # 重写ImagesPipeline中的方法
    def get_media_requests(self, item, info):
        # 把图片链接交给调度器
        yield scrapy.Request(item['img_link'])











