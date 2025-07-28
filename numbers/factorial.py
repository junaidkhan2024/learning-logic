#Find factorial of a number. # factorial number matla diye gaye number se 1 tak multiply karkne k bad unki jama kiya hua number

def fectorial1(num):
    fcat = 1
    for i in range(1,num+1):
        fcat = fcat * i  # or fcat *= i
    print(f"factorial of {num} = {fcat} ")
a = 5
fectorial1(a)     

#recursion method (calling self function in nfunction)

def fcatorial2(num):
    if num == 0 or num == 1:
        return 1
    return num * fcatorial2(num - 1) 
# Multiply the current number n with the factorial of the previous number (n-1).
# So it's breaking the big problem into smaller problems.
# # factorial(5)
# = 5 * factorial(4)
# = 5 * (4 * factorial(3))
# = 5 * (4 * (3 * factorial(2)))
# = 5 * (4 * (3 * (2 * factorial(1))))
# = 5 * (4 * (3 * (2 * 1)))      ← factorial(1) returns 1
# = 5 * 4 * 3 * 2 * 1
# = 120 
a = 4
print(fcatorial2(a))

def fact3(num):
    import math
    print(math.factorial(num))
a = 6
fact3(a)


#for me
# The factorial of a number n (written as n!) means:
# Multiply all whole numbers from n down to 1.
# 5 factorial = 5!
# 5! = 5 × 4 × 3 × 2 × 1 = 120
