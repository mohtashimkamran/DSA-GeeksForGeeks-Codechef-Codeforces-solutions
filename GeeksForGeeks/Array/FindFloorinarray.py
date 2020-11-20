def findFloor(arr,n,x):
    y=-1
    low=0
    high=n-1
    while(low<=high):
        mid=(low+high)//2
        if (x==arr[mid]):
            return mid
        elif(arr[mid]>x):
            high = mid-1
        else:
            y=mid
            low = mid+1
    return y
arr=[1,2,8,10,11,12,19]
n= len(arr)
x=5
print(findFloor(arr,n,x))