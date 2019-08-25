# -*- coding: utf-8 -*-
import scrapy
from ..items import ProxyCrawlItem


class ProxySpider(scrapy.Spider):
    name = 'proxy1'
    allowed_domains = ['www.free-proxy-list.net']
    start_urls = ['https://www.us-proxy.org/']

    def parse(self, response):
        print('proxy1')
        ip_address = response.xpath('//*[@id="proxylisttable"]/tbody/tr//td[1]/text()').extract()
        port = response.xpath('//*[@id="proxylisttable"]/tbody/tr//td[2]/text()').extract()
        country = response.xpath('//*[@id="proxylisttable"]/tbody/tr//td[4]/text()').extract()
        anonymity = response.xpath( '//*[@id="proxylisttable"]/tbody/tr//td[5]/text()').extract()
        item = ProxyCrawlItem()
        for i, j, k, t in zip(ip_address,port, country, anonymity):
            item['ip'] = i
            item['port'] = j
            item['country'] = k
            item['anonymity'] = t
            yield item
        print(len(ip_address),len(port))



