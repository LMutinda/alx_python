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

    @property
    def width(self):
        """
        Getter for the __width variable  
        """
        return self.__width
    @width.setter
    def width(self,value):
        """
        Setter for width value
        """
        self.__width = value
        if self.__width is int:
            if self.__width<=0:
                raise ValueError("width must be > 0")
            else:
                self.__width = value
            
        else:
            raise TypeError("width must be an integer")


    @property
    def height(self):
        """
        Getter for the height
        """
        return self.__height
    
    @height.setter
    def height(self,value):
        """
        Setter fo rthe height value
        """
        if self.__height is int:
            if self.__height<=0:
                raise ValueError("height must be > 0")
            else:
                self.__height = value
            
        else:
            raise TypeError("height must be an integer")
    
    @property
    def x(self):
        """
        Getter for x
        """
        return self.__x
    
    @x.setter
    def x(self,value):
        """
        Setter for x value
        """
        if self.__x is int:
            if self.__x < 0:
                raise ValueError("x must be >= 0")
            else:
                self.__x = value
            
        else:
            raise TypeError("x must be an integer")
    

    @property
    def y(self):
        """
        Getter for y
        """
        return self.__y
    
    @y.setter
    def y(self,value):
        """
        Setter for y value
        """
        if self.__y is int:
            if self.__y < 0:
                raise ValueError("y must be >= 0")
            else:
                self.__y = value
            
        else:
            raise TypeError("y must be an integer")
        
if __name__ == "__main__":

    try:
        Rectangle(10, "2")
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        r = Rectangle(10, 2)
        r.width = -10
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        r = Rectangle(10, 2)
        r.x = {}
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        Rectangle(10, 2, 3, -1)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
