#!/usr/bin/python3
"""MyInt module"""


class MyInt(int):
    """A rebel int class with inverted == and != operators"""

    def __eq__(self, other):
        """Inverted equality - returns True when not equal"""
        return super().__ne__(other)

    def __ne__(self, other):
        """Inverted inequality - returns True when equal"""
        return super().__eq__(other)
