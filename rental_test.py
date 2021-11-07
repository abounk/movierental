import unittest
from customer import Customer
from rental import Rental
from movie import Movie, PriceCode
from movie_catalog import MovieCatalog


class RentalTest(unittest.TestCase):

    def setUp(self):
        self.new_movie = Movie("Mulan", 2021, ['Action', 'Adventure'])
        self.regular_movie = Movie("CitizenFour", 2013, ['Documentary'])
        self.childrens_movie = Movie(
            "Frozen", 2020, ['Action', 'Adventure', 'Children'])

    def test_movie_attributes(self):
        """trivial test to catch refactoring errors or change in API of Movie"""
        m = Movie("CitizenFour", 2013, ['Documentary'])
        self.assertEqual("CitizenFour", m.get_title())

    def test_rental_price(self):
        rental = Rental(self.new_movie, 1, PriceCode.new_release)
        self.assertEqual(rental.get_charge(), 3.0)
        rental = Rental(self.new_movie, 5, PriceCode.new_release)
        self.assertEqual(rental.get_charge(), 15.0)
        rental = Rental(self.regular_movie, 3, PriceCode.regular)
        self.assertEqual(rental.get_charge(), 1.5)
        rental = Rental(self.regular_movie, 1, PriceCode.regular)
        self.assertEqual(rental.get_charge(), 2.0)
        rental = Rental(self.childrens_movie, 4, PriceCode.childrens)
        self.assertEqual(rental.get_charge(), 1.5)
        rental = Rental(self.childrens_movie, 2, PriceCode.childrens)
        self.assertEqual(rental.get_charge(), 1.5)

    def test_rental_points(self):
        rental = Rental(self.new_movie, 1, PriceCode.new_release)
        self.assertEqual(rental.get_rental_points(), 1)
        rental = Rental(self.new_movie, 5, PriceCode.new_release)
        self.assertEqual(rental.get_rental_points(), 5)
        rental = Rental(self.regular_movie, 3, PriceCode.regular)
        self.assertEqual(rental.get_rental_points(), 1)
        rental = Rental(self.childrens_movie, 4, PriceCode.childrens)
        self.assertEqual(rental.get_rental_points(), 1)
