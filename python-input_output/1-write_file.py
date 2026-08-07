#!/usr/bin/python3
"""Module for writing to a file"""


def write_file(filename="", text=""):
    """Writes a string to a text file and returns number of characters"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
