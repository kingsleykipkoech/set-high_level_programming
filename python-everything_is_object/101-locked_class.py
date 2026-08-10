#!/usr/bin/python3
"""Module for LockedClass."""


class LockedClass:
    """Prevents dynamic creation of attributes except first_name."""

    __slots__ = ["first_name"]
