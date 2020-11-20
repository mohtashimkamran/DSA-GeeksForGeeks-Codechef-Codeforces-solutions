def count(arr,low,high,n,x):
    if first(arr,0,n-1,n,x) ==-1:
        return -1
    return last(arr,0,n-1,n,x)-first(arr,0,n-1,n,x)+1

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
def first(arr,low,high,n,x):
    if low>high:
        return -1
    mid = (low+high)//2
    if(x>arr[mid]):
        return first(arr,mid+1,high,n,x)
    elif(x<arr[mid]):
        return first(arr,low,mid-1,n,x)
    else:
        if(mid==0 or arr[mid]!=arr[mid-1]):
            return mid
        else:
            return first(arr,low,mid-1,n,x)
arr=[1,2,2,4,5,6,6,6,6]
n=9
x=3
print(count(arr,0,n-1,n,x))
