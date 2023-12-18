"""
This module contains an empty class
"""
BaseGeometry = __import__('5-base_geometry').BaseGeometry
        


class Rectangle (BaseGeometry):
    """This is a rectangle class that inherits from the BaseGeometry class"""
    def __dir__(cls):
        return [attribute for  attribute in super().__dir__() if attribute != "__init_subclass__"]
    def __init__(self, width, height):
        #self.integer_validator("width", width)
        #self.integer_validator("height", height)
        super().integer_validator("width",width)
        super().integer_validator("height",height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width*self.__height
    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
    







       
    

