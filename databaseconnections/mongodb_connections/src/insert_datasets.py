import glob
import pandas as pd 
import json
from string import digits
import re 
from database_operations import DatabaseManager
from mongod_connection import MongoConnection


def replace_digits(input):
    remove_digits = str.maketrans('', '', digits)
    return input.translate(remove_digits) 


def insert_data(fname,collection_name):
    print("file name:",fname)
    print("collection name:",collection_name)
    print("Inserting records")
    connection = MongoConnection() # Mongoconnection object 
    manager = DatabaseManager("WorldBankDatasets",connection)
    mongo_db = manager.get_db_instance()
    mongo_collection = mongo_db[collection_name]
    data = pd.read_csv(fname)
    payload = json.loads(data.to_json(orient='records'))
    mongo_collection.insert_many(payload)
    print("Record inserted")


path = "./../../../data_extractor/data/*/*.csv"
for fname in glob.glob(path):
    splitted = fname.split("\\")
    file_name = splitted[-1].split(".")[0]
    directory_name = splitted[-2]
    mdirectory_name = replace_digits(directory_name)
    modified_file_name = (file_name.lower().replace(" ","_")).replace("-","_")
    mfile_name = replace_digits(modified_file_name)
    if directory_name.lower() == modified_file_name:
        collection_name = mdirectory_name.lower()
        collection_name = re.sub(r"\__{1,}","",collection_name)
        insert_data(fname,collection_name)
        print("*==*"*20)
    else: 
        collection_name = mdirectory_name + "_" + modified_file_name.replace("___","_")
        collection_name = re.sub(r"\__{1,}","_",collection_name)
        # re.sub(regex_search_term, regex_replacement, text_before)
        insert_data(fname,collection_name)
        print("*==*"*20)


        