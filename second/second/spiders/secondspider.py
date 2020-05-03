# -*- coding: utf-8 -*-
import scrapy
from second.items import SecondItem

class SecondspiderSpider(scrapy.Spider):
    name = 'secondspider'
    allowed_domains = ['www.lagou.com']
    start_urls = ['https://www.lagou.com/beijing-zhaopin/Python/?labelWords=label']

    def parse(self, response):
        for each in response.xpath("//ul[@class='item_con_list']/li") :
            item = SecondItem()
            item['position']= each.xpath("./div[@class='list_item_top']/div/div[@class='p_top']/a/h3/text()").extract()[0]
            item['salary']= each.xpath("./div[@class='list_item_top']/div/div[@class='p_bot']/div/span/text()").extract()[0]
            yield item
