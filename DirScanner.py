#!/usr/bin/env python
#-*-coding:utf-8-*-

import requests
import sys
import config
import argparse


def scan(url):
    f = open(config.dir_Path, "r")
    for path in f:
        #pass    # do scanhere
        scan_url = url + path.strip()
        #print url
        res = requests.get(url=scan_url,headers=config.HEADER,timeout=config.TIMEOUT)
        status = res.status_code
        print "[%d]\t %s" %(status,scan_url)
    f.close()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('website',help="website for scan,eg: http://www.baidu.com")
    parser.add_argument('-t', '--thread', action="store_true")
    parser.add_argument('--suffix',help="This is suffix on scan file")
    args = parser.parse_args()

    url = args.website
    if "http://" not in url and "https://" not in url:
        url = "http://{}".format(url)
    print "url:\t {}".format(url)
    #scan(url)



if __name__ == "__main__":
    main()
