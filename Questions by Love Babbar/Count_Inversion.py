# Count Inversion

arr=[2,4,1,3,5]
for i in range(len(arr)):
    for j in range(i,len(arr)):
        if((i<j and arr[i]>arr[j]) or (i>j) and (arr[i]<arr[j])):
            print(arr[i],arr[j])