#index of last occured elemenet in array
def last(arr,low,high,n,x):
    if low>high:
        return -1
    mid = (low+high)//2
    if(x>arr[mid]):
        return last(arr,mid+1,high,n,x)
    elif(x<arr[mid]):
        return last(arr,low,mid-1,n,x)
    else:
        if(mid==n-1 or arr[mid]!=arr[mid+1]):
            return mid
        else:
            return last(arr,mid+1,high,n,x)
arr=[1,2,2,4,5,6,6,6,6]
n=9
x=6
print(last(arr,0,n-1,n,x))


