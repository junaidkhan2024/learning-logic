# find the first non repeating char in string.

#USING dictionary method
def firtsNr(st):
 dict1 = {}
 for c in st:
  dict1[c] = dict1.get(c,0) + 1
 print(dict1)
 for c in st:
  if dict1[c] == 1:
   print(c)  
   return c 

a = "abhay sharma"
firtsNr(a)

#MOdified for removing special char

def fNRchar(st):
  modified_str = "".join(filter(str.isalpha,st)).lower()
  print("in modified",modified_str)
  d = {}
  for c in modified_str:
   d[c] = d.get(c,0) + 1
  for c in modified_str: 
   if d[c] == 1:
    print(f"first non repeating charector in this string is {c}")
    return c
  else:
    print(f"No Non repeating char here.")

a = "using .join.filter() fOr search 1st non repeating chaR."
fNRchar(a)
b = "aabbcccbddd"
fNRchar(b)
 

 #USING collection counter 

def fNRC(s):
  from collections import Counter
  count_s = Counter(s)
  for c in s:
    if count_s[c] == 1:
     return c
  return None

b = "loiness"
print(fNRC(b))

a = "@sahebzade"
print(fNRC(a)) 
