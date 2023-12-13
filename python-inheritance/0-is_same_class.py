"""
This is a module to determine if an object is an instance of a class
"""

def is_same_class(obj, a_class):
    """
    Method to determine whether an object is an instance of a class

    Args:
        obj: instance
        a_class: class name
    """
    if isinstance(obj,a_class) ==True:
        return True
    else:
        return False
    
    

