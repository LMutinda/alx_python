def fibonacci_sequence(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence
    

def switch(a):
    if a == 6 :
        print(fibonacci_sequence(6))
    elif a ==- 1:
        print(fibonacci_sequence(1))
    elif a == 0:
        print(fibonacci_sequence(0))
    elif a == 20:
        print(fibonacci_sequence(20))
   
