class Car():
    def __init__(self, ID, model, seats, location, price):
        self.ID = ID
        self.model = model
        self.seats = seats
        self.location = location
        self.price = price

    def getCar(self):
        return {
            "ID": self.ID,
            "Model": self.model,
            "Seats": self.seats,
            "Location": self.location,
            "Price": self.price
        }

    def setID(self):
        pass

    def setModel(self):
        pass

    #...

    def availablity(self):
        pass

    def updateLocation(self):
        pass

    def openCar(self):
        pass

    def closeCar(self):
        pass
