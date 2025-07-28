#Count occurrences of a character in a string.

def countOccurences(strg,charTC):
    store =  {}
    for char in strg:
        if char != " ": # for skipping spaces in string
         # if we want to take only alphabets then we can use if c.isalpha():
         store[char] = store.get(char,0) + 1
    return store.get(charTC,0) # ut gives us the cahr we want to search in the string and its occurence in the string.
   # return "".join(filter(str.isalpha,store))    ----wrong experiment

a = "junaid khan dewalghat"
ch = "w"
print(countOccurences(a,ch))


#Using counter()

def occuranceCounter(strg,check):
   from collections import Counter
   count = Counter(alphabet for alphabet in strg.lower() if alphabet != " ") #counter dict banata hai alphabets ki strg k her
   print(count[check])                                                      #ek alphabet ko lekar count karta hai sivaye " " k  " " = space
   
incidence = "Ahmed bhai removed his beared on 24/7/2025"
c = "h"
occuranceCounter(incidence,c)



