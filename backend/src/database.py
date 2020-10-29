import json

import pymongo
from pymongo import MongoClient, UpdateMany, UpdateOne, InsertOne, DeleteMany

car_file = "test_data/car_data.json"
customer_file = "test_data/customer_data.json"

with open(car_file) as json_file:
    cars_data = json.load(json_file)

with open(customer_file) as json_file:
    customer_data = json.load(json_file)


class Db():
    def __init__(self):
        self.host = 'localhost'
        self.port = 27017
        self.con = MongoClient(self.host, self.port)
        self.db = self.con.car_sharing_database

    def delete_all(self, table: str):
        self.db[table].bulk_write([
            DeleteMany({})
        ])

    def update(self, id: int, column: str, value, table):
        try:
            self.db[table].update_one({'_id': id}, {'$set': {column: value}}) #TODO: adds new column if dont exists
        except:
            print("Wrong ID or column")

    def bulk_update(self):
        pass

    def insert(self, data: dict, table: str):
        try:
            self.db[table].insert_one(data)
        except:
            print("ID already exists.")

    def bulk_insert(self, data: list, table: str):
        try:
            self.db[table].bulk_write([InsertOne(i) for i in data if self.find("_id", i["_id"], table) == None])
        except:
            print("All given keys already exist.")

        # cars_table.bulk_write([
        #     DeleteMany({}),
        #     InsertOne(cars_data["car1"]),
        # ])

    def find(self, key: str, value: str, table: str):
        for i in self.db[table].find({key: value}): return i


cars = list(cars_data.values())
# print(cars[0]["_id"])


db = Db()

# db.insert(cars_data["car1"], "car")
# db.find("color", "black", "car")
db.delete_all("car")
# db.find("color", "black", "car")
db.bulk_insert(cars, "car")
print(db.find("_id", 3, "car"))
db.update(3, "available", False, "car")
print(db.find("_id", 3, "car"))

# db.customer_table.update(param=...)

#
# client = MongoClient('localhost', 27017)
#
# db = client.car_sharing_database
# print(db)
#
# cars_table = db.car_table
# customer_table = db.customer_table
# bookings_table = db.bookings_table
#
# cars_table.bulk_write([
#     DeleteMany({}),
#     InsertOne(cars_data["car1"]),
# ])
#
# query = cars_table.find({"color": "black"})
# for x in query:
#     print(x)
#
# for row in cars_table.find():
#     print(row)
#
# db.list_collection_names()
