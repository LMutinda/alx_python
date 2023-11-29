def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def switch(val):
    if val == 17 :
        print(is_prime(17))
    elif val == 15 :
        print(is_prime(15))
    elif val == -5 :
        print(is_prime(-5))
    elif val == 0 :
        print(is_prime(0))

    