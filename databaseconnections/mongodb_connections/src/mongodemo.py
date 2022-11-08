from mongod_connection import MongoConnection
from database_operations import DatabaseManager


connection = MongoConnection() # Mongoconnection object 
manager = DatabaseManager("Sherlock",connection)
print(manager.__dir__)
manager.create_database() #<class 'pymongo.database.Database'>
mongo_db = manager.get_db_instance()

print(manager.__dir__)
# mongo_collection = mongo_db.create_collection("Holmes2")
mongo_collection = mongo_db["Holmes"]
mongo_collection.insert_one({"name":"Sherlock"})
for record in mongo_collection.find({}):
    print(record)