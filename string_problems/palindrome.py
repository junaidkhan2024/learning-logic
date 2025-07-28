# TO Check if  a string is palindrome

def checkPalindrome(str): # method 1
    str = str.lower() # to avoid wrong result due to cap letters
    if str == str[::-1]:
        print(f"{str} is palindrome.")
    else:
        print(f"{str} is not a palindrome")    

a = "lol"
checkPalindrome(a)

b = "ninja"
checkPalindrome(b)

c = "Maam"
checkPalindrome(c)

def checkP(str): # method 2
    reversestr = ""
    index = len(str) - 1
    while index >= 0:
        reversestr += str[index].lower() # reversestr = reversestr + str[index].lower() for ABC it will be "-"+"a" then "a"+"b" then "ba" + "c" final "cab"
        index -= 1
    if str.lower() == reversestr:
        print(f"{str} is a palindrome {reversestr}.")
    else:
        print(f"{str} is not a palindrome {reversestr}")

name = "SHah jahan Akbar"
checkP(name)   

name = "Puup"
checkP(name)


#USING while loop starting from first(0) index

def whileP(s): # method 3
    newStr = ""
    index = 0
    while index < len(s):
        newStr = s[index].lower() + newStr # for anything it will "a" + "-", then "n" + "a", then "y" + "na" and so on.
        
        index += 1
    if s.lower() == newStr:
        print(f"{s} is palindrome. in 0 index of while  {newStr}.")
    else:
        print(f"{s} is not a palindrome in 0 index of while {newStr}.")

anything = "Anything"
whileP(anything)

p = "ahAha"
whileP(p)

def pWithFor(str): # method 4
    newstr = ""
    for i in str.lower():
        newstr = i + newstr
    if str.lower() == newstr:
        print(f"{str} is a palindrome {newstr}.")
    else:
        print(f"{str} is not a palindrome {newstr}.")

x = "Saas"
pWithFor(x)

y = "nothing is here"
pWithFor(y)

z = "MAMMAM"
pWithFor(z)


def joinandReverseP(str): # method 5
    newS = "".join(reversed(str.lower()))
    if str.lower() == newS:
        print(f"{str} is a palindrome.{newS}")
    else:
        print(f"{str} is not a palindrome.{newS}")    

a = "nooN"
joinandReverseP(a)

b= "Moon"
joinandReverseP(b)



# "".join(reversed(str.lower()))

# for i in str.lower():
#         newstr = i + newstr

# while index >= 0:
#         reversestr += str[index].lower()
#         index -= 1

# if str == str[::-1]:
