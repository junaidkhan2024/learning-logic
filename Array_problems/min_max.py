#USing iteration

def minmaxofArray(ary):
    minm = ary[0] # starting from first elemnet of list
    maxi = ary[0]
    for i in range(len(ary)):
        if ary[i] < minm: #if i element of list is smaller that first element 
            minm = ary[i] # than it becomes the minm and contiue to search till end of the list doing the same
        if ary[i] > maxi: # if i element is bigger than first element
            maxi = ary[i]  # than it becomes the maxi and cont to search till the end of list doing the same  
    print("minimum elemnet is ",minm)
    print("maximum element is " , maxi)

a = [12,1,2,455,54,8,13]
minmaxofArray(a)
print()

#other method

def minMaxofList(ls):
    if not ls:
        print("this is not a list")
        return
    minm = maxm = ls[0]
    for n in ls:
        if n < minm:
            minm = n
        elif n > maxm:
           maxm = n
    print("minmum number in the list is ", minm)
    print("maximum number in the list is ",maxm)
         
a = [12,5,51,54,215,94,21,584,12321,9,16,98984,61,9943,161,3,94,649,13,91,3,13,30,0,51,51,6516,414]
minMaxofList(a)


#Using sort()

def usingsort(ls):
    ls.sort()  # this method arrange list in ascending oredr by default 
    print("smallest number in the list is ", ls[0]) # hence first index becomes the smallest element in the list
    print("largest number in the list is ", ls[-1]) # and the last becomes the largest

a = [12,2,12,55,41564,88,16556489,0,65]
usingsort(a)
print()

#Using in built

def inbuiltminMax(ls):
    print("minimu nums = ",min(ls))
    print("maximum number = ",max(ls))

a = [45,12,55,4,54,5,54,84,54,21,858,54,85,42,154,5,1854,51,54,548,
     412,15,]
inbuiltminMax(a)


