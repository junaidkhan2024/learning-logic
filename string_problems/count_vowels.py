# # to check for vowels and consonents in a string.

def check_vowel_or_not(str): # method 1
 count = 0 # counts vowels
 consonents = 0
 vowels = "aeiou"
 string_vowels = "" #gives vowels in str
 string_consonents = ""
 for char in str.lower():
  if char in vowels:
    string_vowels +=  char
    count += 1
 else:
  for char in str.lower():
   if char not in vowels:
    string_consonents += char
    consonents += 1
 print(f"consonents are {string_consonents}  in given string  total = {consonents}")
 print(f"vowels are {string_vowels} total vowels = {count}")

random = "abcdefghijAklmnoEp"
check_vowel_or_not(random)
print("total charectors in words are ", len(random))

#USING sum()
def vowelsCountWithSum(sytr): # method 2
 vowels = "aeiou"
 vowelcount = sum(1 for char in sytr.lower() if char in vowels)
 consonentscount = sum(1 for char in sytr.lower() if char not in vowels)
 print(f"total vowels in {sytr} is {vowelcount}")
 print(f"consonents in {sytr} is total {consonentscount}")

name = "batista jOE aroot"
vowelsCountWithSum(name)




# def vowels_counter(str):
#  count = 0
#  vowels = ["a", "e" , "i", "o", "u"]

#  for char in str:
#   if char in vowels:
#    count += 1
#  print(f"vowels in {str} is ", count)

# x = "abckjlgdfyuiygsdifbvjlsnbl"
# vowels_counter(x)


# #USING str.lower()
# def countVowels(str):
#  vowels = "aeiou"
#  count = 0
#  for char in str.lower():
#   if char in vowels:
#    count += 1
#  print(f"total vowels in {str} is {count}")

# name = "Khabib Nurmagomevo"
# countVowels(name)
