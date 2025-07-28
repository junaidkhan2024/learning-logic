# Count the number of digits in an integer.for positive numbers

def countdigitd(num):
    count = 0
    str_num = str(num)
    for d in str_num:
        count += 1
    print(f"{num} have {count} digits")

a = 10235468
countdigitd(a)
print("_________________")

#Short cut for pos and neg number

def countdigit(num):
    print(f"{num} has {len(str(abs(num)))} digits.")

a = -4523323
countdigit(a)
