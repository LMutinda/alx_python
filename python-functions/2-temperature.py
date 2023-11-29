def convert_to_celsius(fahrenheit):
    temp=(fahrenheit-32)*(5/9)
    degree=str(temp)
    m= degree.split(".")
    n=m[1]
    if len(n)>2:
        a= int(n[2])
        if a==0:
            celsius = round(temp,2)
        else:
            celsius=degree
        
        return celsius
    else:
        return temp


def switch(a):
    if a == 100 :
        print(convert_to_celsius(100))
    elif a ==-40:
        print(convert_to_celsius(-40))
    elif a == -459.67:
        print(convert_to_celsius(-459.67))
    elif a ==32:
        print(convert_to_celsius(32))
   
print(convert_to_celsius(-40))




