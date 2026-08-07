#!/usr/bin/python3
"""Module for appending text after lines containing a search string"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line after each line containing a specific string"""
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()

    result = []
    for line in lines:
        result.append(line)
        if search_string in line:
            result.append(new_string)

    with open(filename, "w", encoding="utf-8") as f:
        f.writelines(result)
