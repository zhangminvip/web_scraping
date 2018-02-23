# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 16:06:46 2018

@author: tom
"""


improt cPickle
import 

class UrlManager:


    def __init__(self):
        self.new_urls = self.load_process("new_urls.txt")
        self.old_urls = self.load_process("old_urls.txt")
        
        
    def has_new_url(self):
        return self.new_url_size() != 0
    
    
    def get_new_url(self):
        new_url = self.new_urls.pop()
        m = hashlib.md5()
        m.update(new_url)
        self.old_urls.add(m.hexigest()[8:-8])
        return new_url
    
    def add_new_urls(self,url):
        if url is None:
            return
        
    
    
    
    
    
    def new_url_size(self):
        return len(self.new_urls)
    
    
    def save_process(self,path,data):
        with open(path,'wb') as f:
            cPickle.dump(data,f)
            
            
    def load_process(self,path):
        try:
            with open(path,'rb') as f:
                tmp = cPickle.load(f)
                return tmp
            
        except:
            print 'not file'
        return set()
            