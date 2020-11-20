# Write a program to cyclically rotate an array by one.

a=[1,2,3,4]
n=len(a)
#insert 0 at first index
a.insert(0, 0)
a[-1],a[0]=a[0],a[-1]
print(a[:n])
