#!/usr/bin/python3
"""Module for converting JSON string to object"""
import json


def from_json_string(my_str):
    """Returns the Python object represented by a JSON string"""
    return json.loads(my_str)
