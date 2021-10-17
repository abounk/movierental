import re
import unittest
from customer import Customer
from rental import Rental
from movie import Movie


class CustomerTest(unittest.TestCase):
    """ Tests of the Customer class"""

    def setUp(self):
        """Test fixture contains:

        c = a customer
        movies = list of some movies
        """
        self.c = Customer("Movie Mogul")
        self.new_movie = Movie("Mulan", Movie.NEW_RELEASE)
        self.regular_movie = Movie("CitizenFour", Movie.REGULAR)
        self.childrens_movie = Movie("Frozen", Movie.CHILDRENS)

    def test_billing(self):
        """ Test rental billing """
        # rental for new released movie
        new_release = Rental(self.new_movie, 3)
        amount_1, point_1 = self.c.billing(new_release)
        # rental for regular movie with more than 2 rental days
        regular = Rental(self.regular_movie, 3)
        amount_2, point_2 = self.c.billing(regular)
        # rental for regular movie with less than 2 rental days
        regular_2 = Rental(self.regular_movie, 1)
        amount_3, point_3 = self.c.billing(regular_2)
        # rental for childrens movie with more than 3 rental days
        childrens = Rental(self.childrens_movie, 4)
        amount_4, point_4 = self.c.billing(childrens)
        # rental for childrens movie with less than 3 rental days
        childrens_2 = Rental(self.childrens_movie, 2)
        amount_5, point_5 = self.c.billing(childrens_2)

        self.assertEqual((9, 3), (amount_1, point_1))
        self.assertEqual((3.5, 1), (amount_2, point_2))
        self.assertEqual((2.0, 1), (amount_3, point_3))
        self.assertEqual((3.0, 1), (amount_4, point_4))
        self.assertEqual((1.5, 1), (amount_5, point_5))

    def test_statement(self):
        stmt = self.c.statement()
        # visual testing
        print(stmt)
        # get total charges from statement using a regex
        pattern = r".*Total [Cc]harges\s+(\d+\.\d\d).*"
        matches = re.match(pattern, stmt, flags=re.DOTALL)
        self.assertIsNotNone(matches)
        self.assertEqual("0.00", matches[1])
        # add a rental
        self.c.add_rental(Rental(self.new_movie, 4))  # days
        stmt = self.c.statement()
        matches = re.match(pattern, stmt.replace('\n', ''), flags=re.DOTALL)
        self.assertIsNotNone(matches)
        self.assertEqual("12.00", matches[1])
