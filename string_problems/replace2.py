# replace

def urlify1(st):
    ls = []
    for ch in st:
        if ch == " ":
            ls.append("%20")
        else:
            ls.append(ch)
    print("".join(ls))

a = " a string with spaces."
urlify1(a)
print()

#in built

def urlifyinbuilt(st):
    print(st.replace(" ","%20"))

a = "  another string with space. "
urlifyinbuilt(a)
print()


#With List comprehension and join
def listcomprihension(st):
    print("".join(["%20" if ch == " " else ch for ch in st]))

a = " one more string with spaces .1 1 1 "
listcomprihension(a)
