# find common in 3 sorted lists

from itertools import groupby
def common(a,b,c,n1,n2,n3):
    i=j=k=0
    x=[]
    while(i<n1 and j<n2 and k<n3):
        if(a[i]==b[j] and b[j]==c[k]):
            # print(a[i])
            x.append(a[i])
            i+=1
            j+=1
            k+=1
        elif(a[i]<b[j]):
            i+=1
        elif(b[j]<c[k]):
            j+=1
        else:
            k+=1
    c= (" ".join(str(x[0])for x in list(groupby(x))))
    p=list(c.split())
    return p
ar1 = [1, 5, 10, 20, 40, 80] 
ar2 = [6, 7, 20, 80, 100] 
ar3 = [3, 4, 15, 20, 30, 70, 80, 120]

n1=len(ar1)
n2=len(ar2)
n3=len(ar3)
print(common(ar1,ar2,ar3,n1,n2,n3))