from pymongo import MongoClient

client = MongoClient("mongodb+srv://unipnosql:unipmongodb@cluster0-1jtkx.mongodb.net/test?w=majority")
dbObject = client.unip.test