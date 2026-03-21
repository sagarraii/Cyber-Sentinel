'''ETL Pipeline : extract and read data from local, do some transformation
 and convert the data into JSON then upload it to MongoDB Atlas'''

import os
import sys
import json

from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URL = os.getenv('MONGO_DB_URL')
print(MONGO_DB_URL)

import certifi # python package that provides the set of roots certificate ? used to make secure http connections
ca = certifi.where()

import pandas as pd
import numpy as np
import pymongo
from networksecurity.exception.custom_exception import NetworkSecurityException
from networksecurity.logging.logger import logging


class NetworkDataExtract():

    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def cv_to_json_converter(self, file_path):
        try:
            # read the dataset
            data = pd.read_csv(file_path)
            # reset the index
            data.reset_index(drop=True, inplace=True)
            # convert the data into list of json
            records = list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def insert_data_mongo(self, records, database, collection):
        try:
            self.records = records
            self.database = database
            self.collection = collection

            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL)

            self.database = self.mongo_client[self.database]
            self.collection = self.database[self.collection]
            self.collection.insert_many(self.records)

            return (len(self.records))
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
if __name__ == "__main__":
    FILE_PATH = "Network_Data\phisingData.csv"
    DATABASE = "SAGARAI"
    Collection = "NetworkData"
    networkobj = NetworkDataExtract()
    records = networkobj.cv_to_json_converter(file_path = FILE_PATH)
    print(records)
    no_of_records = networkobj.insert_data_mongo(records, DATABASE, Collection)
    print(no_of_records)