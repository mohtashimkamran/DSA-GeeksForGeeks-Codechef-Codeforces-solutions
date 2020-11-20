# kedane's algorithm
def kedane(arr,n):
    max_so_far=arr[0]
    current_max=arr[0]
    for i in range(1,n):
        current_max=max(arr[i],current_max+arr[i])
        max_so_far=max(max_so_far,current_max)
    return max_so_far
n=int(input())
arr=list(map(int,input().split()))
print(kedane(arr,n))
