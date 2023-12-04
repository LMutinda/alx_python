def no_c(my_string):
    dict={ord("c"): None, ord("C"): None }
   
    new_string = my_string.translate(dict)
    return new_string

