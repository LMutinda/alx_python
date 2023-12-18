"""
This module contains a rectangle class
"""
rect = __import__('models.rectangle').rectangle

Rectangle = rect.__dict__.get('Rectangle')

class Square(Rectangle):
    """This is the square class that inherits from the Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """
        Method to determine whether an object is an instance of a class

        Args:
            width: Rectangle width.
            height: rectangle height
            x
            y
            id: from Base class

        """
        super().__init__(size, size, x, y, id)


    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
    
    @property
    def size (self):
        return self.width 
    @size.setter
    def size(self,value):
        self.width = value
        self.height = value

