from config import connection_string
from pymongo import MongoClient

class MongoConnection:


    def __init__(self):
        self.__mongo_client = MongoClient(connection_string)

    def get_connection(self):
        return self.__mongo_client