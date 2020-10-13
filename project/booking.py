from datetime import datetime


class Booking():
    def __init__(self, carID, customerID):
        self.carID = carID
        self.customerID = customerID
        self.begin = datetime.now()
        self.end = None
        self.total = 0

    def __str__(self):
        return f"{self.carID}, {self.customerID}, {self.begin}, {self.end}, {self.total}"

    def endBooking(self, price):
        """sets the end time and call function __calc_price__"""
        self.end = datetime.now()
        self.calc_price(price)
        print(f"Rent ended: {self.end}")
        self.transaction()

    def getID(self):
        """get booking.ID"""
        return f"[{self.carID}, {self.customerID}]"

    def getTotal(self):
        return self.total

    def transaction(self):
        print(f"total cost: {self.total}")

    def calc_price(self, price):
        """calculates the total price with the price per hour and the time between renting and returning the car"""
        self.total = f"{round((self.end - self.begin).total_seconds() / 60 * price, 2)}€"
