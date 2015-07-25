# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
from scrapy.item import Item, Field
import scrapy


class StackoverflowItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #pass
    votes = Field()
    answers = Field()
    views = Field()
    title = Field()  # question title
    key = Field()    # key question about language(eg: php,java,c++...)
    author = Field()
    time = Field()