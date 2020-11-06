def search(arr,n,x):
    low = 0
    high = n-1
    while(low<=high):
        mid = (low+high)//2
        if (arr[mid]==x) :
            return mid
        elif(arr[low]<arr[mid]):
            #left half sorted
            if (x>=arr[low] and x<arr[mid]):
                high =mid-1
            else:
                low = mid+1
        else:
            #right half sorted
            if (x>arr[mid] and x<=arr[high]):
                low=mid+1
            else:
                high=mid-1
    return -1
arr=[10,20,40,60,5,8,2]
n=len(arr)
x=8
print(search(arr,n,x))