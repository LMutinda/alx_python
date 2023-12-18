"""
This module contains a rectangle class
"""
from base import Base

class Rectangle(Base):
    """This is the rectangle class taht inherits from the Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def get_width(self):
        return self.__width
    def set_width(self,value):
        self.__width = value

    def get_height(self):
        return self.__height
    def set_height(self,value):
        self.__height = value
        
    def get_x(self):
        return self.__x
    def set_x(self,value):
        self.__x = value

    def get_y(self):
        return self.__y
    def set_y(self,value):
        self.__y = value

