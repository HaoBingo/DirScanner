#!/usr/bin/env python
#-*-coding:utf-8-*-

import requests
import sys

# 字典路径
dir_Path = ''

def usage():
    print '''Usage: \npython %s http://foo.com/''' %sys.argv[0]

def scanne(url):
    f = open("bigFile.txt", "r")
    for line in f:
        pass    # do something here  
    f.close()

def main():
    if len(sys.argv) != 2:
        usage()
        sys.exit(0)
    url = sys.argv[1]
    if "http://" not in url:
        url = "http://%s" %url
    print "url:\t %s" %url



if __name__ == "__main__":
    main()
