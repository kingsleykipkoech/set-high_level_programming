#!/usr/bin/python3
"""Module for class_to_json function"""


def class_to_json(obj):
    """Returns the dict description of an object for JSON serialization"""
    return obj.__dict__
