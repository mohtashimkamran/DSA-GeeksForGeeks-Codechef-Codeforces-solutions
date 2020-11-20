# given an aray if non -ve numbers
# find if there is a subarray of given sum
# arr=[1,4,20,3,10,5]
# n=len(arr)
# k=33
# flg=0
# for i in range(n):
#     sum=0
#     for j in range(i,n):
#         sum += arr[j]
#         if sum==k:
#             flg=1
# if flg==1:
#     print("YES")
# else:
#     print("nO")

# a=[15, 2, 4, 8, 9, 5, 10, 23]
# curr_sum=a[0]
# start=0
# n=len(a)
# i=1
# given_sum=23
# while(i<=n):
#     while curr_sum>given_sum and start<i-1:
#         curr_sum=curr_sum-a[start]
#         start+=1
#     if curr_sum==given_sum:
#         print(start,i-1)

#     if (i<n):
#         curr_sum+=a[i]
#     i+=1


def subArraySum(arr, n, sum):
    i = 1
    start = 0
    total = arr[0]
    while i <= n:
        while total > sum and start < i-1:
            total = total - arr[start]
            start += 1
        if total == sum:
            print (start+1, i,end ="")
            return
        if i < n:
             total = total + arr[i]
        i += 1
    print(-1,end="")

a=[15, 2, 4, 8, 9, 5, 10, 23]
subArraySum(a,len(a),23)