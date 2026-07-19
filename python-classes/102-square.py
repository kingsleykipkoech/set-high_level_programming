#!/usr/bin/python3
"""Square module"""


class Square:
    """Square class"""

    def __init__(self, size=0):
        """Initializes a Square"""
        self.size = size

    @property
    def size(self):
        """Retrieves the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size"""
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates area of the square"""
        return self.__size ** 2

    def __eq__(self, other):
        """Equal comparison"""
        return self.area() == other.area()

    def __ne__(self, other):
        """Not equal comparison"""
        return self.area() != other.area()

    def __lt__(self, other):
        """Less than comparison"""
        return self.area() < other.area()

    def __le__(self, other):
        """Less than or equal comparison"""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Greater than comparison"""
        return self.area() > other.area()

    def __ge__(self, other):
        """Greater than or equal comparison"""
        return self.area() >= other.area()
