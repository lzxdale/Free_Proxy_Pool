# Free_Proxy_Pool Project
Getting free proxy and check if proxy is useable

Free_proxy_websites used:
- www.openproxy.space/free-proxy-list
- www.free-proxy-list.net
- www.free-proxy.cz # the website down after the spider is finished, not useable now

<<<<<<< HEAD
The spider Max RE_try time is set to 2 in the setting.py(by default is 3)
crawling Proxy ip and port, country, and anonymity. More can be added in the pipeline&item file if needed.
=======
The spider Max RE_try time is set to 2 in the setting.py (by default is 3)

Only crawling Proxy ip and port, more can be added in the pipeline.py if needed.
>>>>>>> c1a06fe6162c3ae638bfc12774c077cdfd12aaeb

After crawling the above website, all possible ip is stored into proxy_file.csv

Then, in the 'check.py' file, the csv file is read and all ip is checked (by requesting google.com)
	
	- the proxy request is using mutli threading (much faster than just using for loop and requesting one by one, 8sec vs 130sec for 200 proxy)  

- Use Method:
	
	open the proxy_crawl folder by pycharm as project
	
	run Proxy_get&check.py
	
	U will got a txt file call the good_ip
	
	done



