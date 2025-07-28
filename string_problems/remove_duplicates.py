#Remove all duplicate characters from a string
from collections import OrderedDict
#convert in set then string

a = "whats up pune"
b = set(a) #convert the string to set which is {} unordered and unique doesnt allow duplicates.
c = "".join(b)
print(c) #problem string will be unordered.

# Using collections.OrderedDict.fromkeys() (Order Preserved):
#OrderedDict maintains the insertion order of keys. 
#By creating an OrderedDict from the string using fromkeys(), 
#duplicate characters are automatically handled while preserving the original order.


a = "My name is khan."
new = "".join(OrderedDict.fromkeys(a)) #creating a dict from string then creating a string out of that without repeated letters.
print(new)

#if we want to maintain space between words
def rdupwithSpace(str1):
 a = []
 b = set()
 for c in str1:
    if c not in b or c == " ": #  we are taking " " bcoz we want space between lettrs
        a.append(c) # append is a list method which add char at the end.
    if c != " ":
        b.add(c)  # add is a set method set is unordered hence it get added anywhere in the set.  
 new_string = "".join(a)
 print(new_string)

string1 = "what is going on today."
rdupwithSpace(string1)


