#Remove duplicates from a sorted array.

def removedup(ls):
 ls.sort()
 temp = []
 for i in ls:
  if i not in temp:
   temp.append(i)
 print("manual",temp)

a = [1,2,1,3,6,7,8,9,7,11,0]
removedup(a)


# Another using set.

def using_set_toremove(ls):
 new = sorted(list(set(ls))) # it doesnt have the orignal order
 print("using set",new)

a = [1,2,1,3,6,8,9,7,]
using_set_toremove(a) 

def removeusing_dict(ls): #it will have the orignal order
 print("using dict",list(dict.fromkeys(ls)))

a = [1,2,1,3,6,8,9,7,]
removeusing_dict(a)
