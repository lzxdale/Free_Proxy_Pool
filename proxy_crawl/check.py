import pandas as pd
import requests
import time
temp = pd.read_csv('proxy_file.csv')
thelist = list(temp['port'])
for i in thelist:
    print(i)
    proxies = {"http": i}
    try:
        requests.get("http://google.com", proxies=proxies, timeout=3)
    except:
        print(i, "not successful")
    else:
        print(i, 'successful')