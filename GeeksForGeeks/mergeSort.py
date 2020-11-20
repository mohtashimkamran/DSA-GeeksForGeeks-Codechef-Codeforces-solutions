def mergeSort(a,l,h):
    if(h>l):
        m=(l+h)//2
        mergeSort(a,l,m)
        mergeSort(a,m+1,h)
        mergefun(a,l,h,m)

def mergefun(a,l,h,m):
    n1=m-l+1
    n2=h-m
    x=a[l:m+1]
    y=a[m+1:h+1]
    i=0
    j=0
    k=l
    while(i<n1 and j<n2):
        if(x[i]<=y[j]):
            a[k]=x[i]
            k+=1
            i+=1
        else:
            a[k]=y[j]
            k+=1
            j+=1
    while(i<n1):
        a[k]=x[i]
        k+=1
        i+=1
    while(j<n2):
        a[k]=y[j]
        k+=1
        j+=1

arr=[1,5,7,9,3,2]
l=0
h=5
mergeSort(arr,l,h)
print(arr)