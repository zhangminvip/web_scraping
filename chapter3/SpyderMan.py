# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 15:43:33 2018

@author: tom
"""

from HtmlParser import HtmlParser
from DataOutput import DataOutput

class SpiderMan(object):
    def __init__(self):
        self.output = DataOutput()
        self.parser = HtmlParser()
        
    def crawl(self, root_url):
        self.manager.add_new_url(root_url)
        while (self.manager.has_new_url() and self.manager.old_url_size() < 100):
            try:
                
                new_url = self.manager.get_new_url()
                html = self.downloader.downloader(new_url)
                new_urls,data = self.parser.parser(new_url,html)
                self.manager.add_new_urls(new_urls)
                self.output.store_data(data)
            except Exception e:
                print 'Crawl Fail'
            self.output.output_html()
            
        
if __name__ == '__main__':
    spider_man = SpiderMan()