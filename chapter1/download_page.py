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
            

download('http://www.baidu.com')