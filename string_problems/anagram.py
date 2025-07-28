#Check whether two strings are anagrams
#ANAGRAM = a word, phrase, or name formed by rearranging the letters of another, such as cinema, formed from iceman.

def isAnagrams(s1,s2): # method 1
 dict1 = {} #using dict to compare element without bothering about there index
 dict2 = {}
 for c in s1:
    dict1[c] = dict1.get(c,0)+1 #this will add char in dict1 from s1 string basically populating dict1 +1 adds repeating letters
 print(dict1)
 for c in s2:
    dict2[c] = dict2.get(c,0)+1 #populating dict2
 print(dict2)

 if dict1 == dict2:
    print(f"{s1} and {s2} are anagrams")
 else:
    print(f"{s1} and {s2} are not same.")

a ="aahaa"
b = " ahaaa"
isAnagrams(a,b)

first = "listen"
second = "silen t"
isAnagrams(first,second) #will give not angaram due to space in silen t

#checking the .get(ch,0) method
# ch = "q"
# a = {'q':2, 'd':3, 'c':1}
# print(a.get(ch,0))

#filter and join only alphabets
# word1 = "any thing 266 bu1 with spe&i@l (H@re($0R"
# clear_word = "".join(filter(str.isalpha,word1)).lower()
# print(word1)
# print(clear_word)



def anagramsWithdictionaryMethod(s1,s2): # method 2
   s1 = "".join(filter(str.isalpha,s1)).lower()
   print(s1)
   s2 = "".join(filter(str.isalpha,s2)).lower()
   print(s2)
   #this is first filtering the string for only alphabets removing special charector and spaces
   #then joining the list into a single string and then converting it into lowercase.
   if len(s1) != len(s2):
      print(f"{s1} and {s2} are not anagarms.")
   #if there length is not equal then they cant be anagarms.
   else:
    dict1 = {}
    dict2 = {}
    for c in s1:
      dict1[c] = dict1.get(c,0) + 1
    for c in s2:
      dict2[c] = dict2.get(c,0) + 1
    if dict1 == dict2:
      print(f"{s1} and {s2} are anagrams for sure.")
    else:
      print(f"{s1} and {s2} are not anagrams for sure") 

bio = "my name is junaid khan"
adr = "aa aaaa aa aaaaaa aaaa"
anagramsWithdictionaryMethod(bio,adr)

try1 = "thats juat fo@r ch,_eck"
try2 = "ckehc1 staht juat!! rof."
anagramsWithdictionaryMethod(try1,try2)

# #learnig sort() method

# word = "xylophone"
# print(sorted(word))
# print("".join(sorted(word))) #it give alphabetically sorted string

#checking anagram with sort()method

def anagramSorted(w1,w2): # method 3
  lower1 = w1.lower() #The sort() method cannot be used directly on strings in Python.hence cant write sorted(w1).lower()
  print(lower1)
  lower2 = w2.lower() # .lower() is a string method it cannot be applied directly on list[]

  Sorted_w1 = sorted(lower1)  #it gives alphabetically sorted list[]
  Sorted_w1 = "".join(filter(str.isalpha,Sorted_w1)) # .join and filter can be used on list[] to avoid number and special charectors in the word
  print(Sorted_w1)

  Sorted_w2 = sorted(lower2) 
  Sorted_w2 = "".join(filter(str.isalpha,Sorted_w2))
  print(Sorted_w2)
  if Sorted_w1 == Sorted_w2:
    print(f"'{w1}' and '{w2}' are anagarms")
  else:
    print(f"'{w1}'and '{w2}' are NOT ANAGRAMS.")

name = "ash an"
new = "nasha"
anagramSorted(name,new)


s = "ljhghsfjh"
c = "booopoooo"
anagramSorted(s,c)


#using clooection counter for anagram

def anagramCounter(str1,str2): #Method 4
  from collections import Counter
  s1 = str1.lower() # can do "".join(filter(str.isalpha,str1).lower()) to filter first
  s2 = str2.lower()

  counter_s1 = Counter(s1) # it gives a dictionary{} of word with respective count cant use .join(filter()) on dict directly
  print(counter_s1)
  counter_s2 = Counter(s2)
  print(counter_s2)

  return counter_s1 == counter_s2 # it will fail in special char or space or num in string

a = "anagram"
b = "nagaram"
print("in counter method",anagramCounter(a,b))



 

