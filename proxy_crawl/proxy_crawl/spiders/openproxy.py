# -*- coding: utf-8 -*-
import scrapy
from ..items import ProxyCrawlItem

class OpenproxySpider(scrapy.Spider):
    name = 'openproxy'
    allowed_domains = ['www.openproxy.space/free-proxy-list']
    start_urls = ['http://www.openproxy.space/free-proxy-list/']

    def parse(self, response):
        print('openproxy')
        ip_address = response.xpath('//*[@id="root"]/div/div[1]/div/table/tbody/tr[@class = "http"]/td[@class = "ip"]/div/text()').extract()
        port = response.xpath('//*[@id="root"]/div/div[1]/div/table/tbody/tr[@class = "http"]/td[3]/text()').extract()
        item = ProxyCrawlItem()
        for i, j in zip(ip_address, port):
            print(i.split()[0],j.split()[0])
            item['ip'] = i.split()[0]
            item['port'] = j.split()[0]
            yield item
        print(len(ip_address), len(port))
