# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BtbtdyMovieItem(scrapy.Item):
    name = scrapy.Field()
    url = scrapy.Field()
    score = scrapy.Field()
    des = scrapy.Field()
