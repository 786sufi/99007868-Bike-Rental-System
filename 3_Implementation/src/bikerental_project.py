"""code"""
import datetime

class BikeRental:
    """_summary_"""
    def __init__(self,stock=0):
        """
        Our constructor class that instantiates bike rental shop.
        """

        self.stock = stock

    def displaystock(self):
        """
        Displays the bikes currently available for rent in the shop.
        """

        print("We have currently {} bikes available to rent.".format(self.stock))
        return self.stock

    def rentbikeon_hourlybasis(self, n_a):
        """
        Rents a bike on hourly basis to a customer.
        """
        if n_a <= 0:
            print("Number of bikes should be positive!")
            return None
        elif n_a > self.stock:
            print("Sorry! We have currently {} bikes available to rent.".format(self.stock))
            return None
        else:
            now = datetime.datetime.now()
            print("You have rented a {} bike(s) on hourly basis at {} hours.".format(n_a,now.hour))
            print("You will be charged $5 for each hour per bike.")
            print("We hope that you enjoy our service.")
            self.stock -= n_a
            return now
    def rentbikeon_dailybasis(self, n_a):
        """
        Rents a bike on daily basis to a customer.
        """
        if n_a <= 0:
            print("Number of bikes should be positive!")
            return None

        elif n_a > self.stock:
            print("Sorry! We have currently {} bikes available to rent.".format(self.stock))
            return None
        else:
            now = datetime.datetime.now()
            print("You have rented {} bike(s) on daily basis at {} hours.".format(n_a, now.hour))
            print("You will be charged $20 for each day per bike.")
            print("We hope that you enjoy our service.")
            self.stock -= n_a
            return now

    def rentbikeon_weeklybasis(self, n_a):
        """
        Rents a bike on weekly basis to a customer.
        """
        if n_a <= 0:
            print("Number of bikes should be positive!")
            return None

        elif n_a > self.stock:
            print("Sorry! We have currently {} bikes available to rent.".format(self.stock))
            return None
        else:
            now = datetime.datetime.now()
            print("You have rented {} bike(s) on weekly basis at {} hours.".format(n_a, now.hour))
            print("You will be charged $60 for each week per bike.")
            print("We hope that you enjoy our service.")
            self.stock -= n_a
            return now

    def return_bike(self, request):
        """
        1. Accept a rented bike from a customer
        2. Replensihes the inventory
        3. Return a bill
        """
        rental_time, rental_basis, num_bikes = request
        bill = 0

        if rental_time and rental_basis and num_bikes:
            self.stock += num_bikes
            now = datetime.datetime.now()
            rental_period = now - rental_time
            # hourly bill calculation
            if rental_basis == 1:
                bill = round(rental_period.seconds / 3600) * 5 * num_bikes
            # daily bill calculation
            elif rental_basis == 2:
                bill = round(rental_period.days) * 20 * num_bikes
            # weekly bill calculation
            elif rental_basis == 3:
                bill = round(rental_period.days / 7) * 60 * num_bikes
        if (3 <= num_bikes <= 5):
            print("You are eligible for Family rental promotion of 30% discount")
            bill = bill * 0.7
            print("Thanks for returning your bike. Hope you enjoyed our service!")
            print("That would be ${}".format(bill))
            return bill
        else:
            print("Are you sure you rented a bike with us?")
            return None

class Customer:
    """_summary_
    """

    def __init__(self):
        """
        Our constructor method which instantiates various customer objects.
        """
        self.bikes = 0
        self.rental_basis = 0
        self.rental_time = 0
        self.bill = 0
    def request_bike(self):
        """
        Takes a request from the customer for the number of bikes.
        """
        bikes = input("How many bikes would you like to rent?")
        try:
            bikes = int(bikes)
        except ValueError:
            print("That's not a positive integer!")
            return -1

        if bikes < 1:
            print("Invalid input. Number of bikes should be greater than zero!")
            return -1
        else:
            self.bikes = bikes
        return self.bikes

    def return_bike(self):
        """
        Allows customers to return their bikes to the rental shop.
        """
        if self.rental_basis and self.rental_time and self.bikes:
            return self.rental_time, self.rental_basis, self.bikes
        else:
            return 0,0,0