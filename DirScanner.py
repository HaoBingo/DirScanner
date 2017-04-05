#!/usr/bin/env python
#-*-coding:utf-8-*-

import requests
import sys
import config


def usage():
    print "Usage: \npython %s http://foo.com/" %sys.argv[0]

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
    if len(sys.argv) != 2:
        usage()
        sys.exit(0)
    url = sys.argv[1]
    if "http://" not in url:
        url = "http://%s" %url
    #print "url:\t %s" %url
    scan(url)



if __name__ == "__main__":
    main()
