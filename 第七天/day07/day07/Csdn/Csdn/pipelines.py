# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class CsdnPipeline(object):
    # 必须有１个函数名叫:process_item
    def process_item(self, item, spider):
        print('************************')
        print(item['title'])
        print(item['time'])
        print(item['number'])
        print('************************')

        return item













