from mongod_connection import MongoConnection


class DatabaseManager:


    def __init__(self,database_name,mongo_connection_object):
        self.database_name = database_name
        self.mongo_connection = mongo_connection_object.get_connection()

        
    def create_database(self):
        if self.database_name in self.mongo_connection.list_database_names():
            print ("Database already exists")
            self.get_db_instance()
        else:
            self.database = self.mongo_connection[self.database_name] 
            # database will not be created unless you insert document in it 


    def collection_creation(self, collection_name):
        if self.database == None:
            print("Database for this object is none")
            print("Collection name: ",collection_name )
            # return self.mongo_connection[db].createCollection(collection_name)
        else: 
            print("Collection created")
            print("Collection name: ", collection_name)


    def get_db_instance(self):
        self.database = self.mongo_connection[self.database_name]
        return self.database

        
    def get_collection_instance(self):
        pass 