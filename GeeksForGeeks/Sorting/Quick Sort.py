# Quick Sort
def lomato(a,l,h):
    p=h
    i=l-1
    for j in range(l,h):
        if(a[j]<a[p]):
            i+=1
            a[i],a[j]=a[j],a[i]
    a[i+1],a[h]=a[h],a[i+1]
    return i+1
def quicksort(a,l,h):
    if(l<h):
        p=lomato(a,l,h)
        quicksort(a,l,p-1)
        quicksort(a,p+1,h)
    return a
l=0
a=[10,80,30,90,40,50,70]
h=len(a)-1
print(quicksort(a,l,h))