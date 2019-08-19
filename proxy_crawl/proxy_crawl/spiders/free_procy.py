# -*- coding: utf-8 -*-
import scrapy
import base64
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import ProxyCrawlItem


class FreeProcySpider(CrawlSpider):
    name = 'free_proxy'
    allowed_domains = ['www.free-proxy.cz/en/proxylist/country/all/http/ping/all']
    start_urls = ['http://www.free-proxy.cz/en/proxylist/country/all/http/ping/all/']

    rules = (
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        print('free_proxy')
        item = ProxyCrawlItem()
        java_ip = response.xpath('//*[@id="proxy_list"]/tbody/tr/td//script[@type = "text/javascript"]/text()').extract()
        ip_port = response.xpath('//*[@id="proxy_list"]/tbody/tr/td/span/text()').extract()
        for i, j in zip(java_ip, ip_port):
            i = i.split('"')[1]
            temp = str(base64.b64decode(i))[-2:-1]
            item['ip'] = temp
            item['port'] = j
            yield item
        print(len(java_ip),len(ip_port))
