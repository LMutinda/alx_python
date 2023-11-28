for i in range(100):
    if i < 99:
        # Print a leading zero for single-digit numbers
        print(f"{i:02d}", end=", ")
    else:
        print(i)
        
   