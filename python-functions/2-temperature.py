def convert_to_celsius(fahrenheit):
    celsius=(fahrenheit-32)*0.56
    return celsius

def switch(a):
    if a == 100 :
        print(convert_to_celsius(100))
    elif a ==-40:
        print(convert_to_celsius(-40))
    elif a == -459.67:
        print(convert_to_celsius(-459.67))
    elif a ==32:
        print(convert_to_celsius(32))
   





