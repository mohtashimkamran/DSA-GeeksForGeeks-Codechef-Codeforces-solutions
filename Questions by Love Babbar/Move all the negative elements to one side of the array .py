# Move all the negative elements to one side of the array 

def moveNegative(arr,n):
    # h=n-1
    l=0
    k=l-1
    for i in range(n):
        if(arr[i]<0):
            k+=1
            arr[k],arr[i]=arr[i],arr[k]
    return arr
arr=[1,-3,9,8,-5,-6]
n=len(arr)
print(moveNegative(arr,n))