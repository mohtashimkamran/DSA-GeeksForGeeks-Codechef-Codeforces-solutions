n,k = map(int,input().split())
arr=list(map(int,input().split()))
if arr[-1]!=k:  # 1 2 3 5 3 2 1 3 1 2
    arr.reverse()
    s=0
    for i in range(len(arr)):
        s+=arr[i]
        if s==arr[i]:
            s=s-arr[i]
            arr[i],arr[i-1]=arr[i-1],arr[i]
print("YES")
print(arr)