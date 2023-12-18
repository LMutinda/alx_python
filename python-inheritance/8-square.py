"""
This module contains an empty class
"""
Rectangle = __import__('7-rectangle').Rectangle
    
class Square (Rectangle):
    """This is a square class that inherits from the Rectangle class"""
    def __dir__(cls):
        return [attribute for  attribute in super().__dir__() if attribute != "__init_subclass__"]
    
    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", size) 
        super().__init__(size,size)

    def area(self):
        return self.__size * self.__size
    
    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__size,self.__size)







       
    

