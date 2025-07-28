#Hiow to reverse a string?

#USING  String slicing

# my_string = "arman"
# reversed_string = my_string[::-1] #str[start:stop:step] 
#                                   #start: where to start (default is 0).
#                                   #stop: where to end (default is end of string).
#                                   #step: how many steps to move each time.
#                                   #start and stop are empty → so it takes the whole string.
#                                   #step = -1 → it goes backward, reversing the string.
# print(reversed_string)

# a = "junaid"
# r = a[::-1]
# print(r)

def reverseString(str): #1 method
    New_String = str[::-1]
    print(New_String)


a ="tac"
reverseString(a)

#USING .reversed() and .join() method 
def reversewithjoinandreversed(st): #2nd method
    new = "".join(reversed(st)) # reversed() gives a object hence cant print it directly
    print(f"in reversed {new}")

name = "khansaab"
reversewithjoinandreversed(name)
print("_________")


#USING loop

# name = "Ahmad"
# r = ""
# for char in name:
#     r = char + r # here each time one char will be added in the new string and each time the new one will
#                  #take place at front(at first charcetor) hence at the end it will be reverse of the orignal string
# print(r)


def revS(str): #3 method
    New_string = ""
    for char in str:
        New_string = char + New_string
    print(New_string)

student = "khubaib"
revS(student)

#USIng while loop

def reverse(str): #4 methhod
    newstr = ""
    index = len(str) - 1 # it gives len till total elements in string
    while index >= 0:
        newstr += str[index] # same as newstr = newstr + str[index] 
        index -= 1
    return newstr
name = "minhaj"
print(reverse(name))    


# print("trying************************")
# a = "abc"
# print(reversed(a))
# print("".join(reversed(a)))
