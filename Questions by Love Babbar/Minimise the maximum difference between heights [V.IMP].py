#Minimise the maximum difference between heights [V.IMP]
def Minimise_the_maximum_difference_between_heights(arr, k, size):
    a=[]
    maxarr=max(arr)
    difference=maxarr-k
    for i in range(n):
        b=arr[i]+k
        if(b<difference):
            a.append(b)
        else:
            a.append(arr[i]-k)
    return (max(a)-min(a))
arr=[1,15,16]
k=5
n=3
print(Minimise_the_maximum_difference_between_heights(arr,k,n))
