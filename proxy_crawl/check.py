import pandas as pd
import requests
import time
import threading


class Http_proxy:
    def __init__(self):
        pass

    def checking(self, ip):
        proxies = {"http": ip}
        try:
            requests.get("http://www.spbeen.com/tool/request_info/", proxies=proxies, timeout=3)
        except:
            print(ip, "not successful")
        else:
            print(ip, "successful")
            save_ip(ip)

def save_ip(ip):
    with open('good_ip.txt','a+') as f:
        f.writelines(ip)
        f.writelines('\n')

def clean_ip():
    with open('good_ip.txt', 'w') as f:
        f.close()


if __name__ == "__main__":
    temp = pd.read_csv('proxy_file.csv')
    iplist = list(temp['ip'])
    portlist = list(temp['port'])
    clean_ip()
    start = time.time()
    proxy = Http_proxy()
    lock = threading.Lock()
    thread_list = []
    for i, p in zip(iplist, portlist):
        thread_list.append(threading.Thread(target=proxy.checking, args=(str(i)+':'+str(p),)))
    for t in thread_list:
        t.start()
    for t in thread_list:
        t.join()
    end = time.time()
    print("used time:{}".format((end - start)))
