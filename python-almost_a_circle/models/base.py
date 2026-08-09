#!/usr/bin/python3
"""Module for Base class."""
import csv
import json
import os


class Base:
    """Base class for all other classes in this project."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor for Base class.

        Args:
            id (int, optional): Identifier for instance. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns JSON string representation of list_dictionaries.

        Args:
            list_dictionaries (list): list of dictionaries

        Returns:
            str: JSON string representation
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes JSON string representation of list_objs to a file.

        Args:
            list_objs (list): list of Base instances
        """
        filename = "{}.json".format(cls.__name__)
        list_dicts = []
        if list_objs is not None:
            list_dicts = [obj.to_dictionary() for obj in list_objs]
        with open(filename, "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Returns list of JSON string representation json_string.

        Args:
            json_string (str): string representing list of dicts

        Returns:
            list: list represented by json_string
        """
        if json_string is None or len(json_string.strip()) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set.

        Args:
            dictionary (dict): key/value pairs of attributes

        Returns:
            Base instance: instance of Rectangle or Square
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = cls()
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances loaded from JSON file.

        Returns:
            list: list of instances
        """
        filename = "{}.json".format(cls.__name__)
        if not os.path.exists(filename):
            return []
        with open(filename, "r", encoding="utf-8") as f:
            json_str = f.read()
        list_dicts = cls.from_json_string(json_str)
        return [cls.create(**d) for d in list_dicts]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes list_objs to CSV file.

        Args:
            list_objs (list): list of instances
        """
        filename = "{}.csv".format(cls.__name__)
        with open(filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            if list_objs is not None:
                for obj in list_objs:
                    if cls.__name__ == "Rectangle":
                        writer.writerow([
                            obj.id, obj.width, obj.height, obj.x, obj.y
                        ])
                    elif cls.__name__ == "Square":
                        writer.writerow([
                            obj.id, obj.size, obj.x, obj.y
                        ])

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes instances from CSV file.

        Returns:
            list: list of instances
        """
        filename = "{}.csv".format(cls.__name__)
        if not os.path.exists(filename):
            return []
        instances = []
        with open(filename, "r", newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                if not row:
                    continue
                row = [int(val) for val in row]
                if cls.__name__ == "Rectangle":
                    d = {
                        "id": row[0],
                        "width": row[1],
                        "height": row[2],
                        "x": row[3],
                        "y": row[4]
                    }
                elif cls.__name__ == "Square":
                    d = {
                        "id": row[0],
                        "size": row[1],
                        "x": row[2],
                        "y": row[3]
                    }
                instances.append(cls.create(**d))
        return instances

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Opens a window and draws all Rectangles and Squares.

        Args:
            list_rectangles (list): list of Rectangle instances
            list_squares (list): list of Square instances
        """
        import turtle

        t = turtle.Turtle()
        t.speed(2)
        t.pensize(2)
        screen = turtle.Screen()
        screen.bgcolor("#1a1a2e")
        screen.title("Almost a Circle - Shapes")

        rect_colors = ["#e94560", "#0f3460", "#16213e"]
        sq_colors = ["#533483", "#e94560", "#0f3460"]

        t.penup()
        for i, rect in enumerate(list_rectangles):
            t.goto(rect.x, rect.y)
            t.pendown()
            t.color(rect_colors[i % len(rect_colors)])
            t.begin_fill()
            for _ in range(2):
                t.forward(rect.width)
                t.left(90)
                t.forward(rect.height)
                t.left(90)
            t.end_fill()
            t.penup()

        for i, sq in enumerate(list_squares):
            t.goto(sq.x, sq.y)
            t.pendown()
            t.color(sq_colors[i % len(sq_colors)])
            t.begin_fill()
            for _ in range(4):
                t.forward(sq.size)
                t.left(90)
            t.end_fill()
            t.penup()

        t.hideturtle()
        turtle.exitonclick()
