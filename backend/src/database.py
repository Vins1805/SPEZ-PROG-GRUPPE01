import json

import pymongo
from pymongo import MongoClient, UpdateMany, UpdateOne, InsertOne, DeleteMany


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

            if column in self.db[table].find()[0].keys():
                self.db[table].update_one({'_id': id}, {'$set': {column: value}})
            else :
                print("Wrong Column name.")
        except:
            print("Wrong ID or column")


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


    def find(self, key: str, value: str, table: str):
        for i in self.db[table].find({key: value}): return i

    def getTable(self,table):

        return self.db[table].find()




# print(cars[0]["_id"])


# db = Db()
#
# # db.insert(cars_data["car1"], "car")
# # db.find("color", "black", "car")
# db.delete_all("car")
# db.find("color", "black", "car")
# db.bulk_insert(cars, "car")
# print(db.find("_id", 3, "car"))
# db.update(3, "available", False, "car")
# print(db.find("_id", 3, "car"))

