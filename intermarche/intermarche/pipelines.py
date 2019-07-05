# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class IntermarchePipeline(object):
	counter_id = 0

	def process_item(self, item, spider):
		if spider.name == 'spider_category':
			self.counter_id += 1
			item['id'] = self.counter_id
            return item
        
		return item
