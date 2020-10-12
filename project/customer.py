import uuid

class Customer():
    def __init__(self, driver_license, payment_methods):
        self.ID = uuid.uuid4()
        self.driver_license = driver_license
        self.payment_methods = payment_methods

    def __str__(self):
        return f"{self.ID}, {self.driver_license}, {self.payment_methods}"

    def __repr__(self):
        return {"ID": self.ID, "Driver license": self.driver_license, "Payment methods": self.payment_methods}

    def getID(self):
        """get customer.ID"""
        return self.ID

    def setCustomer(self):
        pass

    def rentCar(self, car):
        """call function setAvailability"""
        car.setAvailability()

    def returnCar(self, car, booking):
        """call function setAvailability and call function booking.endBooking"""
        car.setAvailability()
        booking.endBooking(car.getPrice())