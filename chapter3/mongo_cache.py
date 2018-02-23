try:
    import cPickle as pickle
except ImportError:
    import pickle
import zlib
from datetime import datetime, timedelta
from pymongo import MongoClient
from bson.binary import Binary


expires = timedelta(days = 30)
ex = expires.total_seconds()

print ex

print datetime.utcnow()