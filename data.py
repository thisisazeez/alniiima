class Node:
    def __init__(self,val):
        self.childleft = None
        self.childright = None
        self.nodedata = val

root = Node(1)
root.childleft = Node(2)
root.childright = Node(3)
root.childleft.childleft = Node(4)
root.childleft.childright = Node(5)

# def InOrd(root):
#     if root:
#         InOrd(root.childleft)
#         print (root.nodedata)
#         InOrd(root.childright)
# InOrd(root)

# def PreOrd(root):
#     if root:
#         print (root.nodedata)
#         PreOrd(root.childleft)
#         PreOrd(root.childright)
# PreOrd(root)

# def PostOrd(root):
#     if root:
#         PostOrd(root.childleft)
#         PostOrd(root.childright)
#         print (root.nodedata)
# PostOrd(root)

def msort(mylist, left, right):
    if right - left > 1:
        middle = (left + right) // 2
        msort(mylist, left, middle)
        msort(mylist, middle, right)
        mlist(mylist, left, middle, right)

def mlist(mylist, left, middle, right):
    leftlist = mylist[left:middle]
    rightlist = mylist[middle:right]
    k = left 
    i = 0
    j = 0
    while(left + i < middle and middle + j < right):
        if (leftlist[i] <= rightlist[j]):
            mylist[k] = leftlist[i]
            i = i + 1
        else:
            mylist[k] = rightlist[j]
            j = j + 1
            k = k + 1
        if left + i < middle:
            while k < right:
                mylist[k] = leftlist[i]
                i = i + 1
                k = k + 1
        else:
            while k < right:
                mylist[k] = rightlist[j]
                j = j + 1
                k = k + 1

mylist = input('Enter the list values to be sorted: ').split()
mylist = [int(x) for x in mylist]
msort(mylist, 0, len(mylist))
print('The sorted list is: ')
print(mylist)