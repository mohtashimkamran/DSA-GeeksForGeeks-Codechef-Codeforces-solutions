# kedane's  algorithm
def kedane(arr,n):
    curm=arr[0]
    maxm=arr[0]
    for i in range(1,n):
        curm=max(arr[i],curm+arr[i])
        maxm=max(maxm,curm)
    return maxm
arr=[-1,-2,-3,-4]
n=len(arr)
print(kedane(arr,n))
