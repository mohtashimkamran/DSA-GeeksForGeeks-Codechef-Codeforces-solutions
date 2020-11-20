# BUBBLE SORT

a=[1,4,5,9,2]
a=list(map(int,input().split()))
for i in range(0,len(a)):
    for j in range(i,len(a)):
        if (a[i]>a[j]):
            a[i],a[j]=a[j],a[i]
print(a)