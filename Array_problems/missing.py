#Find the missing number in a range (1 to n).


#if only 1 element is missing
def findmissing(ls): 
 new = sorted(ls)
 print(new)
 n = new[-1] # n is the largest numbver in the list
 expected_sum = n * (n + 1) // 2 #this formula gives the missing number in return after substracting with actual sum
 print(expected_sum)
 actual_sum = sum(new)
 print(actual_sum)
 missing_num = expected_sum - actual_sum
 print(f"missing num in {ls} is = ",missing_num)
# here is a problem what if we dont know the largest num. # we can use max(ls) method (earlier used a different approach its for that)
a = [1,2,3,5,7,6]                           # whic is def missingnum(ls,largestnum)
findmissing(a)                              # missing_num = largestnum * (n+1) // 2
print()                                     #  print(missing_num)
                                             #a = [1,2,3,5,7,6]
                                             # lnum = 7
                                             # missingnum(a,7) 



#2 for multiple missing numbers using set
def multiplemissing(ls):
 new = sorted(ls)
 start = new[0]
 end = new[-1]
 total_ele = [] # one more method total = list(range(start,end +1))
 for i in range(start,end +1 ): # dont have to bother about starting number of list.
  total_ele.append(i)
 missing_ele = sorted(list(set(total_ele) - set(new))) #cannt substract lists directly
 print(f"missing ele in {ls} is =",missing_ele)

a = [1,2,3,5,10,6]
multiplemissing(a)
print("--------------------------------")

b = [4,54,121,65,5,12,6]
multiplemissing(b)
print("***************************************")

#3 using manual without set

def manual_findM(ls):
 new = sorted(ls)
 start = new[0]
 end   = new[-1]
 total_el = []
 for i in range(start,end + 1):
  total_el.append(i)
 missing_el = []
 for el in total_el:
  if el not in new:
   missing_el.append(el)
 print(f"Missing elements in {ls} are ", missing_el)

a = [1,2,3,5,10,6]
manual_findM(a)  

