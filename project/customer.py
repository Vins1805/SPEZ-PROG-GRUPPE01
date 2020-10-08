class Customer():
    def __init__(self, ID, driver_license, payment_methods):
        self.ID = ID
        self.driver_license = driver_license
        self.payment_methods = payment_methods

    def getCustomer(self):
        return {
            "ID": self.ID,
            "Driver license": self.driver_license,
            "Payment methods": self.payment_methods
        }

    def setCustomer(self):
        pass

    def book(self):
        pass
