# Radix Sort
def countingSort(arr,n,exp):
    c=[0]*10
    op=[0]*n
    for j in range(n):
        index = arr[j]//exp
        c[int(index)%10]+=1
    for k in range(1,10):
        c[k]+=c[k-1]
    i=n-1
    while(i>=0):
        index=arr[i]//exp
        op[c[int(index%10)]-1]=arr[i]
        c[int(index%10)]-=1
        i-=1
    i=0
    for i in range(n):
        arr[i]=op[i]

def RadixSort(arr,n):
    mx = max(arr)
    exp=1
    while (mx//exp)>0:
        countingSort(arr,n,exp)
        exp*=10
    return arr
a=[312,212,5,90,787]
n=len(a)
print(RadixSort(a,n))