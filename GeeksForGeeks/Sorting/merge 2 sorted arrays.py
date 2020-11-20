# merge 2 sorted arrays

def mergeSorted(a,b,n,m):
    i=0
    j=0
    x=[]
    while(i<n and j<m):
        if(a[i]<b[j]):
            x.append(a[i])
            i+=1
        else:
            x.append(b[j])
            j+=1

    while(i<n):
        x.append(a[i])
        i+=1
    while(j<m):
        x.append(b[j])
        j+=1
    print(x)
a=[1,3,4]
b=[1,2,3]