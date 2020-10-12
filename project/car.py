import uuid


class Car():
    def __init__(self, color, brand, model, seats, location, price, available):
        self.ID = uuid.uuid4()
        self.color = color
        self.brand = brand
        self.model = model
        self.seats = seats
        self.location = location
        self.price = price
        self.available = available
        self.bookings = list()

    def __str__(self):
        return f"{self.ID}, {self.model}, {self.seats}, {self.location}, {self.price}, {self.available}"

    def __repr__(self):
        return {'ID': self.ID, 'Model': self.model, 'Seats': self.seats, 'Location': self.location, 'Price': self.price}

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
        self.bookings.append(booking.getID())



    def showBookings(self):
        """show booking list of one car"""
        return self.bookings