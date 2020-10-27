#rotate an array by d elements
def rotate(arr,n,d):
    reverse(arr,0,d-1)
    reverse(arr,d,n-1)
    reverse(arr,0,n-1)
    return arr
def reverse(arr,low,high):
    while(low<high):
        temp=arr[low]
        arr[low]=arr[high]
        arr[high]=temp
        low+=1
        high-=1

arr=[1,2,3,4,5]
n=5
d=2
print(rotate(arr,n,d))