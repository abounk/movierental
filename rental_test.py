from datetime import datetime
import unittest
from customer import Customer
from rental import Rental
from movie import Movie, PriceCode
from movie_catalog import MovieCatalog


class RentalTest(unittest.TestCase):

    def setUp(self):
        self.current_year = datetime.now().year
        self.new_movie = Movie("Mulan", self.current_year, [
                               'Action', 'Adventure'])
        self.regular_movie = Movie(
            "CitizenFour", self.current_year - 1, ['Documentary'])
        self.childrens_movie = Movie(
            "Frozen", self.current_year - 1, ['Action', 'Adventure', 'Children'])

    def test_movie_attributes(self):
        """trivial test to catch refactoring errors or change in API of Movie"""
        m = Movie("CitizenFour", self.current_year - 1, ['Documentary'])
        self.assertEqual("CitizenFour", m.get_title())

    def test_rental_price(self):
        test_cases = [
            (Rental(self.new_movie, 1), 3.0),
            (Rental(self.new_movie, 5), 15.0),
            (Rental(self.regular_movie, 3), 1.5),
            (Rental(self.regular_movie, 1), 2.0),
            (Rental(self.childrens_movie, 4), 1.5),
            (Rental(self.childrens_movie, 2), 1.5)
        ]
        for test in test_cases:
            with self.subTest():
                self.assertEqual(test[0].get_charge(), test[1])

    def test_rental_points(self):
        test_cases = [
            (Rental(self.new_movie, 1), 1),
            (Rental(self.new_movie, 5), 5),
            (Rental(self.regular_movie, 3), 1),
            (Rental(self.childrens_movie, 4), 1)
        ]
        for test in test_cases:
            with self.subTest():
                self.assertEqual(test[0].get_rental_points(), test[1])
