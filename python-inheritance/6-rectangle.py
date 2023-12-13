"""
This module contains an empty class
"""

class meta_class:
    """This is the meta class"""
    
    def __dir__(cls):
        return [attribute for  attribute in super().__dir__() if attribute != "__init_subclass__"]

class BaseGeometry(meta_class):
    
    """This is a geometry class"""
    def area(self):
        raise Exception ("area() is not implemented")
    
    def integer_validator(self, name, value):
        self.name = name
        self.value = value

        if type(value) != int:
            raise TypeError ("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError ("{} must be greater than 0".format(name))
        

class Rectangle ( BaseGeometry ):
    """This is a rectangle class that inherits from the BaseGeometry class"""
    def __init__(self, width, height):
        self.__width = width 
        self.__height = height 
        
    def integer_validator(self, width, height):
        self.__width = width 
        self.__height = height 

        if type(width) != int:
            raise TypeError ("width must be an integer")
        if width <= 0:
            raise ValueError ("width must be greater than 0")
        if type(height) != int:
            raise TypeError ("width must be an integer")
        if height <= 0:
            raise ValueError ("width must be greater than 0")
        
       
    

