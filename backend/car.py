import json
from backend.booking import Bookings


class Car():
    def __init__(self, ID, color, brand, model, seats, location, price, available):
        self.ID = ID
        self.color = color
        self.brand = brand
        self.model = model
        self.seats = seats
        self.location = location
        self.price = price
        self.available = available
        self.bookings = Bookings()

    def __str__(self):
        return f"{self.ID},{self.color},{self.brand},{self.model}," \
               f"{self.seats},{self.location},{self.price},{self.available}"

    def toJSON(self):
        return json.dumps(self.__dict__)

    def getID(self):
        return self.ID

    def getPrice(self):
        return self.price

    def setID(self):
        pass

    def setModel(self):
        pass

    def setAvailability(self):
        """toggles the availability of a car"""
        self.available = not self.available

    def updateLocation(self):
        pass

    def openCar(self):
        pass

    def closeCar(self):
        pass

    def addBooking(self, booking):
        """car gets assigned one booking to a list where all bookings from one car are stored"""
        self.bookings.addBooking(booking.getID())

    def showBookings(self):
        """show booking list of one car"""
        return self.bookings


class Cars(list):

    def addCar(self, car):
        self.append(car)
