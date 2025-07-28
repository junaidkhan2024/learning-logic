#Find the sum of all elements in the array.

# def findsum(ls):
#     total = 0
#     for i in range(len(ls)):
#        total += ls[i]
#     print(total)    

# a = [1,2,3,45,3,5]
# findsum(a)


def lssum(ls):
    total = 0
    for i in ls:
        total += i # it is same as total = i + total
    print(total)

a = [1,2,3,45,3,5,1]
lssum(a)

#in built

def suminbuilt(ls):
    print(sum(ls))

a = [1,2,3,45,3,5,1,2]
suminbuilt(a)
