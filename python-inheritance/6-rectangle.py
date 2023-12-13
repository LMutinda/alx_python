"""
This is a module on inheritance
"""
from Base import BaseGeometry

class Rectangle (BaseGeometry):
    """This is a rectangle class that inherits from the BaseGeometry class"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height



       
    

