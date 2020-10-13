# SPEZ-PROG-GRUPPE01

## Links

### [github]
### [google-doc]

---

## History

### Lecture Sheet 1

* added following files:
    * booking.py
    * car.py
    * customer.py
    * main.py
    * car_data.json
    * customer_data.json

---

## Structure

Files:

* customer.py - Customer Class
* car.py - Car Class
* booking.py - Booking Class
* main.py - Main Programm
* README.md - Links to github and google-doc
* car_data.json - JSON test data for cars
* customer_data.json - JSON test data for customers

Classes:

* Customer(surname, name, driver_license, payment_methods)
* getID() - returns customer_id
* rentCar(car) - if driver_license == True call function car.setAvailability()
* returnCar(car, booking) - call functions car.setAvailability() and booking.endBooking(...)
* Car(self, color, brand, model, seats, location, price, available)
* getID() - returns carID
* getPrice() - returns price per minute 
* setAvailability() - toogle the availability  (boolean)
* addBooking(booking) - car gets assigned one booking to a list where all bookings from one car are stored
* showBookings() - show booking list of one car
* Booking(carID, customerID)
* endBooking(price) - set end time, call functions calc_price(price) and transaction()
* getID() - returns booking_id
* getTotal() - returns total price
* transaction() - returns total cost as string
* calc_price(price) - calculates the total price


[github]: https://github.com/s0551489/SPEZ-PROG-GRUPPE01
[google-doc]: https://docs.google.com/document/d/1Atfu4mfd_iCKmvobBXp0uDsa3Y7Ef8PWUSXOQ4B3fmU/edit?usp=sharing

