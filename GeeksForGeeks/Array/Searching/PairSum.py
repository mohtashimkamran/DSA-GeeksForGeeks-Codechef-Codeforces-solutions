#two pointer approach
# given a sorted array and a sum count total pairs of given sum
def pairSum(arr,n,x):
    left=0
    right=n-1
    count=0
    while(left<right):
        if(arr[left]+arr[right]==x):
            # return (arr[left],arr[right])
            count+=1
            right-=1
            left+=1
            # return count
        elif(arr[left]+arr[right]>x):
            right-=1
        else:
            left+=1
    return count

arr=[1,2,3,4,5,6,7]
n=len(arr)
x=5
print(pairSum(arr,n,x))