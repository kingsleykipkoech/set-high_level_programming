#!/usr/bin/python3
"""Magic class module"""
import math


class MagicClass:
    """Magic class matching bytecode"""

    def __init__(self, radius=0):
        """Initializes the Magic class"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Calculates the area"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Calculates the circumference"""
        return 2 * math.pi * self.__radius
