#!/usr/bin/python3
"""
Method module
"""


def inherits_from(obj, a_class):
    """
    Check if object is an instance of a class.
    
    Args:
        obj: Object to check.
        a_class: Class to check.
    
    Returns:
        True or False.
    """

    if type(obj) == a_class:
        return False
    return issubclass(type(obj), a_class)
