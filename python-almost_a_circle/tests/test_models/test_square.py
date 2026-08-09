#!/usr/bin/python3
"""Unit tests for models/square.py."""
import unittest
import io
import sys
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test cases for Square class."""

    def setUp(self):
        """Reset Base instance counter before each test."""
        Base._Base__nb_objects = 0

    def test_inheritance(self):
        """Test Square inherits from Rectangle and Base."""
        s = Square(5)
        self.assertIsInstance(s, Rectangle)
        self.assertIsInstance(s, Base)

    def test_init_defaults(self):
        """Test constructor with default x, y, id."""
        s = Square(5)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)
        self.assertEqual(s.id, 1)

    def test_init_all_args(self):
        """Test constructor with all arguments."""
        s = Square(5, 2, 3, 10)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)
        self.assertEqual(s.id, 10)

    def test_size_setter(self):
        """Test size getter and setter."""
        s = Square(5)
        s.size = 10
        self.assertEqual(s.size, 10)
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)

    def test_size_type_errors(self):
        """Test TypeError exceptions for size."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("9")
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s = Square(5)
            s.size = "9"

    def test_size_value_errors(self):
        """Test ValueError exceptions for size."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-5)

    def test_area(self):
        """Test area method."""
        s = Square(5)
        self.assertEqual(s.area(), 25)

    def test_str(self):
        """Test __str__ method output."""
        s1 = Square(5)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 5")
        s2 = Square(2, 2, 1, 12)
        self.assertEqual(str(s2), "[Square] (12) 2/1 - 2")

    def test_display(self):
        """Test display method."""
        s = Square(2, 2)
        captured = io.StringIO()
        sys.stdout = captured
        s.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), "  ##\n  ##\n")

    def test_update_args(self):
        """Test update method with *args."""
        s = Square(5)
        s.update(10)
        self.assertEqual(s.id, 10)
        s.update(1, 2)
        self.assertEqual(s.size, 2)
        s.update(1, 2, 3)
        self.assertEqual(s.x, 3)
        s.update(1, 2, 3, 4)
        self.assertEqual(s.y, 4)

    def test_update_kwargs(self):
        """Test update method with **kwargs."""
        s = Square(5)
        s.update(x=12)
        self.assertEqual(s.x, 12)
        s.update(size=7, y=1)
        self.assertEqual(s.size, 7)
        self.assertEqual(s.y, 1)
        s.update(size=7, id=89, y=1)
        self.assertEqual(s.id, 89)

    def test_to_dictionary(self):
        """Test to_dictionary method."""
        s = Square(10, 2, 1, 1)
        s_dict = s.to_dictionary()
        expected = {'id': 1, 'x': 2, 'size': 10, 'y': 1}
        self.assertEqual(s_dict, expected)


if __name__ == "__main__":
    unittest.main()
