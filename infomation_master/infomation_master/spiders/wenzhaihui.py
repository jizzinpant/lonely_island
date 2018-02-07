# -*- coding: utf-8 -*-
import scrapy


class WenzhaihuiSpider(scrapy.Spider):
    name = 'wenzhaihui'
    allowed_domains = ['wenzhaihui.com']
    start_urls = ['http://wenzhaihui.com/']

    def parse(self, response):
        pass
