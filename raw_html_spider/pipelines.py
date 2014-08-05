# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy import signals

from raw_html_spider.exporters import RawHtmlExporter

import datetime
import os

class RawHtmlExportPipeline(object):
	@classmethod
	def from_crawler(cls, crawler):
		pipeline = cls()
		crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
		crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
		return pipeline
	
	def spider_opened(self, spider):
		date = datetime.date.today()
		expDir = "./data/raw/" + spider.name + "/" + str(date.year) + "." + str(date.month) + "." + str(date.day) + "/"
		self.exporter = RawHtmlExporter(expDir)
		self.exporter.start_exporting()

	def spider_closed(self, spider):
		self.exporter.finish_exporting()
	
	def process_item(self, item, spider):
		self.exporter.export_item(item)
		return item
