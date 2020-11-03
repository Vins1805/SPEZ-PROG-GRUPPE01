import json

from flask import Flask, request, jsonify

from booking import Booking
from customer import *
from car import *
from database import Db

app = Flask(__name__)

car_file = "test_data/car_data.json"
customer_file = "test_data/customer_data.json"

with open(car_file) as json_file:
    cars_data = json.load(json_file)

with open(customer_file) as json_file:
    customer_data = json.load(json_file)

db = Db()
car_list = list(cars_data.values())
customer_list = list(customer_data.values())
db.bulk_insert(car_list, "car")
db.bulk_insert(customer_list, "customer")
db.insert(Car("4","yellow","Audi","A8","5",None,2,True).toJSON(),"car")
cars = Cars()


for i in db.getTable("car"):
    car = Car(i["_id"], i["color"], i["brand"], i["model"], i["seats"], i["location"],
              i["price"], i["available"])
    cars.addCar(car)

customers = Customers()
for i in db.getTable("customer"):
    customer = Customer(i["_id"],i["surname"], i["name"], i["driver_license"],
                        i["payment_methods"], i["renting"])
    customers.addCustomer(customer)

bookings = Bookings()

@app.route('/')
def info():
    return 'Hello HTW'


@app.route('/show_customers')
def show_customers():
    return str([customer.toJSON() for customer in customers]).replace("'","")


@app.route('/show_cars')
def show_cars():
    return str([car.toJSON() for car in cars]).replace("'","")




@app.route('/book_car', methods=['POST'])
def book_car():
    s = "Error"
    remember_me = False
    car_id = request.args.get("car_id")
    customer_name = request.args.get("customer_name")

    for customer in customers:
        if customer.name == customer_name and customer.renting == False and customer.driver_license == True:
            for car in cars:
                remember_me = True
                if car._id == car_id and car.available == True:
                    print(customer)
                    customer.rentCar(car)
                    booking = Booking(car._id, customer._id)
                    db.insert(booking.toJSON(), "booking")
                    car.addBooking(booking)
                    customer.addBooking(booking)
                    bookings.addBooking(booking)
                    print(customer)
                    s = f"{customer.surname} booked {car.brand} {car.model}."
                    break
                else:
                    s = "Car not found or not available."

        elif remember_me == False:
            s = "You are renting already or you have to add your driver license."

    return s

@app.route('/show_bookings')
def show_bookings():
    return str([booking.toJSON() for booking in bookings]).replace("'","")


app.run(host='0.0.0.0', port=4000)
