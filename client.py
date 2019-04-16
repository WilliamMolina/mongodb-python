from pymongo import MongoClient
from bson.objectid import ObjectId

class Database: # Classes generally are camel-case, starting with uppercase
    def __init__(self, hostname, port, dbname):
        self._hostname = hostname
        self._port = port
        self._dbname  = dbname

    def connect(self):
        self._client = MongoClient(self._hostname, self._port)
        self._db = self._client[self._dbname]
    # methods usually start with lowercase, and are either camel case (less desirable
    # by Python standards) or underscored (more desirable)
    # All instance methods require the 1st argument to be self (pointer to the
    # instance being affected)
    def createCollection(self, name=""):
        return self._db[name]


if __name__ == '__main__':
    # you want to initialize the class
    database = Database("52.90.145.195", 27017,"testdb")
    database.connect()
    collection = database.createCollection("testcollection")
    data = {
        "Hello": "world!"
    }
    id = collection.insert_one(data).inserted_id
    print(collection.find_one({"_id": ObjectId(id)}))