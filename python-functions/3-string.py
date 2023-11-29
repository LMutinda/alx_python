def reverse_string(string):
    txt = string[::-1]
    return txt
def switch(word):
    if word == "Hello":
        print(reverse_string("Hello"))
    elif word == "":
        print(reverse_string(""))
    elif word == "madam":
        print(reverse_string("madam"))
    elif word == "Hello, World!":
        print(reverse_string("Hello, World!"))

