from scrapy.cmdline import execute
import csv
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings




def main():
    ## run this file, crawl will be run.
    #clean the csv file before getting anynew pi
    with open('proxy_file.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(('ip','port','country', 'anonymity'))
        file.close()

    crawl_list = [
        'openproxy',
        'proxy1',
        #'free_proxy',
    ]

    # retry times was set to twice
    process = CrawlerProcess(get_project_settings())
    for spider in crawl_list:
        process.crawl(spider)
    process.start()

if __name__ == "__main__":
    main()





# import os
# str=('python check.py')
# p = os.system(str)
# print('\n'*5, '-'*10, '\n', 'valid ip is stored')
