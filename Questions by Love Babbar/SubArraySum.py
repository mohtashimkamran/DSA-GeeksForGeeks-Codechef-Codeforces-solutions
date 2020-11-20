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

# a=[15, 2, 4, 8, 9, 5, 10, 23]
# subArraySum(a,len(a),23)
arr=[4,2,-3,1,6]
n=len(arr)
subArraySum(arr,n,0)
n=len(a)