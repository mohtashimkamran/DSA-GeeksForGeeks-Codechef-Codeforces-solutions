l=0
r=0
def pairSum(arr,n,x):
    left=0
    right=n-1
    count=0
    global l
    global r
    while(left<right):
        if((arr[left]**2)+(arr[right]**2)==(x**2)):
            # return (arr[left],arr[right])
            l=arr[left]
            r=arr[right]
            count+=1
            right-=1
            left+=1
            # return count
        elif((arr[left]**2)+(arr[right]**2)>(x**2)):
            right-=1
        else:
            left+=1
    return count
a=[1,2,3,4,5]
n=5
x=5
pairSum(a,n,x)
print(l,r)
