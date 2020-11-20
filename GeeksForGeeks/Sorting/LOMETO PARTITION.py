# LOMETO PARTITION
# a=[10,80,30,90,40,50,70]
n=int(input())
a=list(map(int,input().split()))
# partition=int(input())
# a[partition],a[n-1]=a[n-1],a[partition]
pivot=n-1
high=n-1
low=0
i=low-1
for j in range(low,high):
    if(a[j]<a[pivot]):
        i+=1
        a[i],a[j]=a[j],a[i]
a[i+1],a[high]=a[high],a[i+1]
print(a)

def lomato(a,l,h,n):
    p=n-1
    i=l-1
    for j in range(l,h):
        if(a[j]<a[p]):
            i+=1
            a[i],a[j]=a[j],a[i]
    a[i+1],a[h]=a[h],a[i+1]
    return a

l=0
a=[10,80,30,90,40,50,70]
n=len(a)
h=n-1
print(lomato(a,l,h,n))