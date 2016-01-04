# -*- coding: utf-8 -*-

# Define here the models for your scraped items

import scrapy


class TweetItem(scrapy.Item):
    username = scrapy.Field()
    profile = scrapy.Field()
    url = scrapy.Field()
    timestamp = scrapy.Field()
    text = scrapy.Field()
    hashtag = scrapy.Field()
    atreply = scrapy.Field()
    avatar = scrapy.Field()
    pass
