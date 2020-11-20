def sort0s1s2s(arr,n):
    l=0
    h=n-1
    mid=0
    while(mid<=h):
        if(arr[mid]==0):
            arr[mid],arr[l]=arr[l],arr[mid]
            l+=1
            mid+=1
        elif(arr[mid]==1):
            mid+=1
        else:
            arr[mid],arr[h]=arr[h],arr[mid]
            h-=1
    return arr
arr=[0,1,0,1,2,0,1,2,0]
n=len(arr)
print(sort0s1s2s(arr,n))