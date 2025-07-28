# Convert a string to title case.

def convertInTitleCase(str1):
 splitted_words = str1.split()
 print(splitted_words)
 title_case_words = []
 for w in splitted_words:
  if w:
    temp = w[0].upper() + w[1:].lower()
    title_case_words.append(temp)
 print(title_case_words)
 print(" ".join(title_case_words))

naything = "How's the weather in pune on 24/7/25."
convertInTitleCase(naything)


#USnig inbuilt str.title()
def inbuiltTC(st):
 b = st.title()
 print(b)

a = "amazing india"
inbuiltTC(a)
b = "pune is good's city"
inbuiltTC(b)


#Using capwords

def using_capwrds(s1):
 from string import capwords
 print(capwords(s1))

a = "pune is good's city"
using_capwrds(a)
