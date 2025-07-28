#Check if one string is a rotation of another.

def isRotation(s1,s2):
 if len(s1) != len(s2):
  print(f"{s2} and {s1} cannot be rotation.")
  return
 for i in range(len(s1)):
  rotated_string = s1[i:] + s1[:i]
  if rotated_string == s2:
   print(f"{s2} is rotation of {s1}")
   return
 print(f"{s2} is not  a rotation of {s1}")

a = "junaid"
b = "naidju"
isRotation(a,b)

s = "khan"
d = "khak"
isRotation(s,d)

art = "painting"
poc = "crafting is fun"
isRotation(art,poc)


# Using concatenation method
def rotation_with_concat(s1,s2):
 if len(s1) != len(s2):
  print("these strings cant be rotation")
 return s2.lower() in (s1.lower() + s1.lower())

st = "India"
ts = "Diain"
print(rotation_with_concat(st,ts))


a = "Login"
b = "nigha"
print(rotation_with_concat(a,b))



# def moveleft(st,k): # k is for how many positions we need to move
#  k = k % len(st) #Because if k is larger than the string length, it would unnecessarily repeat.
#  print(k)
#  print(st[k:] + st[:k]) #string k "k" position se end tak k letters excluding k + string k start se "k" postion tak k letters (only letters on position of k)  
#  #--isse string rotate ho jayengi left me.

# strin = "junaid"
# moveleft(strin,50) # k ki position par kitne bhi likho wo string ki lenght k ander convert ho jayengi due to k = k % len(st)


# def moveright(st,k):
#  k = k % len(st)
#  print(st[-k:]+st[:-k])

# a = "arhamm"
# moveright(a,1)



# #comments for my self
# # if a%b and a is smaller than b then the modulus of this will be a like 2%4 = 2(4 goes 0 times in 2 and 2 is remainder)
# #a/b a is numerator and b is denominator
