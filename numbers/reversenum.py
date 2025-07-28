#Reverse a number.

def reversed_num(num):
    rev = 0
    while num > 0:
        d  = num % 10 # it gives last digit of the num 
        rev = rev * 10 + d #shift and last digit at first in rev
        num = num // 10 # remove last digit from the num then loops continue until num becomes 0
    print(rev)

a = 123
reversed_num(a)
print("__________________")


#using for loop for negative and positive both
def reverse1(num):
    sign = -1 if num < 0 else 1
    str_num = str(abs(num))
    rev = ""
    for ch in str_num:
        rev = ch + rev
    print(f"using for loop",int(rev) * sign)

a = 14899816
reverse1(a)
b = -13254
reverse1(b)
print("__________________")

#2 slicing and converting method
def revN(num):
    temp = int(str(num)[::-1])
    print(temp)

a = 466852
revN(a)

#3 for negative number
def negrev(num):
    rev = int(str(abs(num))[::-1]) * (-1 if num < 0 else 1) #abs(num) converts num in positive num str converts in string 
                                                            # [::-1] reverse the string int converts back to int
                                                            # * -1 if num < 0 converts back to negative num else keep it same
    print(rev)

a = 65164589
negrev(a)
