#Allocate minimum number of pages 
#Asked in FAANG


#naive sollution
# def minpage(arr,n,k):
#     if (k==1):
#         return sum(arr[0:n])
#     if (n==1):
#         return arr[0]
#     res = 1000000000000
#     for i in range(1,n):
#         res = min(res,max(minpage(arr,i,k-1),sum(arr[i:n])))
#     return res
# a=[250,74,159,181,23,45,129,174]
# n=len(a)
# k=6
# print(minpage(a,n,k))

def minpage(arr,n,k):
    sm=sum(arr);mx=max(arr)
    
    low = mx;high=sm;res=0
    while(low<=high):
        mid=(low+high)//2
        if (ispheasible(arr,n,k,mid)):
            res=mid
            high=mid-1
        else:
            low=mid+1
    return res

def ispheasible(arr,n,k,ans):
    req=1;sum=0
    for i in range(n):
        if(sum+arr[i]>ans):
            req+=1
            sum=arr[i]
        else:
            sum+=arr[i]
    return (req<=k)
a=[250,74,159,181,23,45,129,174]
n=len(a)
k=6
print(minpage(a,n,k))