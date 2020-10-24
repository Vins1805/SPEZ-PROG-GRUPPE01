import os
from flask import Flask, jsonify, request

from backend.booking import Booking
from backend.customer import *
from backend.car import *
from time import sleep
from pathlib import Path

app = Flask(__name__)

ROOT = Path(__file__).parent

car_file = os.path.join(ROOT, "test_data/car_data.json")
customer_file = os.path.join(ROOT, "test_data/customer_data.json")

with open(car_file) as json_file:
    cars_data = json.load(json_file)

with open(customer_file) as json_file:
    customer_data = json.load(json_file)

cars = Cars()
for i in cars_data.values():
    car = Car(i["ID"], i["color"], i["brand"], i["model"], i["seats"], i["location"],
              i["price"], i["available"])
    cars.addCar(car)

customers = Customers()
for i in customer_data.values():
    customer = Customer(i["surname"], i["name"], i["driver_license"],
                        i["payment_methods"], i["renting"])
    customers.addCustomer(customer)

bookings = Bookings()


@app.route('/info')
def info():
    return 'Hello HTW'


@app.route('/show_customers')
def show_customers():
    return str([customer.toJSON() for customer in customers])


@app.route('/show_cars')
def show_cars():
    return str([car.toJSON() for car in cars])


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
                if car.ID == car_id and car.available == True:
                    print(customer)
                    customer.rentCar(car)
                    booking = Booking(car.ID, customer.ID)
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
    return str([booking.toJSON() for booking in bookings])


app.run(host='0.0.0.0', port=4000)
