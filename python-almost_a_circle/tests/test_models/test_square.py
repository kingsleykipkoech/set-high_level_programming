#!/usr/bin/python3
"""Unit tests for models/square.py."""
import unittest
import os
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

    def test_square_one_arg(self):
        """Test of Square(1) exists."""
        s = Square(1)
        self.assertEqual(s.size, 1)

    def test_square_two_args(self):
        """Test of Square(1, 2) exists."""
        s = Square(1, 2)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 2)

    def test_square_three_args(self):
        """Test of Square(1, 2, 3) exists."""
        s = Square(1, 2, 3)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    def test_square_four_args(self):
        """Test of Square(1, 2, 3, 4) exists."""
        s = Square(1, 2, 3, 4)
        self.assertEqual(s.id, 4)

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

    def test_string_size(self):
        """Test of Square("1") exists."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("1")

    def test_string_x(self):
        """Test of Square(1, "2") exists."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "2")

    def test_string_y(self):
        """Test of Square(1, 2, "3") exists."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, "3")

    def test_negative_size(self):
        """Test of Square(-1) exists."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1)

    def test_negative_x(self):
        """Test of Square(1, -2) exists."""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(1, -2)

    def test_negative_y(self):
        """Test of Square(1, 2, -3) exists."""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(1, 2, -3)

    def test_zero_size(self):
        """Test of Square(0) exists."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)

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
            s = Square(5)
            s.size = "9"

    def test_size_value_errors(self):
        """Test ValueError exceptions for size."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s = Square(5)
            s.size = -5

    def test_area(self):
        """Test area method."""
        s = Square(5)
        self.assertEqual(s.area(), 25)

    def test_str(self):
        """Test of __str__() for Square exists."""
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

    def test_update_no_args(self):
        """Test of update() in Square exists."""
        s = Square(5)
        s.update()
        self.assertEqual(str(s), "[Square] (1) 0/0 - 5")

    def test_update_id(self):
        """Test of update(89) in Square exists."""
        s = Square(5)
        s.update(89)
        self.assertEqual(s.id, 89)

    def test_update_id_size(self):
        """Test of update(89, 1) in Square exists."""
        s = Square(5)
        s.update(89, 1)
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 1)

    def test_update_id_size_x(self):
        """Test of update(89, 1, 2) in Square exists."""
        s = Square(5)
        s.update(89, 1, 2)
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 2)

    def test_update_id_size_x_y(self):
        """Test of update(89, 1, 2, 3) in Square exists."""
        s = Square(5)
        s.update(89, 1, 2, 3)
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    def test_update_kwargs_id(self):
        """Test of update(**{ 'id': 89 }) in Square exists."""
        s = Square(5)
        s.update(**{'id': 89})
        self.assertEqual(s.id, 89)

    def test_update_kwargs_id_size(self):
        """Test of update(**{ 'id': 89, 'size': 1 }) in Square."""
        s = Square(5)
        s.update(**{'id': 89, 'size': 1})
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 1)

    def test_update_kwargs_id_size_x(self):
        """Test of update(**{ 'id': 89, 'size': 1, 'x': 2 }) in Square."""
        s = Square(5)
        s.update(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 2)

    def test_update_kwargs_id_size_x_y(self):
        """Test of update(**{ 'id': 89, 'size': 1, 'x': 2, 'y': 3 })."""
        s = Square(5)
        s.update(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    def test_to_dictionary(self):
        """Test of to_dictionary() in Square exists."""
        s = Square(10, 2, 1, 1)
        s_dict = s.to_dictionary()
        expected = {'id': 1, 'x': 2, 'size': 10, 'y': 1}
        self.assertEqual(s_dict, expected)

    def test_create_id(self):
        """Test of Square.create(**{ 'id': 89 }) in Square exists."""
        s = Square.create(**{'id': 89})
        self.assertEqual(s.id, 89)

    def test_create_id_size(self):
        """Test of Square.create(**{ 'id': 89, 'size': 1 }) in Square."""
        s = Square.create(**{'id': 89, 'size': 1})
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 1)

    def test_create_id_size_x(self):
        """Test of Square.create(**{ 'id': 89, 'size': 1, 'x': 2 })."""
        s = Square.create(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 2)

    def test_create_id_size_x_y(self):
        """Test of Square.create(**{ 'id': 89, 'size': 1, 'x': 2, 'y': 3})."""
        s = Square.create(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    def test_save_to_file_none(self):
        """Test of Square.save_to_file(None) in Square exists."""
        Square.save_to_file(None)
        self.assertTrue(os.path.exists("Square.json"))
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")
        os.remove("Square.json")

    def test_save_to_file_empty(self):
        """Test of Square.save_to_file([]) in Square exists."""
        Square.save_to_file([])
        self.assertTrue(os.path.exists("Square.json"))
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")
        os.remove("Square.json")

    def test_save_to_file_valid(self):
        """Test of Square.save_to_file([Square(1)]) in Square exists."""
        Square.save_to_file([Square(1)])
        self.assertTrue(os.path.exists("Square.json"))
        with open("Square.json", "r") as f:
            content = f.read()
            self.assertIn('"size": 1', content)
        os.remove("Square.json")

    def test_load_from_file_no_file(self):
        """Test of Square.load_from_file() when file doesn't exist."""
        if os.path.exists("Square.json"):
            os.remove("Square.json")
        result = Square.load_from_file()
        self.assertEqual(result, [])

    def test_load_from_file_exists(self):
        """Test of Square.load_from_file() when file exists."""
        s1 = Square(5, 0, 0, 1)
        Square.save_to_file([s1])
        output = Square.load_from_file()
        self.assertEqual(len(output), 1)
        self.assertEqual(output[0].id, 1)
        self.assertEqual(output[0].size, 5)
        os.remove("Square.json")


if __name__ == "__main__":
    unittest.main()
