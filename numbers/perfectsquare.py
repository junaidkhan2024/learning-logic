#Check if a number is a perfect square.

def perfectsquare(num):
    for i in range(1,num+1):
        if i * i == num:
            print(f"{num} is a perfect square.")
            return
        elif i * i > num:
            break
    print(f"{num} is not a perfect square for sure.")
# earlier version 
# def perfectsquare(num):
#     for i in range(1,num+1):
#         if i * i == num:
#             print(f"{num} is a perfect square.")
#             return
#     else:
#         print(f"{num} is not a perfect square.")

a = 49
perfectsquare(a)
print()
b = 88
perfectsquare(b)
