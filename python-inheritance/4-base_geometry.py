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
       
