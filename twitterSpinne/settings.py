# -*- coding: utf-8 -*-

BOT_NAME = 'twitterSpinne'

SPIDER_MODULES = ['twitterSpinne.spiders']
NEWSPIDER_MODULE = 'twitterSpinne.spiders'

USER_AGENT = 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'

ITEM_PIPELINES = ['twitterSpinne.pipelines.MongoDBPipeline', ]

MONGODB_SERVER = "localhost"
MONGODB_PORT = 27017
MONGODB_DB = "twitter"
MONGODB_COLLECTION = "tweet"

