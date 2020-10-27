#Leaders in array
def leader(arr,n):
    currentleader=arr[n-1]
    print(currentleader)
    for i in range(n-2,-1,-1):
        if currentleader<=arr[i]:
            print(arr[i])
            currentleader=arr[i]
n=int(input())
arr=list(map(int,input().split()))
leader(arr,n)