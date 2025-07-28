#Check if a number is a palindrome.
def ispalindrome(num):
    rev = int(str(num)[::-1])
    if num == rev:
        print(f"{num} is palindrome.")
    else:
        print(f"{num} is not a palindrome.")
    
a = 123321
ispalindrome(a)
print("_______________")
b = 987654
ispalindrome(b)

#for negative number

def ispalindrome(num):
    absN = abs(num)
    rev = int(str(absN)[::-1]) * (-1 if num < 0 else 1)
    if rev == num:
          print(f"{num} is palindrome.")
    else:
        print(f"{num} is not a palindrome.")

a = -123321
ispalindrome(a)
print("_______________")
b = -987654
ispalindrome(b)
print("_____________________")

#using for loop 
def is_palindrome(num):
    str_absN = str(abs(num))
    rev = ""
    sign = -1 if num < 0 else 1
    for ch in str_absN:
        rev = ch + rev
    isplaind = sign * int(rev)
    if isplaind == num:
        print(f"in for loop {num} is palindrome")
    else:
        print(f"in for loop {num} is not a palindrome")

a = 1234321
is_palindrome(a) 
b = -121
is_palindrome(b)
c = 1321654
is_palindrome(c)      
