# Free_Proxy_Pool Project
Getting free proxy and check if proxy is useable

Free_proxy_websites used:
- www.openproxy.space/free-proxy-list
- www.free-proxy-list.net
- www.free-proxy.cz # this website down after the spider is finished

The spider Max RE_try time is set to 2 in the setting.py(by default is 3)
crawling Proxy ip and port, country, and anonymity. More can be added in the pipeline&item file if needed.

After crawling the above website, all possible ip is stored into proxy_file.csv

Then, in the 'check.py' file, the csv file is read and all ip is checked (by requesting google.com)
	- the proxy request is using mutli threading (much faster than just using for loop and requesting one by one, 8sec vs 130sec for 200 proxy)  





