# SPEZ-PROG-GRUPPE01

## Links

### [github]
### [google-doc]

---

# History

## Lecture Sheet 1

* added following files:
    * booking.py
    * car.py
    * customer.py
    * main.py
    * car_data.json
    * customer_data.json

### Structure

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

---

## Lecture Sheet 2

New features:

* Creating an Docker Image
* Connecting with Docker
* Creating a RESTful Server.py with Flask

Files added:

* Server.py - interface between frontend and backend

Changes in Classes:

* Customer()
    * addBooking(booking)
    * showBookings()
    * toJSON()
* Booking()
    * toJSON()
* Car()
    * toJSON()
* Customers(list)
    * addCustomer(customer)
* Cars(list)
    * addCar(car)
* Bookings(list)
    * addBooking(booking)

Docker:

Drawbacks:

* Complicated Testing: Due to generating a new image and running docker to see the results of the updated code.

Alternative to Docker:

* Right now, an alternative would be to just not use Docker. We have our web server with flask and we can access every function with localhost

Szenario using Postman:

* GET: localhost:4000/show_customers
    * returns the list of all customers
* GET: localhost:4000/show_cars
    * returns the list of all cars
* POST: localhost:4000/book_car?car_id=2&customer_name=Mueller
    * Keys: car_id, customer_name; Example values: Mueller, 2
    * customer Mueller books a car with the id: 2, if the id exists, the car is available and Mueller has a driver license
    * The available state of the car changes to False 
    * The renting state of the customer changes to True
    * if another customer tries to book a car with the id: 2, he gets an Error message
* GET: localhost:4000/show_bookings
    * returns the list of all bookings; Example: Mueller's booking got added to the booking list



[github]: https://github.com/s0551489/SPEZ-PROG-GRUPPE01
[google-doc]: https://docs.google.com/document/d/1Atfu4mfd_iCKmvobBXp0uDsa3Y7Ef8PWUSXOQ4B3fmU/edit?usp=sharing

