import pandas as pd
import pymongo
from pymongo import MongoClient

"""
db.help()
db.dropDatabase()
show dbs
use db
db.stats()
"""

#extraigas host y port de un config file
#puerto = config['puerto'] #27017
#host = config['host'] # 127.0.0.1

#mc = MongoClient()
#mc = MongoClient('localhost,27017') 
mc = MongoClient('127.0.0.1',27017) 
nombrecole = "cole18"

db = mc["nueva17"] # mc.nueva17
cole = db[nombrecole] # db.cole18

doc = {"uno":"nuevo"}
w = cole.insert_one(doc).inserted_id
print(w)