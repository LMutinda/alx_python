for i in range(100):
    if i < 99:
        # Print a leading zero for single-digit numbers
        print("{:02d}".format(i), end=", ")
    else:
        print("{}".format(i))
        
   