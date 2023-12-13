"""
This is a module to determine if an object is the object is an instance of, or if the object is an instance of a class that inherited from, the specified class
"""

def is_kind_of_class(obj, a_class):
    """
    Method to determine whether an object is an instance of a class

    Args:
        obj: The object to be checked.
        a_class: The class to compare against.

    Returns:
    -True if obj is an instance of a_class, otherwise False.
    
    """
    x = isinstance (obj, a_class)
    if x == True:
        return True
    
    else: 
        return False
    #return type(obj) == a_class and (a_class != bool or obj is True)

    
    

