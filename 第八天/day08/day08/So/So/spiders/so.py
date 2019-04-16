# -*- coding: utf-8 -*-
import scrapy
from urllib import parse
import json
from So.items import SoItem

class SoSpider(scrapy.Spider):
    name = 'so'
    allowed_domains = ['image.so.com']
    # 重写start_requests()方法,自定义URL地址和解析方法
    # 不一定非得是parse函数
    # 构造请求,去交给调度器
    def start_requests(self):
        # 拼接URL地址
        baseurl = 'http://image.so.com/zj?'
        for i in range(0,301,30):
            params = {
                'ch' : 'beauty',
                'sn' : str(i),
                'listtype' : 'new',
                'temp' : '1'
            }
            url = baseurl + parse.urlencode(params)
            # 构造请求,交给调度器
            yield scrapy.Request(url,callback=self.parse_so)

    # 定义解析函数
    def parse_so(self,response):
        # 获取响应内容
        html = response.text
        # 内容为json,转为python数据类型
        html = json.loads(html)
        for img in html['list']:
            # 创建item对象
            item = SoItem()
            item['img_link'] = img['qhimg_url']
            # 交给管道
            yield item













