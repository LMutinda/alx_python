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

    
    @property
    def size(self):
        """Getter method to retrieve the size of the square."""
        return self.__size
    
    @size.setter
    def size(self, value):
        """Setter method to set the size of the square.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If the provided value is not an integer.
            ValueError: If the provided value is less than 0.
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size **2
    
    def my_print(self):
        """prints a rectangle using '#'"""
        
        if self.__size == 0:
            print()
        else:
            for height in range(self.__size):
                for width in range(self.__size):
                    print('#', end='')
                print()
        
    def __str__(self):
        """prints a rectangle using '#'"""
        return f"{self.my_print()}"
    


    
    



