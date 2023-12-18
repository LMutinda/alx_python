"""
This module contains a rectangle class
"""
base = __import__('models.base').base

Base = base.__dict__.get('Base')



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
        self.validate_integer("width", width)
        self.validate_positive("width", width)
        self.__width = width
        self.validate_integer("height", height)
        self.validate_positive("height", height)
        self.__height = height
        self.validate_integer("x", x)
        self.validate_non_negative("x", x)
        self.__x = x
        self.validate_integer("y", y)
        self.validate_non_negative("y", y)
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
        self.validate_integer("width", value)
        self.validate_positive("width", value)
        self.__width = value
        
        


    @property
    def height(self):
        """
        Getter for the height
        """
        return self.__height
    
    @height.setter
    def height(self,value):
        """
        Setter fo the height value
        """
        self.validate_integer("height", value)
        self.validate_positive("height", value)
        self.__height =value
            
       
    
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
        self.validate_integer("x", value)
        self.validate_non_negative("x", value)
        self.__x =value
            
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
        self.validate_integer("y", value)
        self.validate_non_negative("y", value)
        self.__y =value
            
    def validate_integer(self, attribute_name, value):
        """Validate if the value is an integer"""
        if not isinstance(value, int):
            raise TypeError(f"{attribute_name} must be an integer")

    def validate_positive(self, attribute_name, value):
        """Validate if the value is greater than 0"""
        if value <= 0:
            raise ValueError(f"{attribute_name} must be > 0")

    def validate_non_negative(self, attribute_name, value):
        """Validate if the value is greater than or equal to 0"""
        if value < 0:
            raise ValueError(f"{attribute_name} must be >= 0") 

    def area(self):
        return self.__width* self.__height  

