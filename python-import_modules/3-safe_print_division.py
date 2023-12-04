def safe_print_division(a, b):
    try:
        result=a/b
        print("Inside result: {}".format(result))
        
    except:
        result = None
        print("Inside result: {}".format(result))
    
    finally:
        
        print("{:d} / {:d} = {}".format(a, b, result))





