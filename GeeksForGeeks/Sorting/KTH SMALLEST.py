# KTH SMALLEST

def lomato(a,l,h):
    p=h
    i=l-1
    for j in range(l,h):
        if(a[j]<a[p]):
            i+=1
            a[i],a[j]=a[j],a[i]
    a[i+1],a[h]=a[h],a[i+1]
    return i+1
def KthSmallest(a,l,h,k):
    while(l<=h):
        p=lomato(a,l,h)
        if(p==(k-1)):
            return a[p]
        elif(p>(k-1)):
            h=p-1
        else:
            l=p+1
    return -1
a=[10,80,30,90,40,50,70]
l=0
h=len(a)-1
k=2
print(KthSmallest(a,l,h,k))