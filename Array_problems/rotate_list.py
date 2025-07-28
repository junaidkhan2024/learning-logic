#Left rotate/right rotate an array by one position.

#1 manual method

def rotate(ls):
    leftRotate = ls[1:] + [ls[0]] #+ operator between lists works: ✅ [a, b] + [c]
                                  # + between list and single number fails: ❌ [a, b] + c
                                  # So we wrap the number inside [ ] to make it a 1-element list.
    rightRotate = [ls[-1]] + ls[:-1]
    print("left rotated by 1 position", leftRotate)
    print("right rotated by 1 position", rightRotate)

a = [1,2,3,4,5]
rotate(a)
