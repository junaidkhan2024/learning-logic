#1 Count occurrences of an element in an array.

def occurance(ls,elTC):
    dict = {}

    for el in ls:
        dict[el] = dict.get(el,0) + 1
    print(dict)    
    print(dict[elTC])

a = [1,2,3,5,46,9,61,61,16]
occurance(a,61)
print("*********************")

#2 Without dict using counter
def forloop(ls,eltS):
    count = 0
    for el in ls:
        if el == eltS:
            count += 1
    print(count)

a = [321,45,612,54,21,321,12,12,21,21,55,54,612,45]
forloop(a,21)
print("********************************")

#3 using collections counter
def using_counter(ls):
    from collections import Counter
    counter_ls = Counter(ls)
    print(counter_ls) 

a = [321,45,612,54,21,321,12,12,21,21,55,54,612,45]
using_counter(a)
print("/////////////////////////////////")

#4 Modified collection counter
def using_counter(ls,eltS):
    from collections import Counter
    counter_ls = Counter(ls)
    print(counter_ls[eltS])

a = [321,45,612,54,21,321,12,12,21,21,55,54,612,45]
using_counter(a,12)
print("::::::::::::::::::::::::::::")

#5 In bUilt

def inBuiltcounter(ls,eltS):
    print(ls.count(eltS))

a = [321,45,612,54,21,321,12,12,21,21,55,54,612,45]
inBuiltcounter(a,15)

b = [321,45,612,54,21,321,12,12,21,21,55,54,612,45]
inBuiltcounter(b,55)
