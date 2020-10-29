from pymongo import MongoClient
from pprint import pprint

client = MongoClient('localhost', 27017)

db = client.car_sharing_database
print(db)

cars_table = db.car_table
customer_table = db.customer_table
bookings_table = db.bookings_table

cars_table.update_one()

import datetime
post = {"author": "Mike",
         "text": "My first blog post!",
         "tags": ["mongodb", "python", "pymongo"],
         "date": datetime.datetime.utcnow()}

posts = db.posts
post_id = posts.insert_one(post).inserted_id
post_id

db.list_collection_names()

print("Done")
db.posts.delete_one({"author":'Mike'})
db.posts.delete_one({"author":'Mike'})
db.posts.delete_one({"author":'Mike'})
db.posts.delete_one({"author":'Mike'})

Queryresult = posts.find_one({'author': 'Mike'})
pprint(Queryresult)
