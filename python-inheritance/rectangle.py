"""
This module contains an empty class
"""

class meta_class:
    """This is the meta class"""
    
    def __dir__(cls):
        return [attribute for  attribute in super().__dir__() if attribute != "__init_subclass__"]

class BaseGeometry(meta_class):
    
    """This is a geometry class"""
    def area(self):
        raise Exception ("area() is not implemented")
    
    def integer_validator(self, name, value):
        self.name = "name"
        

        #if type(value) != int:
            #raise TypeError ("{} must be an integer".format(name))
        #if value <= 0:
            #raise ValueError ("{} must be greater than 0".format(name))
        if type(value) is int:
            if value <= 0:
                raise ValueError("{} must be greater than 0".format(name))
            else:
                self.value = value
        else:
            raise TypeError("{} must be an integer".format(name))
