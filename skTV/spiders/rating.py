# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request

class RatingSpider(scrapy.Spider):
    name = 'rating'
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
    	tvn = "".join(line for line in response.xpath('//*[@class="infobox vevent"]//th[contains(text(),"Original network")]/../td//text()').extract_first())
    	
    	month = response.xpath('//table[@class="infobox vevent"]//th[contains(text(),"Original release")]/..//td//text()').extract_first().strip()
    	rating = response.xpath('//table[@class="wikitable"]//span//b//text()').extract_first("-")

        item = {'Title' : titles, 'TV Network' : tvn, 'Month release' : month, 'Rating' : rating}
    	yield item

