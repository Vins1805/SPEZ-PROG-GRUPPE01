from project.car import *
from project.customer import Customer
from project.booking import Booking
from time import sleep
import json
from pathlib import Path
import os

ROOT = Path(__file__).parent.parent

car_file = os.path.join(ROOT, "test_data/car_data.json")
customer_file = os.path.join(ROOT, "test_data/customer_data.json")

with open(car_file) as json_file:
    cars_data = json.load(json_file)

with open(customer_file) as json_file:
    customer_data = json.load(json_file)

cars = list()
cars.append(cars_data["car1"])
cars.append(cars_data["car2"])
cars.append(cars_data["car3"])

customers = list()
customers.append(customer_data["customer1"])
customers.append(customer_data["customer2"])
customers.append(customer_data["customer3"])

bookings = list()

car = cars[0]
customer = customers[1]

print(car.__str__())
print(customer.__str__())

customer1 = Customer(customer["surname"], customer["name"], customer["driver_license"], customer["payment_methods"])
car1 = Car(car["color"], car["brand"], car["model"], car["seats"], car["location"], car["price"], car["available"])

customer1.rentCar(car1)

booking1 = Booking(car1.getID(), customer1.getID())
print(f"Rent started: {booking1.begin}")
car1.addBooking(booking1)

sleep(5)

customer1.returnCar(car1, booking1)
bookings.append(booking1)
print(booking1.__str__())

for i in bookings:
    print(i)
