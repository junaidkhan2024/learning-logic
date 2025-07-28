#Check if a number is an Armstrong number.
# An Armstrong number (also called a narcissistic number, pluperfect number, or pluperfect digital invariant (PPDI)) is:
# A number that is equal to the sum of its digits each raised to the power of the number of digits.

def is_Armstrong(num):
    str_num = str(num)
    print(str_num)
    power = len(str_num)
    print(power)
    total = sum(int(ch)** power for ch in str_num) # num k har ek digit ko len of digits ki quwwat se zarab karte hai fir inhe jama karrte hai
    print(total)
    if total == num :
        print(f"given {num} is a armstrong number.")
    else:
        print("its not a armstrong number")

a = 153
is_Armstrong(a)   
print("______________")     

b = 143
is_Armstrong(b)
print("_______________________")


#for me
# ایک ایسا عدد (نمبر) جس کے تمام اعداد (digits) کو
# ان ہی کی تعداد کے برابر طاقت (power) پر اٹھا کر
# جب سب کو جمع کیا جائے تو اصل نمبر واپس مل جائے۔


#2 manual method for armstrong number

def is_armstrn(num):
    orignal = num
    power = 0
    temp = num
  #obtain power firts(how many digits in num)
    while temp > 0:
        temp //= 10             # or <temp = temp // 10> isse har bar ek digit kam hojayengi num me se  
        power += 1              # ek digit kam hua to ye count karenga 1 aise he sare digits count honge ek ek kar ke 
    print(power)                # so that hame kitni quwwat(power)(exponentiation) use karna hai pata chal sake

  # Sum for armstrong number
    total = 0
    temp = num
    while temp >0:
        digit = temp % 10 #will get last digit of the number 
        total = total + (digit ** power)
        temp = temp // 10 # each time temp will loose one last digit that is remainder ex 153 // 10 = 3(// floordivision gives remainder in int)
    print(total)

    #compare num with total to see armstrong or not

    if total == orignal:
        print(f"{orignal} is Armstrong number.")
    else:
        print(f"{orignal} is not a armstrong number")
print("in manuall method")
a = 153
is_armstrn(a)
print("_______")
b = 1234
is_armstrn(b)
print("_________")

