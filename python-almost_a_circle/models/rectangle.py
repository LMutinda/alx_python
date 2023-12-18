"""
This module contains a rectangle class
"""
class Base:
    """This is the meta class"""
    __nb_objects = 0
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects



class Rectangle(Base):
    """This is the rectangle class taht inherits from the Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Method to determine whether an object is an instance of a class

        Args:
            width: Rectangle width.
            height: rectangle height
            x
            y
            id: from Base class

        

        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def get_width(self):
        """
        Getter for the __width variable  
        """
        return self.__width
    def set_width(self,value):
        """
        Setter for width value
        """
        self.__width = value

    def get_height(self):
        """
        Getter for the height
        """
        return self.__height
    def set_height(self,value):
        """
        Setter fo rthe height value
        """
        self.__height = value
        
    def get_x(self):
        """
        Getter for x
        """
        return self.__x
    def set_x(self,value):
        """
        Setter for x value
        """
        self.__x = value

    def get_y(self):
        """
        Getter for y
        """
        return self.__y
    def set_y(self,value):
        """
        Setter for y value
        """
        self.__y = value

