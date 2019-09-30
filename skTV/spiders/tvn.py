# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request

class TvnSpider(scrapy.Spider):
    name = 'tvn'
    allowed_domains = ['en.wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/Category:2019_South_Korean_television_series_debuts']

    def parse(self, response):
    	movies = response.xpath('//div[@class="mw-category-group"]//li')
    	
    	for tv in movies: 
    		title = tv.xpath('a//text()').extract_first()
    		next_url = tv.xpath('a/@href').extract_first()
    		urls = "https://en.wikipedia.org" + str(next_url)

    		yield Request(urls, self.parse_details, meta={'Title' : title})

    	next_url  = response.xpath('//div[@class="mw-category-group"]//li//a/@href').extract_first()
    	urls = "https://en.wikipedia.org" + str(next_url)

    	yield Request(urls, callback=self.parse)

    def parse_details(self, response):
    	titles = response.meta.get('Title')
    	tvn = "".join(line for line in response.xpath('//*[@class="infobox vevent"]//th[contains(text(),"Original network")]/../td//text()').extract_first()).strip()

    	yield {'Title' : titles, 'TV Network' : tvn}

# for data in response.xpath('//div[@class="mw-parser-output"]//table[@class="infobox vevent"]'):
# 	data = data.xpath('//tbody//tr[21]//td//text()').extract()
# 	print(data)
# //table[@class='wikitable']//tr[19]//th[1]