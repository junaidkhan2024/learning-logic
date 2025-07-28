#Find the second largest and second smallest element.

#1 manual method

def secondL_S(ls):
    sorted_ls = sorted(ls)
    print(f"second largest element in the{ls} is ",sorted_ls[-2],f"and second smallest element is ", sorted_ls[1])

a = [15,321,65411,3215,1,51,23,2,65]
secondL_S(a)
print("--------------------------------------")


#2 other method

def secondLandS(ls):
  new_list =list(set(ls)) # first removes duplicate by making a set which doesnt allow duplicates then makes a list. we cant use sort() directly here
  print(ls)
  print(new_list)
  new_list.sort()
  print(new_list)
  print(f"Second largest = ",new_list[-2])
  print(f"Second Smallest = ", new_list[1])

a = [654,654,21,85,1,84,55,21,6,54,52,551,2,2588,1,6]
secondLandS(a)
