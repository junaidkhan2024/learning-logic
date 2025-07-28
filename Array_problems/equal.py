# #Check if two arrays are equal.

# #1 manual or loop method

# def is_equal(ls1,ls2):
#   if len(ls1) != len(ls2):
#      print(f"{ls1} and {ls2} are not equal.")
#      return
#   for el in range(len(ls1)):
#         if ls1[el] != ls2[el]: #comparing each element of ls1 with ls2 
#          print(f"{ls1} and {ls2} are not equal for sure.")
#          return
#   else:
#        print(f"finally {ls1} and {ls2} are equal")


# a = [1,2,3,4,5,6,7,8,9,10,12]
# b = [1,2,3,4,5,6,7,8,9,10,12]
# is_equal(a,b)
# print('____________________________________')

# #2 other method

# def is_equal(l1,l2):
#    if l1 == l2: #direct comparision of lists
#       print(f"{l1} and {l2} are equal .")
#    else:
#       print("error")     
   
# a = [1,2,3,4,5,6,7,8,9,10,12,7]
# b = [1,2,3,4,5,6,7,8,9,10,12]
# is_equal(a,b)
# print("-------------------------------------------")
# #3 using sorted() method

# def is_equalwith_sorted(l1,l2):
#    if sorted(l1) == sorted(l2): # to check if they have the same element arranged differently.
#       print(f"{l1} and {l2} are equal.")
#    else:
#       print("ERROR-2")

# a = [3,2,1,5,6,4]
# b = [1,2,3,4,5,6]
# is_equalwith_sorted(a,b)
# print('..........................................')

# c = ["a","b","c"]
# d = ["c","a","b"]
# is_equalwith_sorted(c,d)
# print(".....................................")


#4 using dict (it will auto-matically solve sorting issue)

def is_equalwithDict(l1,l2):
   d1 = {}
   d2 = {}
   for el in l1:
      d1[el] = d1.get(el,0)+1
   print(d1)
   for el in l2:
      d2[el] = d2.get(el,0)+1
   print(d2)
   if d1 == d2:
      print(f"{l1} and {l2} are equal")
   else:
      print("ERORRRRRRRRRRRRRRRRR")

c = ["a",True,"b","c",1]
d = ["c","a",True,"b",1]
is_equalwithDict(c,d)  
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")


#5 using dict with collection counter

def is_equalwithcollectionCounter(l1,l2):
   from collections import Counter

   counter_l1 = Counter(l1)
   print(counter_l1)
   counter_l2 = Counter(l2)
   print(counter_l2)
   if counter_l1 == counter_l2:
      print(f"{l1} and {l2} are equal")
   else:
      print("EAROR$$$$$$$$$$$$$$$")

c = ["a",True,"b","c",2,True]
d = ["c","a",True,"b",2,1]  #true == 1 hence its printed equal
is_equalwithcollectionCounter(c,d)
