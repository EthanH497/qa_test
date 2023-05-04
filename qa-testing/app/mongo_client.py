import pymongo  # package for working with MongoDB

# Client connects to local docker container running mongodb
client = pymongo.MongoClient("mongodb://root:password@localhost:27017/?authMechanism=DEFAULT")
# Database name
db = client["userDb"]
# User collection in userDb database
users_collection = db["users"]