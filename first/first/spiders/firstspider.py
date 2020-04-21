# -*- coding: utf-8 -*-
import scrapy
from first.items import FirstItem

class FirstspiderSpider(scrapy.Spider):
    name = 'firstspider'
    allowed_domains = ['codeup.cn']
#    start_urls = ['http://codeup.cn/']

    """
    功能：爬取腾讯社招信息
    """
   
    url = "http://codeup.cn/status.php?&top="
    offset = 1809410
    # 起始url
    start_urls = [url + str(offset)]
    def parse(self, response):
        for each in response.xpath("//tr[@class='evenrow'] | //tr[@class='oddrow']"):
            # 初始化模型对象
            item = FirstItem()
            # 职位名称
            item['runid'] = each.xpath("./td[1]/text()").extract()[0]
            # 详情连接
            item['username'] = each.xpath("./td[2]/a/text()").extract()[0]
            # 职位类别
            
            item['problem_id'] = each.xpath("./td[3]/div/a/text()").extract()[0]
            # 招聘人数
            
            item['result'] =  each.xpath("./td[4]/a/text()").extract()[0]
            # 工作地点
            item['memory'] = each.xpath("./td[5]/div/text()").extract()[0]
            # 发布时间
            item['timer'] = each.xpath("./td[6]/div/text()").extract()[0]
            item['lang'] = each.xpath("./td[7]/text()").extract()[0]
            item['codel'] = each.xpath("./td[8]/text()").extract()[0]
            
            item['sub_time'] = each.xpath("./td[9]/text()").extract()[0]
            
            yield item
        if self.offset < 1809510:
            self.offset += 99
        # 每次处理完一页的数据之后，重新发送下一页页面请求
        # self.offset自增10，同时拼接为新的url，并调用回调函数self.parse处理Response
        yield scrapy.Request(self.url + str(self.offset), callback = self.parse)