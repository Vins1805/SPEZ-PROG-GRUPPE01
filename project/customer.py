import uuid


class Customer():
    def __init__(self, surname, name, driver_license, payment_methods):
        self.ID = uuid.uuid4()
        self.surname = surname
        self.name = name
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

        if self.driver_license == False:

            print("Please add a driver license")

        else:

            print(f"Renting {car.brand} {car.model}")
            car.setAvailability()

    def returnCar(self, car, booking):
        """call function setAvailability and call function booking.endBooking"""
        car.setAvailability()
        booking.endBooking(car.getPrice())
