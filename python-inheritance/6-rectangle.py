"""
This module contains an empty class
"""
BaseGeometry = __import__('5-base_geometry').BaseGeometry
        


class Rectangle (BaseGeometry):
    """This is a rectangle class that inherits from the BaseGeometry class"""
    def __init__(self, width, height):
        
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
       





       
    

