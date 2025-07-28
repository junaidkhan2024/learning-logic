#Check if a number is even or odd.

def even_odd(n):
    if n % 2 == 0:
        print(f"{n} is even number")
    else:
        print(f"{n} is odd number")

a = 13
b = 22654
even_odd(a)
print("____________________________")
even_odd(b)
print("____________________________")

#pythonic way ternary (conditional) expression:

def oddeven(n):
    print(f"{n} is {'even' if n%2 == 0 else 'odd'} number")

a = 32328+94
oddeven(a)
