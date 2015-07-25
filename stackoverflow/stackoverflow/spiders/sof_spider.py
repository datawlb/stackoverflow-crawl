# -*- coding:utf-8 -*-
__author__ = 'datawlb'
from scrapy.selector import Selector
try:
    from scrapy.spider import Spider
except:
    from scrapy.spider import BaseSpider as Spider
from scrapy.contrib.spiders import CrawlSpider, Rule
from stackoverflow.items import StackoverflowItem

class stackoverflowSpider(CrawlSpider):
    name = "sof"
    allowed_domains = ["stackoverflow.com/"]
    start_urls = [
        "http://stackoverflow.com/questions?page="+str(i)+"&sort=newest" for i in range(1,100,1)  # 100 pages
    ]
    rules = [
    ]

    def parse(self, response):
        sel = Selector(response)
        sites = sel.xpath('//div[@id="questions"]/div[@class="question-summary"]')
        items = []
        print len(sites)

        for site in sites:
            item = StackoverflowItem()
            #tt = site.xpath('div[1]/div[3]/text()').extract()
            #print tt[0].split(' ')
            item['views'] = site.xpath('div[1]/div[3]/text()').extract()[0].split(' ')[4]
            item['votes'] = site.xpath('div[1]/div[2]/div[1]/div/span/strong/text()').extract()
            item['answers'] = site.xpath('div[1]/div[2]/div[2]/strong/text()').extract()
            item['title'] = site.xpath('div[2]/h3/a/text()').extract()

            key_list = [ksite.xpath('text()').extract()[0].encode('utf-8') for ksite in site.xpath('div[2]/div[2]/a')]
            item['key'] = " ".join(str(ele) for ele in key_list)

            item['author'] = site.xpath('div[2]/div[3]/div/div[3]/a/text()').extract()

            item['time'] = site.xpath('div[2]/div[3]/div/div[1]/span/text()').extract()

            items.append(item)

        return items








