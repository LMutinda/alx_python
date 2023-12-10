"""
This module consists of a class Square
"""
class Square:
    """
    This is the class Square. If the class has public attributes, they may be documented here
    in an ``Attributes`` section.
    """
    def __init__(self, size=0):
        """
        The __init__ method may be documented in either the class level
        docstring, or as a docstring on the __init__ method itself.
        Args:
            size (int): Defines the size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

