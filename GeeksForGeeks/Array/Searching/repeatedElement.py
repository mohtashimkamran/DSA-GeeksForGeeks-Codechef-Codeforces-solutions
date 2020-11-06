#efficient approach for repeated elements
a=[1,2,3,3,4,4]
arr=[False]*len(a)
for i in range(len(a)):
    if arr[a[i]]==True:
        print(a[i])
    arr[a[i]]=True