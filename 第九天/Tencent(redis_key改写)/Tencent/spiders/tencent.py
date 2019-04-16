# -*- coding: utf-8 -*-
import scrapy
from Tencent.items import TencentItem
from scrapy_redis.spiders import RedisSpider

class TencentSpider(RedisSpider):
    name = 'tencent'
    allowed_domains = ['hr.tencent.com']
    # 把start_urls去掉,使用redis_key控制爬虫
    redis_key = 'tencentspider:start_urls'

    baseurl = 'https://hr.tencent.com/position.php?start='

    def parse(self, response):
        #　把所有页的URL地址交给调度器
        for page in range(0,2001,10):
            url = self.baseurl + str(page)
            yield scrapy.Request(
                    url,
                    callback=self.parse_one_link
                )
    # 一级页面解析函数
    def parse_one_link(self,response):
        # 基准xpath,匹配节点对象列表
        job_list = response.xpath('//tr[@class="even"] | //tr[@class="odd"]')
        # 依次遍历每个职位对象
        for job in job_list:
            # 创建item对象
            item = TencentItem()
            item['zh_name'] = job.xpath('./td[1]/a/text()').extract()[0]
            # 因为有的职位类别不存在
            item['zh_type'] = job.xpath('./td[2]/text()').extract()
            if item['zh_type']:
                item['zh_type'] = item['zh_type'][0]
            else:
                item['zh_type'] = '无'

            item['zh_number'] = job.xpath('./td[3]/text()').extract()[0]
            item['zh_address'] = job.xpath('./td[4]/text()').extract()[0]
            item['zh_time'] = job.xpath('./td[5]/text()').extract()[0]
            item['zh_link'] = 'https://hr.tencent.com/' + \
                       job.xpath('./td[1]/a/@href').extract()[0]

            yield scrapy.Request(
                    item['zh_link'],
                    meta={'item':item},
                    callback=self.parse_two_link
                )
    # 解析二级页面的函数
    def parse_two_link(self,response):
        item = response.meta['item']
        # 基准xpath,匹配工作职责和要求的两个节点对象
        duty_list = response.xpath('//tr[@class="c"]/td/ul[@class="squareli"]')
        # 工作职责
        job_duty = '\n'.join(duty_list[0].xpath('.//li/text()').extract())
        # 工作要求
        job_requirement = '\n'.join(duty_list[1].xpath('.//li/text()').extract())
        item['zh_duty'] = job_duty
        item['zh_requirement'] = job_requirement

        yield item
# //tr[@class="c"]/td/ul[@class="squareli"]
# '\n'.join(L[0].xpath('.//li/text()').extract())
# '\n'.join(L[1].xpath('.//li/text()').extract())




















