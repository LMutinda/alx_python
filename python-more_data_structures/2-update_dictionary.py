def update_dictionary(a_dictionary, key, value):
    new_dict= a_dictionary
    x = new_dict.get(key,0)
    if x == 0:
        new_dict[key]=value
    else:
        new_dict[key] = value

    return new_dict



    
   
