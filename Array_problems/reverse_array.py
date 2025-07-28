#Reverse an array.

def reversls(ls):
    new = "".join(reversed(ls)) # or "".join(ls[::-1])
    print(new)
    n = []
    for elm in new:
        n.append(elm)
    print(n)

a = ["1","2","3" "4"]
reversls(a)
b = ["a","b","c", "d","e"]
reversls(b)
print()

#other method
def revls(ls):
    start = 0 #assigning pointer at the first index
    end = len(ls) - 1
    while start < end: # jab tak start wala end wale se chota hai
        ls[start],ls[end] = ls[end],ls[start] # start wale ko end wale se swap karna hai.
        start += 1 #start se ek aage badhna hai
        end -= 1 # end se ek peeche aana hai
    print(ls)

a = ["a","b","c", "d","e"]
revls(a)
print()

#IN BUILT METHODS

def revLS(ls):
    ls.reverse()  # this METHOD reverses the same list
    print(ls)

a = ["a", "b", "c", "d"]
revLS(a)

def revls(ls):
    new = ls[::-1]

