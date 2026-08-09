#!/usr/bin/python3
"""Unit tests for models/base.py."""
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Test cases for Base class."""

    def setUp(self):
        """Reset private class attribute before each test."""
        Base._Base__nb_objects = 0

    def test_id_auto_increment(self):
        """Test auto incrementing id when id is None."""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_id_custom(self):
        """Test custom id assignment."""
        b = Base(89)
        self.assertEqual(b.id, 89)

    def test_id_mixed(self):
        """Test mix of auto increment and custom id."""
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 12)
        self.assertEqual(b3.id, 2)

    def test_to_json_string_none(self):
        """Test to_json_string with None."""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_empty(self):
        """Test to_json_string with empty list."""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_valid(self):
        """Test to_json_string with valid dictionaries."""
        d = [{'id': 1, 'width': 10, 'height': 2}]
        json_s = Base.to_json_string(d)
        self.assertIsInstance(json_s, str)
        self.assertIn('"id": 1', json_s)

    def test_from_json_string_none(self):
        """Test from_json_string with None."""
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty(self):
        """Test from_json_string with empty string."""
        self.assertEqual(Base.from_json_string(""), [])
        self.assertEqual(Base.from_json_string("  "), [])

    def test_from_json_string_valid(self):
        """Test from_json_string with valid JSON string."""
        json_s = '[{"id": 89, "width": 10, "height": 4}]'
        res = Base.from_json_string(json_s)
        self.assertEqual(res, [{'id': 89, 'width': 10, 'height': 4}])

    def test_save_to_file_none(self):
        """Test save_to_file with None."""
        Rectangle.save_to_file(None)
        self.assertTrue(os.path.exists("Rectangle.json"))
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")
        os.remove("Rectangle.json")

    def test_save_to_file_empty(self):
        """Test save_to_file with empty list."""
        Square.save_to_file([])
        self.assertTrue(os.path.exists("Square.json"))
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")
        os.remove("Square.json")

    def test_save_to_file_valid(self):
        """Test save_to_file with valid instances."""
        r1 = Rectangle(10, 7, 2, 8, 1)
        Rectangle.save_to_file([r1])
        self.assertTrue(os.path.exists("Rectangle.json"))
        with open("Rectangle.json", "r") as f:
            self.assertIn('"id": 1', f.read())
        os.remove("Rectangle.json")

    def test_create_rectangle(self):
        """Test create method for Rectangle."""
        r_dict = {'id': 1, 'width': 3, 'height': 5, 'x': 1, 'y': 2}
        r = Rectangle.create(**r_dict)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 3)
        self.assertEqual(r.height, 5)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 2)

    def test_create_square(self):
        """Test create method for Square."""
        s_dict = {'id': 2, 'size': 4, 'x': 1, 'y': 3}
        s = Square.create(**s_dict)
        self.assertEqual(s.id, 2)
        self.assertEqual(s.size, 4)
        self.assertEqual(s.x, 1)
        self.assertEqual(s.y, 3)

    def test_load_from_file_no_file(self):
        """Test load_from_file when file does not exist."""
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_load_from_file_valid(self):
        """Test load_from_file when file exists."""
        r1 = Rectangle(10, 7, 2, 8, 1)
        Rectangle.save_to_file([r1])
        output = Rectangle.load_from_file()
        self.assertEqual(len(output), 1)
        self.assertEqual(output[0].id, 1)
        self.assertEqual(output[0].width, 10)
        os.remove("Rectangle.json")

    def test_csv_save_and_load(self):
        """Test save_to_file_csv and load_from_file_csv."""
        r1 = Rectangle(10, 7, 2, 8, 1)
        Rectangle.save_to_file_csv([r1])
        output = Rectangle.load_from_file_csv()
        self.assertEqual(len(output), 1)
        self.assertEqual(output[0].id, 1)
        self.assertEqual(output[0].width, 10)
        os.remove("Rectangle.csv")


if __name__ == "__main__":
    unittest.main()
