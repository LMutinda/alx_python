def safe_print_division(a, b):
    try:
        result=a/b
        return result
    except:
        return None
    
    finally:
        print("Inside result: {}".format(safe_print_division(a,b)))





