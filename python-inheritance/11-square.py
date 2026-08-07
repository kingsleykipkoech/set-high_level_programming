#!/usr/bin/python3
"""Square module"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A Square class with custom str representation"""

    def __init__(self, size):
        """Initializes a Square with a validated size"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Returns the area of the square"""
        return self.__size ** 2

    def __str__(self):
        """Returns the square description"""
        return "[Square] {}/{}".format(self.__size, self.__size)
