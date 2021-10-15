from info import DATABASE_URI

import pymongo
DB_URL = DATABASE_URI
DB_NAME = "ALBusers" 
mongo = pymongo.MongoClient(DB_URL)
db = mongo[DB_NAME]
dbcol = db["SMLxUSER"]


def insert(chat_id):
            user_id = int(chat_id)
            user_det = {"_id":user_id}
            try:
            	dbcol.insert_one(user_det)
            except:
            	pass

def getid():
    values = []
    for key  in dbcol.find():
         id = key["_id"]
         values.append((id)) 
    return values
