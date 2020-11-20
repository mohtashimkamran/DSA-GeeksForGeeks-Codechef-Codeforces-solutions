
# Given an array which consists of only 0, 1 and 2. Sort the array without using any sorting algo
def sortOs1s2s(arr,n):
    l=0
    mid=0
    h=n-1
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
arr=[1,0,2,0,1,2]
n=len(arr)