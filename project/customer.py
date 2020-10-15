import uuid
import json


class Customer():
    def __init__(self, surname, name, driver_license, payment_methods, renting):
        self.ID = str(uuid.uuid4())
        self.surname = surname
        self.name = name
        self.driver_license = driver_license
        self.payment_methods = payment_methods
        self.renting = renting
        self.bookings = list()

    def __repr__(self):
        return {"ID": self.ID, "Surname": self.surname, "Name": self.name, "Driver license": self.driver_license,
                "Payment methods": self.payment_methods, "Renting": self.renting}

    def toJSON(self):
        return json.dumps(self.__dict__)

    def getID(self):
        """get customer.ID"""
        return self.ID

    def setCustomer(self):
        pass

    def setRentingState(self):
        """toggles the renting state of a customer"""
        self.renting = not self.renting

    def rentCar(self, car):
        """call function setAvailability"""
        if self.driver_license == False:
            print("Please add a driver license")
        else:
            print(f"Renting {car.brand} {car.model}")
            self.setRentingState()
            car.setAvailability()

    def returnCar(self, car, booking):
        """call function setAvailability and call function booking.endBooking"""
        car.setAvailability()
        self.setRentingState()
        booking.endBooking(car.getPrice())

    def addBooking(self, booking):
        """car gets assigned one booking to a list where all bookings from one car are stored"""
        self.bookings.append(booking.getID())

    def showBookings(self):
        """show booking list of one car"""
        return self.bookings
