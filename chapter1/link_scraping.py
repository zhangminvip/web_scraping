

import re
import urllib2
import urlparse
import robotparser


def download(url, user_agent = 'wswp', num_retries = 2,proxy = None):
    
    print 'Downloading', url
    headers = {'User-agent':user_agent}
    request = urllib2.Request(url, headers =headers)
    
    opener = urllib2.build_opener()
    if proxy:
        proxy_params = {urlparse.urlparse(url).scheme:proxy}
        opener.add_handler(urllib2.ProxyHandler(proxy_params))
    try:
#        html =  urllib2.urlopen(request).read()
        
        html = opener.open(request).read()
    except urllib2.URLError as e:
        print 'Download error:', e.reason
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code <600:
                return download(url, user_agent, proxy, num_retries -1)
    return html

def analysis_robots():
    rp = robotparser.RobotFileParser()
    rp.set_url('http://example.webscraping.com/robots.txt')
    rp.read()
    return rp
    
    
    
    
def get_links(html):
    webpage_regex = re.compile('<a[^>]+href=["\'](.*?)["\']',re.IGNORECASE)
    
    return webpage_regex.findall(html)    

def link_crawler(seed_url, link_regex):
   
    crawl_queue = [seed_url]
    # keep track which URL's have seen before
    seen = set(crawl_queue)
    while crawl_queue:
        url = crawl_queue.pop()
        rp = analysis_robots()
        user_agent = 'wswp'
        
        if rp.can_fetch(user_agent, url):
            
            html = download(url)
            for link in get_links(html):
                if re.match(link_regex, link):
                    link = urlparse.urljoin(seed_url,link)
                    if link not in seen:
                        seen.add(link)
                        crawl_queue.append(link)
        else:
            print 'Blocked by robots.txt, url

            



