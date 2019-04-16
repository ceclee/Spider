# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
import pymysql
from .settings import *


class TencentPipeline(object):
    def process_item(self, item, spider):
        print(dict(item))
        return item

# 定义存到mongo的管道类
class TencentMongoPipeline(object):
    def __init__(self):
        # 创建三个对象
        self.conn = pymongo.MongoClient(
            MONGO_HOST,MONGO_PORT
        )
        self.db = self.conn[MONGO_DB]
        self.myset = self.db[MONGO_SET]

    def process_item(self,item,spider):
        # 把item转为字典,进行数据库插入
        d = dict(item)
        self.myset.insert_one(d)

        return item

    # 爬虫程序结束时执行的函数
    def close_spider(self,spider):
        print('执行了close_spider函数')


# 新建存入到mysql的管道类
class TencentMysqlPipeline(object):
    def __init__(self):
        # 创建2个对象
        self.db = pymysql.connect(
            MYSQL_HOST,MYSQL_USER,MYSQL_PWD,
            MYSQL_DB,charset=MYSQL_CHAR
        )
        self.cursor = self.db.cursor()

    def process_item(self,item,spider):
        ins = 'insert into tencentset values(%s,%s,%s,%s)'
        L = [
                item['zh_name'].strip(),
                item['zh_type'].strip(),
                item['zh_address'].strip(),
                int(item['zh_number'].strip())
        ]
        self.cursor.execute(ins,L)
        self.db.commit()
        return item

    # 爬虫结束时执行此函数(收尾工作)
    def close_spider(self,spider):
        self.cursor.close()
        self.db.close()





