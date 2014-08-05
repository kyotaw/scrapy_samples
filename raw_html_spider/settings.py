# -*- coding: utf-8 -*-

# Scrapy settings for crime_crawler project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'raw_html_spider'

SPIDER_MODULES = ['raw_html_spider.spiders']
NEWSPIDER_MODULE = 'raw_html_spider.spiders'

DOWNLOAD_DELAY = 3
ROBOTSTXT = True
COOKIES_ENABLED = False

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'raw_html_spider (+http://www.yourdomain.com)'

ITEM_PIPELINES = {
	'raw_html_spider.pipelines.RawHtmlExportPipeline' : 100,
}
