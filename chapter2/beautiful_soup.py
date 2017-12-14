from bs4 import BeautifulSoup
import urllib2
import urlparse

def download(url, headers, proxy, num_retries, data=None):
    print 'Downloading:', url
    request = urllib2.Request(url, data, headers)
    opener = urllib2.build_opener()
    if proxy:
        proxy_params = {urlparse.urlparse(url).scheme: proxy}
        opener.add_handler(urllib2.ProxyHandler(proxy_params))
    try:
        response = opener.open(request)
        html = response.read()
        code = response.code
    except urllib2.URLError as e:
        print 'Download error:', e.reason       
        html = ''
        if hasattr(e, 'code'):
            code = e.code
            if num_retries > 0 and 500 <= code < 600:
                # retry 5XX HTTP errors
                return download(url, headers, proxy, num_retries-1, data)
        else:
            code = None
    return html

#def download(url, user_agent = 'wswp', num_retries = 2):
#    
#    print 'Downloading', url
#    headers = {'User-agent':user_agent}
#    request = urllib2.Request(url, headers =headers)
#    try:
#        html =  urllib2.urlopen(request).read()
#    except urllib2.URLError as e:
#        print 'Download error:', e.reason
#        html = None
#        if num_retries > 0:
#            if hasattr(e, 'code') and 500 <= e.code <600:
#                return download(url, num_retries -1)
#    return html

url = 'http://example.webscraping.com/places/default/view/Afghanistan-1'
html = download(url,headers = {'User-agent':'wswp'},proxy = None, num_retries = 1)
soup = BeautifulSoup(html)
tr  = soup.find(attrs = {'id':'places_area__row'})
td = tr.find(attrs = {'class':'w2p_fw'})
area = td.text
print type(tr)
print area