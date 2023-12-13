"""
This module checks if the object is an instance of a class that inherited (directly or indirectly) from the specified class
"""

def inherits_from(obj, a_class):
    """
    Method to determine whether an object is an instance of a class

    Args:
        obj: The object to be checked.
        a_class: The class to compare against.

    Returns:
    -True if obj is an instance of a_class, otherwise False.
    
    """

    return issubclass(type(obj), a_class) and type(obj) != a_class