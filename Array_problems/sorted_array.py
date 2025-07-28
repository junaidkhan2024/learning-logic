# Chec k if an array is sorted.

def sortedls(ls):
    for i in range(len(ls) - 1): # if we have length 4 range(4 - 1) = range(3) = [0, 1, 2]\n
                                 # we r nt taking 3 index coz we are comoparing it with 2 if we include 3 thann itwill go out of range of the list indices
        if ls[i] > ls[i+1]: # comparing current index with next index for ascending order small to large
            print(f"{ls} is not sorted in")
            break
    else:
         print(f"{ls} is sorted in ascending order ")
    
a = [11,12,13,14]
sortedls(a)
print()

def descendingsortedlist(ls):
    for i in range((len(ls)-1)):
        if ls[i] < ls[i+1]:
            print(f"{ls} is  not a descending sorted list")
            break
    else:
        print(f"{ls} is a descending sorted list.")

a = [11,12,13,14,15]
descendingsortedlist(a)

b = [10,9,8,7,6,5,4]
descendingsortedlist(b)

#using all() it checks if all values in an iterable are True and returns True if they are, else returns False.
# syntax all(iterable) 
# iterable can be:
        # A list: [True, True, True]
        # A tuple: (True, False, True)
        # A generator: (x > 0 for x in numbers)
        # Any sequence you can loop over.

def issortedusingall(ls):
    print("if true this  is a ascending sorted list\n",all(ls[i] < ls[i +1] for i in range(len(ls) - 1)))

a = [1,2,3,4,5]
issortedusingall(a)

def decesoretdbyALL(lst):
    lst = list(lst) #convert string if comes into input  
    print(f"{lst} is a descending sorted list if true\n" , all(lst[i] > lst[i+1] for i in range(len(lst) - 1)))

a = [1,2,3,4,5]
decesoretdbyALL(reversed(a))

b  = [5,4,3,2,1]
decesoretdbyALL(b)

c = "123456"
decesoretdbyALL(reversed(c))
          
#FOR ME The range() function generates a sequence of numbers for looping.

# range(stop) → from 0 up to stop-1.
# range(start, stop) → from start up to stop-1.
# range(start, stop, step) → from start up to stop-1, incrementing by step.
