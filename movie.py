from enum import Enum

from datetime import datetime


class PriceCode(Enum):
    """An enumeration for different kinds of movies and their behavior"""
    new_release = {"price": lambda days: 3.0*days,
                   "frp": lambda days: days
                   }
    regular = {"price": lambda days: (1.5 * (days - 2)) if days > 2 else 2.0,
               "frp": lambda days: 1
               }
    childrens = {"price": lambda days: (1.5 * (days - 3)) if days > 3 else 1.5,
                 "frp": lambda days: 1
                 }

    def frequent_rental_point(self, days: int) -> int:
        """Return the renter points for a given number of days"""
        point = self.value["frp"]    # the enum member's price formula
        return point(days)

    def price(self, days: int) -> float:
        "Return the rental price for a given number of days"""
        pricing = self.value["price"]    # the enum member's price formula
        return pricing(days)

    @staticmethod
    def for_movie(movie):
        new_release = movie.get_year() == str(datetime.now().year)
        children = 'Children' in movie.get_genre()
        if new_release:
            return PriceCode.childrens
        elif children:
            return PriceCode.new_release
        return PriceCode.regular


class Movie:
    """
    A movie available for rent.
    """

    def __init__(self, title, year, genre):
        # Initialize a new movie.
        self.__title = title
        self.__price_code = ""
        self.__year = year
        self.__genre = genre

    def get_price_code(self):
        # get the price code
        return self.__price_code

    def set_price_code(self, value):
        self.__price_code = value

    def get_title(self):
        return self.__title

    def get_year(self):
        return self.__year

    def get_genre(self):
        return self.__genre

    def is_genre(self, genre):
        return True if genre in self.__genre \
            else False

    def __str__(self):
        return self.__title
