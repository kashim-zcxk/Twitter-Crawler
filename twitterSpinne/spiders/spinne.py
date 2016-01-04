# -*- coding: utf-8 -*-

import scrapy
import urlparse
import datetime
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.http import Request
from twitterSpinne.items import TweetItem

class SpinneSpider(scrapy.Spider):
    name = 'spinne'
    query = '%40BarackObama'
    allowed_domains = ['mobile.twitter.com']
    start_urls = (
        'https://mobile.twitter.com/search?q='+query+'&s=typd',
    )
    
    def parse(self, response):
        self.logger.info('Parse Page')
        next = response.xpath('//div[@class="w-button-more"]/a/@href').extract()
        if not next:
            print 'Empty url'
            return
        
        item = TweetItem()
        for sel in response.xpath('//div[@class="timeline"]/table'):
            urlTweet = sel.xpath('@href').extract()[0]
            
            #DEBUG
            username = sel.xpath('tr[@class="tweet-header "]/td[@class="user-info"]/a/div[@class="username"]/text()').extract()[1].rstrip('\n').replace(" ", "")[:-1]
            timestamp = sel.xpath('tr[@class="tweet-header "]/td[@class="timestamp"]/a/text()').extract()[0]
            print timestamp, username
            #/DEBUG
            
            urlTweet = urlparse.urljoin("https://mobile.twitter.com/",urlTweet)
            request = Request(urlTweet, callback=self.parse_tweed)
            yield request

        parsed = urlparse.urljoin("https://mobile.twitter.com/",str(next).strip('[u\']')) 
        yield Request(parsed, callback=self.parse)
        
    def parse_tweed(self, response):
        item = TweetItem()
        textNormalize = ''
        item['url'] = response.url
        item['username'] = response.xpath('//span[@class="username"]/text()').extract()[1].rstrip('\n').replace(" ", "")[:-1]
        item['timestamp'] = response.xpath('//div[@class="metadata"]/a/text()').extract()[0]
        rawText = response.xpath('//table[@class="main-tweet"]/tr/td[@class="tweet-content"]/div[@class="tweet-text"]/div[@class="dir-ltr"]/text()').extract()
        for texxt in rawText:
            textNormalize = textNormalize + ' ' + texxt.replace('\n', '').replace('\t', '').strip()
            
        item['text'] = textNormalize.strip()
        item['avatar'] = response.xpath('//table[@class="main-tweet"]/tr/td[@class="avatar"]/a/img/@src').extract()[0]
        item['hashtag'] = response.xpath('//table[@class="main-tweet"]/tr/td[@class="tweet-content"]/div[@class="tweet-text"]/div[@class="dir-ltr"]/a[@class="twitter-hashtag dir-ltr"]/text()').extract()
        item['atreply'] = response.xpath('//table[@class="main-tweet"]/tr/td[@class="tweet-content"]/div[@class="tweet-text"]/div[@class="dir-ltr"]/a[@class="twitter-atreply dir-ltr"]/text()').extract()
        urlProfile = urlparse.urljoin("https://mobile.twitter.com/",item['username'])
	return item
