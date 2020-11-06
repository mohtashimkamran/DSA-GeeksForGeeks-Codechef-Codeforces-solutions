#indexof 1st occured no if multiple same no is present in list
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
arr=[1,2,2,4,5,6]
n=6
x=2
print(first(arr,0,n-1,n,x))