from project.car import Car
from project.customer import Customer
from project.booking import Booking
from time import sleep

customer1 = Customer(True, None)
print(customer1.__str__())

car1 = Car("model1", 4, None, 10.0, True)
print(car1.__str__())
print(car1.showBookings())

customer1.rentCar(car1)
booking1 = Booking(car1.getID(), customer1.getID())
car1.addBooking(booking1)

print(car1.__str__())
print(car1.showBookings())
print(booking1.__str__())

sleep(5)

customer1.returnCar(car1, booking1)

print(car1.__str__())
print(booking1.__str__())