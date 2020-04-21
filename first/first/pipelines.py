# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import codecs
class FirstPipeline(object):
    def __init__(self):
        self.file = codecs.open("tencent.json", "w+",encoding="utf-8")
    def process_item(self, item, spider):
        iaa = dict(item)
        text = json.dumps(iaa, ensure_ascii = False) + ",\n"
        self.file.write(text)
        return item
    def close_spider(self, spider):
        self.file.close()