def multiple_returns(sentence):
    
    length = len(sentence)
    if len(sentence) >0:
        first = sentence[0]
    else:
        first = None

    print("Length: {:d} - First character: {}".format(length, first))
    return (length, first)

   

    
    
