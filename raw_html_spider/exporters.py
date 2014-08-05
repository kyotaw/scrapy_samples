# -*- coding: utf-8 -*-

from scrapy.contrib.exporter import BaseItemExporter

import lxml.etree
import lxml.html

import os
from urlparse import urlparse

class RawHtmlExporter(BaseItemExporter):
	def __init__(self, dir):
		self.exportDir = dir
		if not os.path.exists(self.exportDir):
			os.makedirs(self.exportDir)

	def export_item(self, item):
		root = lxml.html.fromstring(item["body"])
		lxml.etree.strip_elements(root, lxml.etree.Comment, 'script', 'head')
		rawHtml = lxml.html.tostring(root)
		url = urlparse(item["url"])
		path = url.path.replace("/", ".").lstrip(".")
		file = open(self.exportDir + path, "wb")
		file.write(rawHtml.encode(item["encoding"]))
		return item
		
