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
        #self.__width = width
        #self.__height = height
        #self.__x = x
        #self.__y = y
        if self.__width is not int:
            raise TypeError("width must be an integer")
        else:
            if self.__width<= 0:
                raise ValueError("width must be > 0")
            else:
                self.__width = width

        if self.__height is not int:
            raise TypeError("height must be an integer")
            
        else: 
            if self.__height<= 0:
                raise ValueError("height must be > 0")
            else:
                self.__height = height

        if self.__x is not int:
            raise TypeError("x must be an integer")
            
        else: 
            if self.__x < 0:
                raise ValueError("x must be >= 0")
            else:
                self.__x =x

        if self.__y is not int:
            raise TypeError("y must be an integer")
            
        else: 
            if self.__y < 0:
                raise ValueError("y must be >= 0")
            else:
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
        
        self.__y =value
            
       

