def best_score(a_dictionary):
    if a_dictionary is not None:
        values= a_dictionary.values()
        if not values:
            best_key = None
            return best_key
        else:
            max_value= max(values)
            max_key = {i for i in a_dictionary if a_dictionary[i]== max_value}
            for x in max_key:
                best_key = x
            
            return best_key
        
    else:
        best_key = None
        return best_key
    


    