#wave in array
arr=list(map(int,input().split()))
# j=0
for i in range(0,len(arr)-1,2):
    x=arr[i]
    # print(x)
    arr[i]=arr[i+1]
    arr[i+1]=x
print(arr)