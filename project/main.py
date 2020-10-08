import sys
import os.path

from project.car import Car
from project.customer import Customer
from project.booking import Booking

customer = Customer("customer1", True, None)
print(customer.getCustomer())

car = Car("car1", "model1", 4, None, 10.0)
print(car.getCar())




