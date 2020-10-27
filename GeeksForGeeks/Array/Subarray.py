# given an aray if non -ve numbers
# find if there is a subarray of given sum
arr=[1,4,20,3,10,5]
n=len(arr)
k=33
flg=0
for i in range(n):
    sum=0
    for j in range(i,n):
        sum += arr[j]
        if sum==k:
            flg=1
if flg==1:
    print("YES")
else:
    print("nO")