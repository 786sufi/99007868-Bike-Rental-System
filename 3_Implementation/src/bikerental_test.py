import unittest
from datetime import datetime, timedelta
from bikerental_project import BikeRental, Customer


class BikeRental_test(unittest.TestCase):

    def test_bike_rental_diplays_correct_stock(self):
        shop1 = BikeRental()
        shop2 = BikeRental(10)
        self.assertEqual(shop1.displaystock(), 0)
        self.assertEqual(shop2.displaystock(), 10)
    def test_rentbikeon_hourlybasis_for_negative_num_bikes(self):
        shop = BikeRental(10)
        self.assertEqual(shop.rentbikeon_hourlybasis(-1), None)
    def test_rentbikeon_hourlybasis_for_zero_num_bikes(self):
        shop = BikeRental(10)
        self.assertEqual(shop.rentbikeon_hourlybasis(0), None)
    def test_rentbikeon_hourlybasis_for_valid_positive_num_bikes(self):
        shop = BikeRental(10)
        hour = datetime.now().hour
        self.assertEqual(shop.rentbikeon_hourlybasis(2).hour, hour)
    def test_rentbikeon_hourlybasis_for_invalid_positive_num_bikes(self):
        shop = BikeRental(10)
        self.assertEqual(shop.rentbikeon_hourlybasis(11), None)

    def test_rentbikeon_dailybasis_for_negative_num_bikes(self):
        shop = BikeRental(10)
        self.assertEqual(shop.rentbikeon_dailybasis(-1), None)

    def test_rentbikeon_dailybasis_for_zero_num_bikes(self):
        shop = BikeRental(10)
        self.assertEqual(shop.rentbikeon_dailybasis(0), None)

    def test_rentbikeon_dailybasis_for_valid_positive_num_bikes(self):
        shop = BikeRental(10)
        hour = datetime.now().hour
        self.assertEqual(shop.rentbikeon_dailybasis(2).hour, hour)

    def test_rentbikeon_dailybasis_for_invalid_positive_num_bikes(self):
        shop = BikeRental(10)
        self.assertEqual(shop.rentbikeon_dailybasis(11), None)

    def test_rentbikeon_weeklybasis_for_negative_num_bikes(self):
        shop = BikeRental(10)
        self.assertEqual(shop.rentbikeon_weeklybasis(-1), None)

    def test_rentbikeon_weeklybasis_for_zero_num_bikes(self):
        shop = BikeRental(10)
        self.assertEqual(shop.rentbikeon_weeklybasis(0), None)

    def test_rentbikeon_weeklybasis_for_valid_positive_num_bikes(self):
        shop = BikeRental(10)
        hour = datetime.now().hour
        self.assertEqual(shop.rentbikeon_weeklybasis(2).hour, hour)

    def test_rentbikeon_weeklybasis_for_invalid_positive_num_bikes(self):
        shop = BikeRental(10)
        self.assertEqual(shop.rentbikeon_weeklybasis(11), None)

    def test_return_bike_for_invalid_rental_time(self):
        # create a shop and a customer
        shop = BikeRental(10)
        customer = Customer()

        # let the customer not rent a bike a try to return one.
        request = customer.return_bike()
        self.assertIsNone(shop.return_bike(request))

        # manually check return function with error values
        self.assertIsNone(shop.return_bike((0,0,0)))
    def test_return_bike_for_invalid_rental_basis(self):
        # create a shop and a customer
        shop = BikeRental(10)
        customer = Customer()
        # create valid rental_time and bikes
        customer.rental_time = datetime.now()
        customer.bikes = 3

        # create invalid rental_basis
        customer.rental_basis = 7

        request = customer.return_bike()
        self.assertEqual(shop.return_bike(request), 0)

    def test_return_bike_for_invalid_num_bikes(self):

        # create a shop and a customer
        shop = BikeRental(10)
        customer = Customer()

        # create valid rental_time and rental_basis
        customer.rental_time = datetime.now()
        customer.rental_basis = 1

        # create invalid bikes
        customer.bikes = 0

        request = customer.return_bike()
        self.assertIsNone(shop.return_bike(request))

    # def test_return_bike_for_valid_credentials(self):
    #     # create a shop and a various customers
    #     shop = BikeRental(50)
    #     customer1 = Customer()
    #     customer2 = Customer()
    #     customer3 = Customer()
    #     customer4 = Customer()
    #     customer5 = Customer()
    #     customer6 = Customer()

    #     # create valid rental_basis for each customer
    #     customer1.rental_basis = 1 # hourly
    #     customer2.rental_basis = 1 # hourly
    #     customer3.rental_basis = 2 # daily
    #     customer4.rental_basis = 2 # daily
    #     customer5.rental_basis = 3 # weekly
    #     customer6.rental_basis = 3 # weekly

    #     # create valid bikes for each customer
    #     customer1.bikes = 1
    #     customer2.bikes = 5 # eligible for family discount 30%
    #     customer3.bikes = 2
    #     customer4.bikes = 8
    #     customer5.bikes = 15
    #     customer6.bikes = 30

    #     # create past valid rental times for each customer
    #     customer1.rental_time = datetime.now() + timedelta(hours=-4)
    #     customer2.rental_time = datetime.now() + timedelta(hours=-23)
    #     customer3.rental_time = datetime.now() + timedelta(days=-4)
    #     customer4.rental_time = datetime.now() + timedelta(days=-13)
    #     customer5.rental_time = datetime.now() + timedelta(weeks=-6)
    #     customer6.rental_time = datetime.now() + timedelta(weeks=-12)

    #     # make all customers return their bikes
    #     request1 = customer1.return_bike()
    #     request2 = customer2.return_bike()
    #     request3 = customer3.return_bike()
    #     request4 = customer4.return_bike()
    #     request5 = customer5.return_bike()
    #     request6 = customer6.return_bike()

    #     # check if all of them get correct bill
    #     self.assertEqual(shop.return_bike(request1), None)
    #     self.assertEqual(shop.return_bike(request2), 402.5)
    #     self.assertEqual(shop.return_bike(request3), None)
    #     self.assertEqual(shop.return_bike(request4), None)
    #     self.assertEqual(shop.return_bike(request5), None)
    #     self.assertEqual(shop.return_bike(request6), None)

class CustomerTest(unittest.TestCase):
    def test_return_bike_with_valid_input(self):
        # create a customer
        customer = Customer()
        # create valid rental_time, rental_basis, bikes
        now = datetime.now()
        customer.rental_time = now
        customer.rental_basis = 1
        customer.bikes = 4

        self.assertEqual(customer.return_bike(),(now,1, 4))

    def test_return_bike_with_invalid_input(self):
        # create a customer
        customer = Customer()

        # create valid rental_basis and bikes
        customer.rental_basis = 1
        customer.bikes = 0

        # create invalid rental_time
        customer.rental_time =  0
        self.assertEqual(customer.return_bike(),(0,0,0))

if __name__ == '__main__':
    unittest.main()