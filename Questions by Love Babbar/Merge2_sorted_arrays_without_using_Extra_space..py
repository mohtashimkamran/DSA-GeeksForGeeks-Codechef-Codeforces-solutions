# Merge 2 sorted arrays without using Extra space.
a=[1,2,3,4]
b=[0,1,2,3]
a[:]=sorted(a+b)
b.clear()
print(a)