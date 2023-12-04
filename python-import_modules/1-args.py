if __name__ == "__main__":
    import sys

    # Get the command-line arguments
    argv = sys.argv[1:]
    
    num= len(argv)
    count = 0
    if num == 1:
        print("{} argument:".format(num))
        for i in argv:
            count = count + 1
            print("{}: {}".format(count,i))
    elif num == 0:
        print("{} arguments.".format(num))
        for i in argv:
            count = count + 1
            print("{}: {}".format(count,i))
    else:
        print("{} arguments:".format(num))
        for i in argv:
            count = count + 1
            print("{}: {}".format(count,i))
    

