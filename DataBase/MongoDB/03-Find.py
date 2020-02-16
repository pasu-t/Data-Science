import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

# x = mycol.find_one()
x = mycol.find()

for x in mycol.find():
    print(x)