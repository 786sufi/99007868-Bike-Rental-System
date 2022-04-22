from bikerental_project import*
def main():
    """function"""
    shop = BikeRental(100)
    customer = Customer()

    while True:
        print("""
        ====== Bike Rental Shop =======
        1. Display available bikes
        2. Request a bike on hourly basis $5
        3. Request a bike on daily basis $20
        4. Request a bike on weekly basis $60
        5. Return a bike
        6. Exit
        """)

        choice = input("Enter choice: ")
        try:
            choice = int(choice)
        except ValueError:
            print("That's not an int!")
            continue
        if choice == 1:
            shop.displaystock()
        elif choice == 2:
            customer.rental_time =shop.rentbikeon_hourlybasis(customer.request_bike())
            customer.rental_basis = 1

        elif choice == 3:
            customer.rental_time = shop.rentbikeon_dailybasis(customer.request_bike())
            customer.rental_basis = 2

        elif choice == 4:
            customer.rental_time = shop.rentbikeon_weeklybasis(customer.request_bike())
            customer.rental_basis = 3

        elif choice == 5:
            customer.bill = shop.return_bike(customer.return_bike())
            customer.rental_basis, customer.rental_time, customer.bikes = 0,0,0
        elif choice == 6:
            break
        else:
            print("Invalid input. Please enter number between 1-6 ")
            print("Thank you for using the bike rental system.")

main()
