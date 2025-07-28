#Find GCD and LCM of two numbers.
# in math lcm * gcd = a * b(actual number ko multiply karne par same answer aayenga jo lcm or gcd ko multiply karne par aat hai)

def gcmandlcm(num1,num2):
    import math
    gcd1 = math.gcd(num1,num2)
    print(f"GCD of {num1} and {num2} is =  {gcd1}")

    lcm = num1 * num2 // gcd1
    print(f"LCM of {num1} and {num2} is {lcm}.")

a = 18
b = 6
gcmandlcm(a,b)
print("__________________________")

# euclidean algorythm

def findgcdlcm(n1,n2):
    a = n1 # keeping orignal stored 
    b = n2
    while b != 0:   # euclidean algorythm
        a,b = b , a%b # euclidean algorythm
    gcd = a
    lcm = n1 * n2 // gcd
    print(f"in while loop gcd in {n1} nad {n2} is {gcd}")
    print(f"in while loop lcm in {n1} and {n2} is {lcm}")

a = 18
b = 6
findgcdlcm(a,b)
