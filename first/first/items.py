# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FirstItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    runid = scrapy.Field()
    username = scrapy.Field()
    problem_id = scrapy.Field()
    result = scrapy.Field()
    memory = scrapy.Field()
    timer = scrapy.Field()
    lang = scrapy.Field()
    codel = scrapy.Field()
    sub_time = scrapy.Field()
    pass
