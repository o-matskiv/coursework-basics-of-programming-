from adt import *


class Ward():
    """docstring for Ward."""

    def __init__(self, name):
        self.name = name
        self.schools = Array()
        self.number_crimes = 0
        self.price = None

    def add_school(self, school):
        """
        Adds school to Ward.
        :param school: school to be added.
        """
        if isinstance(school, str):
            self.schools.add(school)
        else:
            raise TypeError

    def add_number_crimes(self, number):
        """
        Adds number of crimes to Ward.
        :param number: number of crimes to be added.
        """
        if isinstance(number, int):
            self.number_crimes += number
        else:
            raise TypeError

    def set_price(self, price):
        """
        Sets average price on Ward.
        :param price: price to be set.
        """
        if isinstance(price, int):
            self.price = price
        else:
            raise TypeError

    def get_name(self):
        """
        Returnss the name of Ward.
        (Ward) -> str
        :return: Ward name.
        """
        return self.name

    def get_number_of_schools(self):
        """
        Returns the number of schools in this Ward.
        (Ward) -> int
        :return: number of schools in Ward.
        """
        return len(self.schools)

    def get_number_of_crimes(self):
        """
        Returns the number of crimes in this Ward.
        (Ward) -> int
        :return: number of crimes in Ward.
        """
        return self.number_crimes

    def get_price(self):
        """
        Returns the average price for appartments in this Ward.
        (Ward) -> int
        :return: number of schools in Ward.
        """
        return self.price

    def __str__(self):
        """
        (Ward) -> str
        :return: string representation of Array
        """
        result = self.get_name()
        result += ':\n\tNumber of schools: ' + str(self.number_of_schools())
        result += '\n\tNumber of crimes: ' + str(self.number_of_crimes())
        result += '\n\tAverage price: ' + str(self.get_price())
        return result

    def __eq__(self, other):
        """
        Checks if two Wards are equal
        (Ward,Ward) -> Bool
        :param other: another Ward to be compared
        :return: True if Wards are equal and False otherwise.
        """
        return self.get_name() == other.get_name()
