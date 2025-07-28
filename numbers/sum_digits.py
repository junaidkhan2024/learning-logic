#Sum of digits of a number.

def sumofdigitsa(num):
    str_num = str(abs(num))
    sum = 0
    for d in str_num:
        sum += int(d)
    print(f"sum of digits of {num} = ",sum)

a = 61565548
sumofdigitsa(a)
print("__________________")
#pythonic version

def countsumofdigits(num):
    total = sum(int(d) for d in str(abs(num)))
    print(f"{total} is the sum of digits of {num}")

a = -13248578
countsumofdigits(a)
