from rental import Rental
from movie import Movie
import logging


class Customer:
    """
       A customer who rents movies.
       The customer object holds information about the
       movies rented for the current billing period,
       and can print a statement of his rentals.
    """

    def __init__(self, name: str):
        """ Initialize a new customer."""
        self.name = name
        self.rentals = []

    def add_rental(self, rental: Rental):
        if rental not in self.rentals:
            self.rentals.append(rental)

    def compute_rental_points(self) -> int:
        total_point = 0
        for rental in self.rentals:
            total_point += rental.get_rental_points()
        return total_point

    def compute_total_charge(self) -> int:
        total_charge = 0
        for rental in self.rentals:
            total_charge += rental.get_charge()
        return total_charge

    def statement(self):
        """
            Print all the rentals in current period, 
            along with total charges and reward points.
            Returns:
                the statement as a String
        """
        statement = f"Rental Report for {self.name}\n\n"
        fmt = "{:32s}    {:4s} {:6s}\n"
        statement += fmt.format("Movie Title", "Days", "Price")
        fmt = "{:32s}   {:4d} {:6.2f}\n"

        for rental in self.rentals:
            statement += fmt.format(rental.get_title(),
                                    rental.days_rented,
                                    rental.get_charge()
                                    )

        # footer: summary of charges
        statement += "\n"
        statement += "{:32s} {:6s} {:6.2f}\n".format(
            "Total Charges", "", self.compute_total_charge())
        statement += "Frequent Renter Points earned: {}\n".format(
            self.compute_rental_points())

        return statement


if __name__ == "__main__":
    customer = Customer("Edward Snowden")
    print(customer.statement())
    movie = Movie("Hacker Noon", Movie.REGULAR)
    customer.add_rental(Rental(movie, 2))
    movie = Movie("CitizenFour", Movie.NEW_RELEASE)
    customer.add_rental(Rental(movie, 3))
    print(customer.statement())
