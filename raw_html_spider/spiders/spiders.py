# -*- coding: utf-8 -*-

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.selector import Selector
from scrapy.http import HtmlResponse
from raw_html_spider.items import RawHtmlItem

class RawHtmlSpider(CrawlSpider):
	name = 'police.pref.aomori.jp'
	allowed_domains = ['police.pref.aomori.jp']
	start_urls = ['http://www.police.pref.aomori.jp/']
	
	rules = [
		Rule(LxmlLinkExtractor(allow=(r'keimubu/kouhou/jiken_jiko.html')), callback='parse_crime')
	]

	def parse_crime(self, response):
		htmlRes = HtmlResponse(url=response.url, body=response.body)
		item = RawHtmlItem();
		item["url"] = htmlRes.url
		item["body"] = htmlRes.body
		item["encoding"] = htmlRes.encoding
		return item


