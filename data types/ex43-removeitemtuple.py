t1=(1,2,3,4,5)
print("Before removing : ",t1)
l1=list(t1)
item=int(input("Enter item to remove "))
l1.pop(l1.index(item))
t1=tuple(l1)
print("After removing item : ")
print(t1)