# find all pairs on integer array whose sum is equal to given number
l=0
r=0
def pairSum(arr,n,x):
    left=0
    n=len(arr)
    right=n-1
    count=0
    global l
    global r
    while(left<right):
        if(arr[left]+arr[right]==x):
            # return (arr[left],arr[right])
            count+=1
            right-=1
            left+=1
            l=arr[left]
            r=arr[right]
            # return count
        elif(arr[left]+arr[right]>x):
            right-=1
        else:
            left+=1
    return count
arr=[1,2,3,4,5,6,7]
n=len(arr)
x=9
print(pairSum(arr,n,x),l,r)
