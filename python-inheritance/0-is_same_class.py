"""
This is a module to determine if an object is an instance of a class
"""

def is_same_class(obj, a_class):
    """
    Method to determine whether an object is an instance of a class

    Args:
        obj: The object to be checked.
        a_class: The class to compare against.

    Returns:
    -True if obj is an instance of a_class, otherwise False.
    
    """
    x= isinstance(obj, a_class)
    if x == True and (obj != True and obj != None and obj != False ) :
        return True
    else: 
        return False
    
    


