# meeting maximum guests
def maxguest(arr,n,dep):
    i=1;j=0;count=1;res=1
    arr.sort()
    dep.sort()
    while(i<n and j<n):
        if(arr[i]<=dep[j]):
            count+=1
            i+=1
        else:
            j+=1
            count-=1
        res=max(res,count)
    return res
arr=[10,12,20]
dep=[20,25,30]
n=3
print(maxguest(arr,n,dep))