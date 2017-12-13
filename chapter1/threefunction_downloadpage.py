# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

python version:    2.7


this function can 
1   catch the exception
2   download again
3   set up user agents

"""

import urllib2
import re


def download(url, user_agent = 'wswp', num_retries = 2):
    
    print 'Downloading', url
    headers = {'User-agent':user_agent}
    request = urllib2.Request(url, headers =headers)
    try:
        html =  urllib2.urlopen(request).read()
    except urllib2.URLError as e:
        print 'Download error:', e.reason
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code <600:
                return download(url, num_retries -1)
    return html


def crawl_sitmap(url):
    # download the sitmap file
    sitmap = download(url)
    # extract the sitmap links
    links = re.findall('<loc>(.*?)</loc>', sitmap)
    #download each link
    for link in links:
        html = download(link)
        
        
def traverse_id(url):
    # maximum number of consecutive download errors allowed
    max_errors = 5
    # current number of consecutive download errors
    num_errors = 0
    for page in itertools.count(1):
        url = 'http://example.webscraping.com/view/-%d' % page
        html = download(url)
        if html is None:
            #received an error trying to download this webpage
            num_errors += 1
            if num_errors == max_errors:
                break
            
        else:
            num_errors = 0
        
    
            

download('http://www.baidu.com')