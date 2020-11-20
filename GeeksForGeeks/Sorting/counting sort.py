# counting sort
def countingSort(arr,n,k):
    c=[0]*k
    for i in range(n):
        c[arr[i]]+=1
    index=0
    for i in range(k):
        for _ in range(c[i]):
            arr[index]=i
            index+=1
    return arr
a=[5,4,3,2,1]
k=6
n=len(a)
print(countingSort(a,n,k))
