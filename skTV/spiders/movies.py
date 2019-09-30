# -*- coding: utf-8 -*-
import scrapy


class MoviesSpider(scrapy.Spider):
    name = 'movies'
    allowed_domains = ['en.wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/Category:2019_South_Korean_television_series_debuts']

    def parse(self, response):
    	titles = response.xpath('//div[@class="mw-category-group"]//li//a//text()').extract()

    	for title in titles:
        	yield {'Title' : title }