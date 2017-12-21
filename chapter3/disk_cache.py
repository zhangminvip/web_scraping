import os 
import re
import urlparse
import shutil
import zlib
from datetime import datetime, timedelta
try:
    import cPickle as pickle
except ImportError:
    import pickle
    
from link_crawler import link_crawler

class DiskCache:
    """
    Dictionary interface that stores cached 
    values in the file system rather than in memory.
    The file path is formed from an md5 hash of the key.

    >>> cache = DiskCache()
    >>> url = 'http://example.webscraping.com'
    >>> result = {'html': '...'}
    >>> cache[url] = result
    >>> cache[url]['html'] == result['html']
    True
    >>> cache = DiskCache(expires=timedelta())
    >>> cache[url] = result
    >>> cache[url]
    Traceback (most recent call last):
     ...
    KeyError: 'http://example.webscraping.com has expired'
    >>> cache.clear()
    """
    
    
    def __init__(self, cache_dir='cache', expires=timedelta(das=30),compress=True):
        '''
        
        cache_dir:the root level folder for the cache
        expires: timedelta of amount of time before a cache entry is considered expried
        compress: whether to compress data in the cache
        '''
        self.cache_dir = cache_dir
        self.expires = expires
        self.compress = compress
        
    def __getitem__(self, url):
        '''
        
        Load data from disk for this url
        '''
        
        path = self.url_to_path(url)
        
        
    def url_to_path(self, url):
        '''
        Create file system path for this url
        '''
        
        
    
        


    