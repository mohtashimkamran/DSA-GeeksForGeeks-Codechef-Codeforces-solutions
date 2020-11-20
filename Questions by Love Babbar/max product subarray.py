# max product subarray
def maxproduct(arr,n):
    if n==0:
        return -1
    if n==1:
        return a[0]
    ans=a[0]
    max_p=a[0]
    max_n=a[0]

    for i in range(1,n):
        c1=max_n*a[i]
        c2=max_p*a[i]

        max_n=min(a[i],c1,c2)
        max_p=max(a[i],c1,c2)
        ans=max(max_n,max_p)
    return ans

a=[6,-3,-10,0,2]
n=5
print(maxproduct(a,n))