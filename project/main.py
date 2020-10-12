from project.car import Car
from project.customer import Customer
from project.booking import Booking
from time import sleep
import json

car_file = "C:/Users/valdo/PycharmProjects/SPEZ-PROG-GRUPPE01/test_data/car_data.json"

customer_file = "C:/Users/valdo/PycharmProjects/SPEZ-PROG-GRUPPE01/test_data/customer_data.json"

with open(car_file) as json_file:
    car_data = json.load(json_file)

with open(customer_file) as json_file:
    customer_data = json.load(json_file)

car = car_data["car1"]
customer = customer_data["customer2"]

customer1 = Customer(customer["surname"], customer["name"], customer["driver_license"], customer["payment_methods"])

car1 = Car(car["color"], car["brand"], car["model"], car["seats"], car["location"], car["price"], car["available"])

customer1.rentCar(car1)

booking1 = Booking(car1.getID(), customer1.getID())
print(f"Rent started: {booking1.begin}")
car1.addBooking(booking1)

sleep(5)

customer1.returnCar(car1, booking1)
