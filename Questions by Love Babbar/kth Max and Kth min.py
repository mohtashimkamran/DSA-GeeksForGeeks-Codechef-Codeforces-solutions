# kth Max
b=[1,1,2,5,6,7]
a=list(set(b))
print(a)
k=2
for i in range(k-1):
    # print(min(a),max(a))
    a.remove(min(a))
    a.remove(max(a))
print(min(a))
print(max(a))


def lomuto(a,n,h):
    l=0
    p=h
    j=l-1
    for i in range(l,h):
        if(a[i]<a[p]):
            j+=1
            a[j],a[i]=a[i],a[j]
    a[j+1],a[h]=a[h],a[j+1]
    return j+1
def kthSmallest(a,n,h,k):
    l=0
    while(l<=h):
        p=lomuto(a,n,h)
        if(p==(k-1)):
            return a[p]
        elif(p>(k-1)):
            h=p-1
        else:
            l=p+1
a=[1,2,4,9,3]
n=len(a)
h=n-1
k=2
print(kthSmallest(a,n,h,k))

kth Max
def lomuto(a,n,h):
    l=0
    p=h
    j=l-1
    for i in range(l,h):
        if(a[i]>a[p]):
            j+=1
            a[j],a[i]=a[i],a[j]
    a[j+1],a[h]=a[h],a[j+1]
    return j+1
def kthMax(a,n,h,k):
    l=0
    while(l<=h):
        p=lomuto(a,n,h)
        if(p==(k-1)):
            return a[p]
        elif(p>(k-1)):
            h=p-1
        else:
            l=p+1
a=[1,2,4,9,3]
n=len(a)
h=n-1
k=2
print(kthMax(a,n,h,k))