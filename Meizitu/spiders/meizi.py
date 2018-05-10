# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import MeizituItem


class MeiziSpider(CrawlSpider):
    name = 'meizi'
    allowed_domains = ['mzitu.com']
    start_urls = ['http://www.mzitu.com']

    # 爬取全站图片的链接规则
    rules = (
        Rule(LinkExtractor(allow=r'com/\d+'),
             callback="parse_item", follow=True),
    )

    def parse_item(self, response):
        item = MeizituItem()
        # 获取图片链接
        item["image_url"] = response.xpath(
            '//div[@class="main-image"]/p/a/img/@src').extract_first()
            
        # 获取每组套图的名字
        item["title"] = response.xpath(
            '//div[@class="main-image"]/p/a/img/@alt').extract_first()
        yield item
