# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DaomuPipeline(object):
    def process_item(self, item, spider):
        print('*********************')
        print(item['juan_name'])
        print(item['zh_number'])
        print(item['zh_name'])
        print(item['zh_link'])
        print(item['zh_content'])
        print('*********************')

        # 定义文件名称：卷名－章节数－章节名.txt
        filename = '{}-{}-{}.txt'.format(
            item['juan_name'],
            item['zh_number'],
            item['zh_name']
        )
        f = open('/home/tarena/daomu/%s' % filename,'w')
        f.write(item['zh_content'])
        f.close()

        return item












