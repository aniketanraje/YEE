from config import connection_string
from pymongo import MongoClient


mongo_client = MongoClient(connection_string)
print(mongo_client)