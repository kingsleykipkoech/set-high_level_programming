#!/usr/bin/python3
"""Module for text_indentation function."""


def text_indentation(text):
    """Prints text with 2 new lines after each '.', '?' or ':'.

    Args:
        text (str): the text to print
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    result = ""
    for char in text:
        result += char
        if char in ".?:":
            result += "\n\n"
    lines = result.split("\n")
    for i, line in enumerate(lines):
        print(line.strip(), end="")
        if i < len(lines) - 1:
            print()
