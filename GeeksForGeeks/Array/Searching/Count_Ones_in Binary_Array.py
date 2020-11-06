def countones(arr,low,high,n,x):
    return n-first(arr,0,n-1,n,x)

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
arr=[0,0,0,1,1,1]
n=6
x=1
print(countones(arr,0,n-1,n,1))
