#Replace all spaces in a string with %20 (like URL encoding).

def replaceS(st):
 temp = []
 for ch in st:
  if ch == " ":
   temp.append("%20")
  else:
   temp.append(ch)
 return "".join(temp)

astringhere = "anything to write with spaces."
print(replaceS(astringhere))

print() # for adding empty line

#in built replace methods
# def replaceS(st):
#     return st.replace(" ", "%20")

# a = "using in built function."
# print(replaceS(a))
# print()


def using_inbuilt(st):
  print(st.replace(" ","%20"))

a = "This is for testing replacing if space"
using_inbuilt(a)
print()








#USing list comprehension method [List comprehension is a short, clean way to create a list by using a single line of code instead of writing a full for loop.]

# def replaceS(st):
#     return ''.join(['%20' if ch == ' ' else ch for ch in st])   #structure [expression for item in iterable if condition]
#                                                                 # expression → What you want to store in the list.
#                                                                 # item in iterable → Loop over items (like for item in list).
#                                                                 # if condition (optional) → To filter which items to include.




def urlify(st):
  print("".join(['%20' if ch == " " else ch for ch in st]))

a = "whatever you wanna write with spaces."
urlify(a)
print()


import re
def replaceS(st):
    return re.sub(r' ', '%20', st)

a = "another line with spaces   "
print(replaceS(a))



#for study
# 1️⃣ import re
# re is Python’s regular expressions module.

# It allows searching, matching, and replacing patterns in strings.

# 2️⃣ def replaceS(st):
# Defines a function named replaceS that takes one input st (the string).

# 3️⃣ return re.sub(r' ', '%20', st)
# What is re.sub?
# re.sub(pattern, replacement, string)

# It searches for the pattern in the string and replaces it with replacement.
