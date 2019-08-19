from scrapy.cmdline import execute
import csv
import pandas as pd
import requests
import time

## run this file, crawl will be run.
#clean the csv file before getting anynew pi
with open('proxy_file.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(('ip','port'))
    file.close()

try:
    execute('scrapy crawl proxy1 --nolog'.split()) #muct be split
    execute('scrapy crawl free_proxy --nolog'.split())
    execute('scrapy crawl openproxy --nolog'.split())
except:
    pass

temp = pd.read_csv('proxy_file.csv')
thelist = list(temp['port'])
good = []
for i in thelist:
    print(i)
    proxies = {"http": i}
    try:
        requests.get("http://google.com", proxies=proxies, timeout=3)
    except:
        print(i, "not successful")
    else:
        print(i, 'successful')
        good.append(i)

with open('proxy_file.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(('ip','port'))
    for k in good:
        writer.writerow(('ip', i))
    file.close()

